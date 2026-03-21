# 该文件基本上是由AI编写的（GLM-4.6）
# This file is basically written by AI (GLM-4.6)

import os
import asyncio
import base64
import io
import traceback
import json

import pyaudio
import mss
import PIL.Image
import numpy as np

from google import genai
from google.genai import types

from tools import tools_list

# 音频配置
FORMAT = pyaudio.paInt16
CHANNELS = 1
SEND_SAMPLE_RATE = 16000
RECEIVE_SAMPLE_RATE = 24000
CHUNK_SIZE = 1024

# 默认配置
DEFAULT_API_KEY = "YOUR_API_KEY"
DEFAULT_MODEL = "models/gemini-2.0-flash-exp"
DEFAULT_VOICE = "Zephyr"


class LiveAgentCore:
    """简化的 LiveAgent API 核心库，支持音频和文本交互"""
    
    def __init__(self, config_file="config.json", prompt_file="utils/prompt.md"):
        """
        初始化 LiveAgent Core
        
        Args:
            config_file: 配置文件路径，默认为 config.json
            prompt_file: 提示词文件路径，默认为 utils/prompt.md
        """
        self.config_file = config_file
        self.prompt_file = prompt_file
        self.config = None
        self.client = None
        self.session = None
        self.model = "models/gemini-2.0-flash-exp"
        
        # 音频相关
        self.pya = pyaudio.PyAudio()
        self.audio_stream = None
        self.audio_in_queue = None
        self.out_queue = None
        
        # 任务控制
        self.send_text_task = None
        self.receive_audio_task = None
        self.play_audio_task = None
        self.listen_audio_task = None
        
        # 状态控制
        self.mic_enabled = True
        self.screen_enabled = True
        self.running = False
        
        # 音频缓冲控制
        self.audio_buffer = []
        self.is_response_complete = False
        self.buffer_lock = asyncio.Lock()
        
        # 回调函数
        self.text_callback = None
        
        # 加载配置
        self._load_config()
    
    def _load_config(self):
        """从 config.json 和 prompt.md 文件加载配置"""
        try:
            # 加载配置文件
            with open(self.config_file) as f:
                config_from_file = json.load(f)
            
            # 加载系统提示词
            with open(self.prompt_file) as f:
                sys_prompt = f.read()
            
            # 创建客户端
            self.client = genai.Client(
                http_options={"api_version": "v1beta"},
                api_key=config_from_file['key']
            )
            
            self.tools = tools_list
            if config_from_file['search']:
                self.tools.append({'google_search': {}}) #TODO:
            
            # 创建配置
            self.config = types.LiveConnectConfig(
                response_modalities=[types.Modality.TEXT if config_from_file['modalities'] == "TEXT" else types.Modality.AUDIO],
                realtime_input_config=types.RealtimeInputConfig(
                    automatic_activity_detection={
                        "disabled": False,
                        "start_of_speech_sensitivity": types.StartSensitivity.START_SENSITIVITY_HIGH,
                        "end_of_speech_sensitivity": types.EndSensitivity.END_SENSITIVITY_LOW,
                        "prefix_padding_ms": 100,
                        "silence_duration_ms": 500
                    },
                    activity_handling=types.ActivityHandling.START_OF_ACTIVITY_INTERRUPTS
                ),
                speech_config={
                    "voice_config": {
                        "prebuilt_voice_config": {
                            "voice_name": config_from_file['voice']
                        }
                    }
                },
                context_window_compression=types.ContextWindowCompressionConfig(
                    trigger_tokens=25600,
                    sliding_window=types.SlidingWindow(target_tokens=12800),
                ),
                media_resolution=types.MediaResolution(['MEDIA_RESOLUTION_LOW', 'MEDIA_RESOLUTION_MEDIUM', 'MEDIA_RESOLUTION_HIGH'][config_from_file['media_resolution_num']]),
                system_instruction=sys_prompt,
                tools=self.tools
            )
            
        except FileNotFoundError:
            print(f"找不到配置文件 {self.config_file} 或 {self.prompt_file}")
            raise
        except json.JSONDecodeError:
            print(f"无效的 {self.config_file} 文件")
            raise
        except Exception as e:
            print(f"加载配置文件时出错: {e}")
            raise
    
    def set_text_callback(self, callback):
        """设置文本回调函数"""
        self.text_callback = callback
    
    def enable_mic(self, enabled=True):
        """启用或禁用麦克风"""
        self.mic_enabled = enabled
        if not enabled and self.audio_stream:
            self.audio_stream.close()
            self.audio_stream = None
    
    def enable_screen(self, enabled=True):
        """启用或禁用屏幕捕获"""
        self.screen_enabled = enabled
    
    async def send_text(self, text):
        """发送文本到服务器"""
        if self.session:
            await self.session.send_client_content(
                turns={"role": "user", "parts": [{"text": text or "."}]}, 
                turn_complete=True
            )
    
    async def send_and_wait(self, text):
        """发送文本并等待响应"""
        if not self.session:
            print("会话未启动")
            return
        
        # 重置响应状态
        async with self.buffer_lock:
            self.audio_buffer.clear()
            self.is_response_complete = False
        
        # 发送文本
        await self.send_text(text)
        
        # 等待响应完成
        await asyncio.sleep(1)  # 给服务器一些时间处理
    
    def _get_screen(self):
        """获取屏幕截图"""
        sct = mss.mss()
        monitor = sct.monitors[0]
        i = sct.grab(monitor)
        
        mime_type = "image/jpeg"
        image_bytes = mss.tools.to_png(i.rgb, i.size)
        img = PIL.Image.open(io.BytesIO(image_bytes))
        
        image_io = io.BytesIO()
        img.save(image_io, format="jpeg")
        image_io.seek(0)
        
        image_bytes = image_io.read()
        return {"mime_type": mime_type, "data": base64.b64encode(image_bytes).decode()}
    
    async def get_screen(self):
        """持续获取屏幕截图"""
        while self.screen_enabled and self.running:
            frame = await asyncio.to_thread(self._get_screen)
            if frame is None:
                break
            
            await asyncio.sleep(1.0)
            if self.out_queue:
                print('[LOG] SS')
                await self.out_queue.put(frame)
    
    async def send_realtime_input(self):
        """发送实时输入到服务器"""
        while self.running:
            try:
                if self.out_queue:
                    msg = await self.out_queue.get()
                    print('[LOG] RT')
                    await self.session.send_realtime_input(media=msg)
                else:
                    await asyncio.sleep(0.1)
            except Exception as e:
                print(f"发送实时输入错误: {e}")
                await asyncio.sleep(0.1)
    
    async def listen_audio(self):
        """监听音频输入"""
        if not self.mic_enabled:
            return
            
        mic_info = self.pya.get_default_input_device_info()
        self.audio_stream = await asyncio.to_thread(
            self.pya.open,
            format=FORMAT,
            channels=CHANNELS,
            rate=SEND_SAMPLE_RATE,
            input=True,
            input_device_index=mic_info["index"],
            frames_per_buffer=CHUNK_SIZE,
        )
        
        if __debug__:
            kwargs = {"exception_on_overflow": False}
        else:
            kwargs = {}
            
        while self.mic_enabled and self.running:
            try:
                data = await asyncio.to_thread(self.audio_stream.read, CHUNK_SIZE, **kwargs)
                if self.out_queue and not self.out_queue.full():
                    # 非阻塞方式放入队列，如果队列满了就跳过这一帧
                    try:
                        print('[LOG] AAAA')
                        self.out_queue.put_nowait({"data": data, "mime_type": "audio/pcm"})
                    except asyncio.QueueFull:
                        # 队列满了，跳过这一帧音频数据
                        continue
                else:
                    # 如果队列不存在或满了，短暂等待
                    await asyncio.sleep(0.01)
            except Exception as e:
                print(f"音频读取错误: {e}")
                await asyncio.sleep(0.1)
    
    async def receive_audio(self):
        """接收音频响应 - 使用小缓冲区减少卡顿"""
        while self.running:
            try:
                turn = self.session.receive()
                async for response in turn:
                    if data := response.data:
                        # 使用小缓冲区策略：每2个块播放一个，保持连接活跃
                        async with self.buffer_lock:
                            self.audio_buffer.append(data)
                            print('[LOG] Received audio chunk')
                            # 当缓冲区达到2个块时，播放第一个
                            if len(self.audio_buffer) >= 2:
                                if self.audio_in_queue:
                                    self.audio_in_queue.put_nowait(self.audio_buffer.pop(0))
                        continue
                    
                    if text := response.text:
                        print(text, end="")
                        if self.text_callback:
                            await self.text_callback(text)
                
                # 响应完成，播放所有剩余的音频数据
                async with self.buffer_lock:
                    self.is_response_complete = True
                    # 将缓冲的音频数据放入播放队列
                    for chunk in self.audio_buffer:
                        if self.audio_in_queue:
                            self.audio_in_queue.put_nowait(chunk)
                    # 清空缓冲区
                    self.audio_buffer.clear()
            except Exception as e:
                print(f"接收音频时出错: {e}")
                break
    
    async def play_audio(self):
        """播放音频 - 简化实现确保声音正常播放"""
        stream = await asyncio.to_thread(
            self.pya.open,
            format=FORMAT,
            channels=CHANNELS,
            rate=RECEIVE_SAMPLE_RATE,
            output=True,
        )
        
        try:
            while self.running:
                # 直接从队列获取音频数据并播放
                bytestream = await self.audio_in_queue.get()
                if bytestream:
                    # 增加音量 - 将音频数据放大2倍
                    audio_array = np.frombuffer(bytestream, dtype=np.int16)
                    amplified_audio = np.clip(audio_array * 2, -32768, 32767).astype(np.int16)
                    await asyncio.to_thread(stream.write, amplified_audio.tobytes())
        finally:
            stream.close()
    
    async def start(self):
        """启动 LiveAgent 会话"""
        if self.running:
            return
        
        self.running = True
        
        try:
            async with (
                self.client.aio.live.connect(model=self.model, config=self.config) as session,
                asyncio.TaskGroup() as tg,
            ):
                self.session = session
                self.audio_in_queue = asyncio.Queue()
                self.out_queue = asyncio.Queue(maxsize=10)
                
                # 创建任务
                self.send_realtime_task = tg.create_task(self.send_realtime_input())
                tg.create_task(self.receive_audio())
                tg.create_task(self.play_audio())
                
                # 根据设置启用麦克风和屏幕
                if self.mic_enabled:
                    tg.create_task(self.listen_audio())
                
                if self.screen_enabled:
                    tg.create_task(self.get_screen())
                
                # 等待用户退出
                while self.running:
                    await asyncio.sleep(1)
                
        except asyncio.CancelledError:
            pass
        except Exception as e:
            print(f"运行时错误: {e}")
            traceback.print_exc()
        finally:
            self.running = False
            if self.audio_stream:
                self.audio_stream.close()
    
    async def stop(self):
        """停止 LiveAgent 会话"""
        self.running = False
        self.enable_mic(False)
        self.enable_screen(False)
        
        # 取消所有任务
        tasks = [
            self.send_realtime_task,
            self.receive_audio_task,
            self.play_audio_task,
            self.listen_audio_task,
        ]
        
        for task in tasks:
            if task and not task.done():
                task.cancel()


