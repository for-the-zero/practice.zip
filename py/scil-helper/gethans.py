# https://studycli.org/zh-CN/chinese-characters/the-100-most-common-chinese-characters/

from lxml import etree

# 读取保存的HTML文件
filename = "./page.html"
with open(filename, "r", encoding="utf-8") as file:
    html_content = file.read()

# 使用lxml解析HTML内容
tree = etree.HTML(html_content)

# 使用XPath选择器获取列表中的所有行
rows = tree.xpath('/html/body/section[1]/div/div/div[1]/div[1]/div[2]/table/tbody/tr')

# 创建一个空列表来存储第二项数据
data = []

# 遍历每一行，将第二项数据添加到列表中
for row in rows:
    cells = row.xpath('.//td')
    if len(cells) >= 2:
        data.append(cells[1].text.strip())

# 将数据写入到txt文件
output_filename = "output.txt"
with open(output_filename, "w", encoding="utf-8") as file:
    file.write('\n'.join(data))

print(f"数据已成功导出到 {output_filename} 文件。")
