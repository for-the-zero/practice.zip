import subprocess
import re
import os

def get_list():
	#packages = subprocess.check_output("adb shell pm list packages -3", shell=True).decode('utf-8')
	#packages = re.findall(r"package:(.*)\r\n", packages)

	list=[]

	paths = subprocess.check_output("adb shell pm list packages -3 -f", shell=True).decode('utf-8')
	paths = re.findall(r"/data\/app\/[^\/]+\/[^\/.]+\.apk", paths)
	#return paths

	os.system("adb push aapt-arm-pie /data/local/tmp")
	os.system("adb shell chmod 0755 /data/local/tmp/aapt-arm-pie")
	for path in paths:
		called = subprocess.check_output("adb shell /data/local/tmp/aapt-arm-pie dump badging "+path+"", shell=True).decode('utf-8')
		package_name = re.findall(r"'(.*?)'", called)
		app_name = re.findall(r"application-label:'(.*)'", called)
		list.append([path, package_name[0], app_name[0]])
	os.system("adb shell rm /data/local/tmp/aapt-arm-pie")

	return list

def desktop_path():
	import winreg
	key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
	path = winreg.QueryValueEx(key, 'Desktop')[0]
	return path

def push(path, opath, name):
	#print("rename "+opath+r"\base.apk "+name+".apk")
	#return None
	os.system('adb pull '+path+' "'+opath+'"')
	os.system('rename "'+opath+r'\base.apk" "'+name+'.apk"')

if __name__ == "__main__":
	print(get_list())
	#print(desktop_path())
	#push("/data/app/com.quark.browser-IyjWJ6IwPhbhL4sSrmm4YA==/base.apk",desktop_path(),"夸克")

