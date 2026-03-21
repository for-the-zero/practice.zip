import maliang
from tkinter import filedialog
import os
import json
import pyperclip

root = maliang.Tk(title="FileMerge", size=(430, 210))
cv = maliang.Canvas(auto_zoom=True, keep_ratio="min", free_anchor=True)
cv.place(width=430, height=210)

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

selected_folder = ""

def generate_str():
    global output_method
    file2be_merged = []
    for root, dirs, files in os.walk(selected_folder):
        for name in files:
            fullpath = os.path.join(root, name)
            relativepath = os.path.relpath(fullpath, selected_folder)
            try:
                with open(fullpath, "r", encoding="utf-8") as f:
                    content = f.read()
                    file2be_merged.append((relativepath, content))
            except:
                print("Error: Cannot open file " + fullpath)
    output_str = ""
    if output_method.get() == 0:
        for file in file2be_merged:
            output_str += '==========filePath: ' + file[0] + '===========\n\n'
            output_str += file[1]
            output_str += '\n\n'
    elif output_method.get() == 1:
        output_json = []
        for file in file2be_merged:
            output_json.append({"filePath": file[0], "content": file[1]})
        output_str = json.dumps(output_json, indent=4)
    elif output_method.get() == 2:
        output_str = '<files>\n'
        for file in file2be_merged:
            output_str += f'<file filePath="{file[0]}">\n\n{file[1]}\n\n</file>\n\n'
        output_str += '</files>'
    else:
        print("Error: Invalid output method")
    return output_str

def select_path():
    global path_text
    global selected_folder
    global desktop_path
    folder_selected = filedialog.askdirectory(title="请选择文件夹", initialdir=desktop_path)
    folder_name = os.path.basename(folder_selected)
    path_text.set(folder_name)
    selected_folder = folder_selected
def export_file():
    global output_method
    if output_method.get() == 0:
        file_type = "文本文件"
        file_ext = ".txt"
    elif output_method.get() == 1:
        file_type = "JSON文件"
        file_ext = ".json"
    elif output_method.get() == 2:
        file_type = "XML文件"
        file_ext = ".xml"
    else:
        print("Error: Invalid output method")
        return
    merged_str = generate_str()
    save_path = file_path = filedialog.asksaveasfilename(
        title="保存文件",
        defaultextension=file_ext,
        filetypes=[(file_type, '*'+file_ext), ("所有文件", "*.*")],
        initialdir=desktop_path
    )
    if save_path:
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(merged_str)
def export_clipboard():
    merged_str = generate_str()
    pyperclip.copy(merged_str)

maliang.Button(cv, (20, 20), text="选择被合并的文件夹", command=select_path)
path_text = maliang.Text(cv, (230, 27), text="")
maliang.Text(cv, (20, 92), text="导出为")
output_method = maliang.SegmentedButton(cv, (90, 80), text=(".txt", ".json", ".xml"))
maliang.Button(cv, (20, 150), text="导出为文件", command=export_file)
maliang.Button(cv, (150, 150), text="导出到剪贴板", command=export_clipboard)

output_method.set(2)

root.center()
root.mainloop()