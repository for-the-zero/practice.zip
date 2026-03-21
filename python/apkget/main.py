import flet as ft
from flet import Theme
import runadb

def main(page: ft.page):
	page.title = "APKGET"
	page.scroll = "always"



	page.fonts = {"SHS": "SourceHanSans-normal.otf", "2": "https://www.unpkg.com/font-online/fonts/SourceHanSans/SourceHanSans-Normal.otf"}
	page.theme = Theme(font_family="SHS")


	global output_dir
	output_dir = runadb.desktop_path()
	def picked_dir(e: ft.FilePickerResultEvent):
		if e.path: 
			global output_dir
			pick_dir_text.value = (e.path)
			output_dir = e.path
			pick_dir_text.update()
	pick_dir_dialog = ft.FilePicker(on_result=picked_dir)
	page.overlay.append(pick_dir_dialog)



	def update_list():
		#app_list.rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text("1")),ft.DataCell(ft.Text("2")),ft.DataCell(ft.Text("3")),]))
		#page.update()

		update_button.disabled = True
		update_button.text = "加载中，请勿执行其它操作"
		page.update()


		global output_dir
		def create_buttons(i):
			global output_dir
			return ft.DataCell(ft.ElevatedButton("导出",icon=ft.icons.DOWNLOAD, on_click=lambda _: runadb.push(i[0],output_dir,i[2])))

		adb_app_list = runadb.get_list()
		for i in adb_app_list:
			app_list.rows.append(ft.DataRow(cells=[
				create_buttons(i),
				ft.DataCell(ft.Text(i[2])),
				ft.DataCell(ft.Text(i[1]))
				]))
		update_button.disabled = False
		update_button.text = "刷新列表"
		page.update()



	page.controls.append(ft.Markdown("# 快速保存手机中的apk",extension_set=ft.MarkdownExtensionSet.GITHUB_WEB))
	pick_dir_text = ft.Text("未选择，默认为桌面")
	update_button = ft.ElevatedButton("刷新列表",icon=ft.icons.REFRESH, on_click=lambda _: update_list())
	page.controls.append(ft.Row([
		update_button,
		ft.ElevatedButton("更改导出路径",icon=ft.icons.FOLDER_OUTLINED,
			on_click=lambda _: pick_dir_dialog.get_directory_path(),),
		pick_dir_text,])
		)

	'''
	app_list = ft.DataTable(
		columns=[ft.DataColumn(ft.Text("操作")),ft.DataColumn(ft.Text("应用名")),ft.DataColumn(ft.Text("包名"))],
		rows=[ft.DataRow(cells=[ft.DataCell(ft.Text("1")),ft.DataCell(ft.Text("2")),ft.DataCell(ft.Text("3")),])]
		)
	'''
	app_list = ft.DataTable(
		columns=[ft.DataColumn(ft.Text("操作")),ft.DataColumn(ft.Text("应用名")),ft.DataColumn(ft.Text("包名"))],
		rows=[],

		border=ft.border.all(2, "grey"),
		border_radius=10,
		horizontal_lines=ft.border.BorderSide(1, "grey"),
		)
	page.controls.append(app_list)
	
	
	page.update()




ft.app(target=main)