'''
[
	['/data/app/com.quark.browser-IyjWJ6IwPhbhL4sSrmm4YA==/base.apk', 'com.quark.browser', '夸克'],
	['/data/app/wangdaye.com.geometricweather-DTmEn8HTZyV3M444wab7ZA==/base.apk', 'wangdaye.com.geometricweather', 'Geometric Weather'],
	['/data/app/org.getlantern.lantern-JNl-rXElMExwwo0eiR3OXQ==/base.apk', 'org.getlantern.lantern', 'Lantern'],
	['/data/app/com.niksoftware.snapseed-EHbgftY_5qJJ8rqdKPnSAA==/base.apk', 'com.niksoftware.snapseed', 'Snapseed'],
	['/data/app/com.zhipuai.qingyan--Yg0Ky45fMrp-rbk5pYung==/base.apk', 'com.zhipuai.qingyan', '智谱清言'],
	['/data/app/free.v2ray.proxy.VPN-zoKKkL_0A_aLHz2kdnwdFA==/base.apk', 'free.v2ray.proxy.VPN', 'V2ray VPN'],
	['/data/app/me.gfuil.bmap-OI7R7Nzi2iBSqS7qf03RBQ==/base.apk', 'me.gfuil.bmap', '白马地图'],
	['/data/app/com.lemonpiggy.school-mFC33lVL-YPh1lnmD3I1dA==/base.apk', 'com.lemonpiggy.school', '柠檬自习室'],
	['/data/app/com.discord-QSK52gMSNCHXIBtvwck0bQ==/base.apk', 'com.discord', 'Discord'],
	['/data/app/me.zhanghai.android.files-OpOn_kcihuEU9w0qHX9xjA==/base.apk', 'me.zhanghai.android.files', 'Material Files'],
	['/data/app/com.mihoyo.hyperion-tVe8V4uDvsUmjnqYhtftRA==/base.apk', 'com.mihoyo.hyperion', '米游社'],
	['/data/app/net.idik.timo-ev-QSvrR6Xvm24sVErpEBQ==/base.apk', 'net.idik.timo', 'Timo笔记'],
	['/data/app/com.v2cross.proxy-J1bvLLYffW5Um3-sR28nIA==/base.apk', 'com.v2cross.proxy', 'Shadowrocket'],
	['/data/app/com.aliyun.tongyi-mxBzJFF52ZChZAsKnJ8vSQ==/base.apk', 'com.aliyun.tongyi', '通义千问'],
	['/data/app/com.mobile.cloudgames-ioC0YiO64YBkPtYnmBsQTg==/base.apk', 'com.mobile.cloudgames', '870游戏'],
	['/data/app/com.chrome.canary-Z57x8q73FTLuv1Tst1CKmw==/base.apk', 'com.chrome.canary', 'Chrome Canary'],
	['/data/app/com.tencent.mm-iB5WNrsmAgtp46j_CJIsTQ==/base.apk', 'com.tencent.mm', 'WeChat'],
	['/data/app/me.piebridge.brevent-kMYzOZqrt3PZ1HDTOMLXqQ==/base.apk', 'me.piebridge.brevent', 'Brevent'],
	['/data/app/org.localsend.localsend_app-zgcpDi5fbmXHB9jrHtUNAw==/base.apk', 'org.localsend.localsend_app', 'LocalSend'],
	['/data/app/com.microsoft.math-lcwuNJwqcmbDNauPEDadDQ==/base.apk', 'com.microsoft.math', 'Math'],
	['/data/app/com.microsoft.office.outlook-xPjTsT3TvzKS37oukYK3Vg==/base.apk', 'com.microsoft.office.outlook', 'Outlook'],
	['/data/app/com.microsoft.office.officehub-GJ6jXJob4Hl_Ow5eZwHN4Q==/base.apk', 'com.microsoft.office.officehub', 'Microsoft 365 (Office)'],
	['/data/app/com.tencent.ehe-OO2H0hsx9Ogv4Xx7GT8R0Q==/base.apk', 'com.tencent.ehe', '鹅盒'],
	['/data/app/com.ruanmei.ithome-f_53gZkDXFAa-sYPeledig==/base.apk', 'com.ruanmei.ithome', 'IT之家'],
	['/data/app/app.lawnchair-DuYa-lXz12VIogYPfTOQUQ==/base.apk', 'app.lawnchair', 'Lawnchair'],
	['/data/app/com.farplace.qingzhuo-TAo7dUkkCG9LKb2xqGrI6g==/base.apk', 'com.farplace.qingzhuo', '清浊'],
	['/data/app/com.tencent.mobileqq-X4_bLi0A_c0gSWpLlbjNzg==/base.apk', 'com.tencent.mobileqq', 'QQ'],
	['/data/app/com.bilibili.studio-XcdviRUOB4PQEKl0T1QtQw==/base.apk', 'com.bilibili.studio', '必剪'],
	['/data/app/com.spotify.music-kMU6Ra1SJiv_qXCAz51zDQ==/base.apk', 'com.spotify.music', 'Spotify'],
	['/data/app/com.zhihu.android-VteoO_rvSMbAhDtfWYV7oQ==/base.apk', 'com.zhihu.android', '知乎'],
	['/data/app/app.lawnchair.lawnicons-NgwqahGD1q_pty1FuxcDhg==/base.apk', 'app.lawnchair.lawnicons', 'cayicons---lawnchair自适应主题色图标包'],
	['/data/app/com.termux-2Gx0LDD9g1elA91ygOZbwA==/base.apk', 'com.termux', 'Termux'],
	['/data/app/com.One.WoodenLetter-gHCM_CHrnQ70KkTPX7qiQg==/base.apk', 'com.One.WoodenLetter', '一个木函'],
	['/data/app/io.github.forkmaintainers.iceraven-LCO2tfAJ57TlfU1znGV_Lw==/base.apk', 'io.github.forkmaintainers.iceraven', 'Iceraven'],
	['/data/app/tv.danmaku.bili--_I53XjL4MizFWV9tdhVIg==/base.apk', 'tv.danmaku.bili', '哔哩哔哩'],
	['/data/app/com.google.android.inputmethod.latin-5_ihwk50yZLBdwZXB5Bljw==/base.apk', 'com.google.android.inputmethod.latin', 'Gboard']
]
'''
