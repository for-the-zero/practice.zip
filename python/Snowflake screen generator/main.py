
# import
import dearpygui.dearpygui as dpg
import json
import core

core = core.core


dpg.create_context()


# lang
lang = 0
def setup_lang():
	global lang
	temp_var_langchoose_bool = True
	while temp_var_langchoose_bool:
		lang = input('zh_cn[c] / en_us[e] : ')
		if lang == 'c' or lang == 'C':
			lang = 'cn'
			temp_var_langchoose_bool = False
		elif lang == 'e' or lang == 'E':
			lang = 'en'
			temp_var_langchoose_bool = False
		else:
			...
		#print(lang)
	with open(f'./{lang}.txt','r',encoding='utf-8') as lang:
		lang = json.loads(lang.read())
		#print(lang)
		#print(type(lang))
		#print(lang.keys())
def get_lang(keyword):
	global lang
	return lang["text"][keyword]
setup_lang()

# dpg
with dpg.font_registry():
	#font = dpg.add_font("xxx.otf", 20)
	if lang["lang"] == 'cn':
		with dpg.font("cn.otf", 20) as load_font:
			dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
			dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
	else:
		load_font = dpg.add_font("en.ttf", 20)
	font = load_font
#dpg.show_font_manager()

'''
def test():
	print(dpg.get_value("x_size"))
	print(dpg.get_value("y_size"))
'''


def gen():
	global core
	size = (int(dpg.get_value("x_size")),int(dpg.get_value("y_size")))
	dpg.configure_item("waitingwindow", show=True)
	core.generate(size)
	dpg.configure_item("waitingwindow", show=False)
	#print(core.get_data())
	dpg.configure_item("mainwindow",show=False)
	with dpg.texture_registry(show=True,label=get_lang("texturewindow_view")):
		dpg.add_static_texture(width=size[0], height=size[1], default_value=core.get_data(), tag="texture")
	

with dpg.window(label=get_lang('waitingwindow_title'), modal=True, show=False,tag="waitingwindow",no_close=True):
	dpg.add_text(get_lang("waitingwindow_text"))


with dpg.window(label=get_lang('mainwindow_title'),no_close=True,tag="mainwindow"):
	
	with dpg.group(tag="start_group"):
		dpg.add_input_text(label="x",tag="x_size")
		dpg.add_input_text(label="y",tag="y_size")
		dpg.add_button(label=get_lang("mainwindow_generate"),callback=gen,tag="button",enabled=True)
	

	dpg.bind_font(font)



dpg.create_viewport(title='ramdom Print', width=1000, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
