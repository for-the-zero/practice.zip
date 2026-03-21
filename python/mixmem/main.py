import flet as ft
import random



f = open('s.txt','r',encoding='utf-8')
fl = f.readlines()
f.close()

def ui(page: ft.page):
	page.fonts = {'s': './SourceHanSansSC-Regular.otf'}
	page.scroll = "always"

	def gen(e):
		global fl
		ret = []
		for i in range(int(ra.value)):
			status = True
			while status:
				temp = random.randint(1, len(fl))
				if modes.value == '5c':
					if len(list(fl[temp])) == 7:
						status = False
				elif modes.value == '7c':
					if len(list(fl[temp])) == 9:
						status = False
				else:
					status = False
			ret.append(fl[temp])

		retstr = ""
		for i in ret:
			retstr = retstr + i + '\n'

		res.value = retstr
		#res.value = 'hello'
		page.update()

	t1 = ft.Text("mixmem", style=ft.TextThemeStyle.TITLE_LARGE, font_family="s")
	t2 = ft.Text('我的记忆——混乱了~', style=ft.TextThemeStyle.LABEL_LARGE, font_family="s")

	modes = ft.RadioGroup(
		content=ft.Column(
			[
				ft.Radio(value="5c", label="5"),
				ft.Radio(value="7c", label="7"),
				ft.Radio(value="ac", label="any")
			]
		)
	)

	b = ft.ElevatedButton("Come On!", on_click=gen, data=0)
	ra = ft.Slider(min=1, max=100, divisions=100, label="{value}time(s)")
	res = ft.Text(font_family="s",selectable=True)
	page.add(t1,t2,modes,ra,b,res)

ft.app(target=ui, assets_dir=".")