#anonfiles in python
import anonfiles

def upload():
    file_list = []
    file_num = int(input('多少文件？\n'))
    file_num = range(file_num)
    for i in file_num:
        file_list.append(input("第{i}文件路径:"))
    anonfiles.upload(file_list)

#there is a bug!!!who can help me???
def download():
    file_list = []
    file_num = int(input('多少文件？\n'))
    file_num = range(file_num)
    for i in file_num:
        file_list.append(input("第{j}文件url:".format(j=i)))
    anonfiles.download(file_list,'./')

while True:
    ans = input("你的操作\n    1.上传\n    2.下载\n")
    if ans == '1':
        upload()
        break
    elif ans == '2':
        download()
        break
    else:
        print("你回复的是什么？\n\n\n")