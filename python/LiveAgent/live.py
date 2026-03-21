import flet as ft
import asyncio
import threading

from utils.core import LiveAgentCore

async def app(page: ft.Page):

	# setup
	page.title = "LiveAgent"
	page.window.width = 400
	page.window.height = 300
	page.scroll = 'AUTO'
	page.fonts = {"Google Sans": "./assets/Product Sans Regular.ttf"}
	page.theme = ft.Theme(font_family="Google Sans")

	# components
	stop_btn = ft.OutlinedButton(text="Stop", width=page.width)
	cb_audio = ft.Checkbox(label="Mic", value=True)
	cb_screen = ft.Checkbox(label="Screen", value=True)
	text_rtn = ft.Text("...")
	input_text = ft.TextField(label="Send Text")
	input_btn = ft.IconButton(icon=ft.Icons.SEND,icon_size=20)
	page.add(
		ft.Column(controls=[
			ft.Row(controls=[
				input_text, input_btn
			],width=page.width,expand=True),
			ft.Row(controls=[
				ft.Text("Input:"), cb_audio, cb_screen,
			]),
			ft.Card(content=ft.Container(content=text_rtn, margin=15), width=page.width),
			stop_btn
		],expand=True,alignment=ft.MainAxisAlignment.END)
	)
	page.update()

	# AI
	core = LiveAgentCore()
	async def text_callback(text):
		text_rtn.value += text
		page.update()
	core.set_text_callback(text_callback)
	def start_session(e):
		try:
			core.enable_mic(cb_audio.value)
			core.enable_screen(cb_screen.value)
			def run_core():
				loop = asyncio.new_event_loop()
				asyncio.set_event_loop(loop)
				loop.run_until_complete(core.start())
			thread = threading.Thread(target=run_core, daemon=True)
			thread.start()
		except Exception as ex:
			text_rtn.value = f"Error: {str(ex)}"
			page.update()
	async def stop_session(e):
		try:
			await core.stop()
		except Exception as ex:
			text_rtn.value = f"Error: {str(ex)}"
			page.update()
	async def send_text(e):
		try:
			if input_text.value:
				await core.send_text(input_text.value)
				input_text.value = ""
				page.update()
		except Exception as ex:
			text_rtn.value = f"Error: {str(ex)}"
			page.update()
	def toggle_audio(e):
		if core:
			core.enable_mic(cb_audio.value)
	def toggle_screen(e):
		if core:
			core.enable_screen(cb_screen.value)
	stop_btn.on_click = stop_session
	input_btn.on_click = send_text
	cb_audio.on_change = toggle_audio
	cb_screen.on_change = toggle_screen
	start_session(None)

ft.app(app)