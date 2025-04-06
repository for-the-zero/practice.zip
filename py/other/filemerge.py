print('File Merge')
print('==========')
print('请在同目录下创建一个files2merge文件夹，并将需要合并的文件放入该文件夹中')
input('完成后，请按回车键继续')
print('====================')

import os
files_2_be_merged = []
for root, dirs, files in os.walk('files2merge'):
    for name in files:
        fullpath = os.path.join(root, name)
        relativepath = os.path.relpath(fullpath, 'files2merge')
        try:
            with open(fullpath, 'r', encoding='utf-8') as f:
                content = f.read()
                files_2_be_merged.append((relativepath, content))
        except:
            print('文件{}打开失败'.format(fullpath))

#print(files_2_be_merged)
print('===================')

print('请选择文件格式：xml / json / txt （输入小写）')
format = input('> ')
contents = ''
if format == 'xml':
    for file in files_2_be_merged:
        contents += '<file filename="{}">\n{}\n</file>\n'.format(file[0], file[1])
elif format == 'json':
    import json
    json_content = []
    for file in files_2_be_merged:
        json_content.append({'filename': file[0], 'content': file[1]})
    contents = json.dumps(json_content, indent=4, ensure_ascii=False)
elif format == 'txt':
    for file in files_2_be_merged:
        contents += '==========filename: ' + file[0] + '===========\n'
        contents += file[1] + '\n'
else:
    print('你输入的是啥玩意啊')
    exit()

with open('merged_files.' + format, 'w', encoding='utf-8') as f:
    f.write(contents)
print('合并完成，文件名为merged_files.' + format)