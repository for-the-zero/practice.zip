import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.font_registry():
	with dpg.font("SourceHanSansSC-normal.otf", 20) as font1:
		dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
		dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)
		dpg.add_font_range_hint(dpg.mvFontRangeHint_Korean)
		dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)

def callback(sender, app_data):
	print('OK was clicked.')
	print("Sender: ", sender)
	print("App Data: ", app_data)


dpg.add_file_dialog(
	directory_selector=True, show=False, callback=callback, tag="file_dialog_id", width=400 ,height=300)

with dpg.window(label="apkget", tag="Primary Window"):
	dpg.add_text("快速保存手机中的apk")
	dpg.add_button(label="导出目录", callback=lambda: dpg.show_item("file_dialog_id"))



	
dpg.bind_font(font1)
dpg.show_font_manager()

dpg.create_viewport(title='APKGET', width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()