# 测试代码
if __name__ == "__main__":
    async def test_text_callback(text):
        """测试文本回调函数"""
        print(f"\n[回调接收到文本]: {text}")
    
    async def test():
        """测试函数 - 交互式控制台测试"""
        try:
            # 创建核心实例，自动读取 config.json
            core = LiveAgentCore()
            
            # 设置文本回调
            core.set_text_callback(test_text_callback)
            
            print("启动 LiveAgent Core...")
            print("命令说明:")
            print("  输入文本 - 发送文本消息")
            print("  mic on/off - 开启/关闭麦克风")
            print("  screen on/off - 开启/关闭屏幕捕获")
            print("  q - 退出程序")
            print()
            
            # 启用麦克风和屏幕
            core.enable_mic(True)
            core.enable_screen(True)
            print("已启用麦克风和屏幕捕获")
            
            # 启动会话任务
            start_task = asyncio.create_task(core.start())
            
            # 等待会话建立
            await asyncio.sleep(2)
            
            # 交互式控制台
            while core.running:
                try:
                    # 获取用户输入
                    text = await asyncio.to_thread(input, "message > ")
                    
                    if text.lower() == 'q':
                        break
                    elif text.lower() == 'mic on':
                        core.enable_mic(True)
                        print("麦克风已开启")
                    elif text.lower() == 'mic off':
                        core.enable_mic(False)
                        print("麦克风已关闭")
                    elif text.lower() == 'screen on':
                        core.enable_screen(True)
                        print("屏幕捕获已开启")
                    elif text.lower() == 'screen off':
                        core.enable_screen(False)
                        print("屏幕捕获已关闭")
                    elif text.strip():
                        # 发送文本消息
                        await core.send_text(text)
                    else:
                        print("请输入有效命令或文本，或输入 'q' 退出")
                        
                except KeyboardInterrupt:
                    break
                except Exception as e:
                    print(f"处理输入时出错: {e}")
            
            # 停止会话
            print("停止会话...")
            await core.stop()
            await start_task
            
        except Exception as e:
            print(f"测试失败: {e}")
            print("请确保 config.json 和 utils/prompt.md 文件存在且格式正确")
            print("请检查麦克风和屏幕权限是否正常")
    
    # 运行测试
    asyncio.run(test())