
# 图像和办公文档处理
## 操作图像
### 计算机图像相关知识
1.颜色

色光三原色：红绿蓝（RGB）

|名称|RGB值|
|-|-|
|white|(255,255,255,255)|
|green|(0,255,0,255)|
|gray |(128,128,128,255)|
|black|(0,0,0,255)|
|red  |(255,0,0,255)|
|blue |(0,0,255,255)|
|yellow|(255,255,0,255)|
|purple|(128,0,128,255)|

2.像素

对于一个由数字序列表示的图像来说，最小的单位就是图像上单一颜色的小方格，这些小方块都有一个明确的位置和被分配的色彩数值，而这些一小方格的颜色和位置决定了该图像最终呈现出来的样子，它们是不可分割的单位，我们通常称之为像素（pixel）。每一个图像都包含了一定量的像素，这些像素决定图像在屏幕上所呈现的大小。



```python
'''用Pillow(Python图像处理库PIL发展而来)操作图像'''
from PIL import Image
image = Image.open('C:/Users/chris/desktop/背景2.png')
print(image.format, image.size, image.mode)    
image.show()
```

    PNG (1920, 1200) P
    


```python
'''裁剪图像'''
image = Image.open('C:/Users/chris/desktop/背景2.png')
rect = 80, 20, 310, 360
image.crop(rect).show()
```


```python
'''生成缩略图'''
image = Image.open('C:/Users/chris/desktop/背景2.png')
size = 128, 128
image.thumbnail(size)
image.show()
```


```python
'''缩放和黏贴图像'''
image1 = Image.open('C:/Users/chris/desktop/背景3.jpg')
image2 = Image.open('C:/Users/chris/desktop/背景2.png')
rect = 80, 20, 310, 360
NooneCare = image2.crop(rect)
width, height = NooneCare.size
image1.paste(NooneCare.resize((int(width / 1.5), int(height / 1.5))), (250, 250))
image1.show()
```


```python
'''旋转和翻转'''
image = Image.open('C:/Users/chris/desktop/背景2.png')
image.rotate(180).show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()
```


```python
'''操作像素'''
image = Image.open('C:/Users/chris/desktop/背景3.jpg')
for x in range(80, 210):
    for y in range(20, 160):
        image.putpixel((x, y), (128, 128, 128))
image.show()
```


```python
'''滤镜效果'''
from PIL import Image, ImageFilter
image = Image.open('C:/Users/chris/desktop/背景3.jpg')
image.filter(ImageFilter.CONTOUR).show()
```


```python
'''处理Excel电子表格'''
"""
创建Excel文件
"""
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

workbook = Workbook()
sheet = workbook.active
data = [
    [1001, '白元芳', '男', '13123456789'],
    [1002, '白洁', '女', '13233445566']
]
sheet.append(['学号', '姓名', '性别', '电话'])
for row in data:
    sheet.append(row)
tab = Table(displayName="Table1", ref="A1:E5")

tab.tableStyleInfo = TableStyleInfo(
    name="TableStyleMedium9", showFirstColumn=False,
    showLastColumn=False, showRowStripes=True, showColumnStripes=True)
sheet.add_table(tab)
workbook.save('C:/Users/chris/desktop/全班学生数据.xlsx')
```

    D:\Anaconda\lib\site-packages\openpyxl\worksheet\_writer.py:273: UserWarning: File may not be readable: column headings must be strings.
      warn("File may not be readable: column headings must be strings.")
    


```python
"""
读取Excel文件
"""
from openpyxl import load_workbook
from openpyxl import Workbook

workbook = load_workbook('C:/Users/chris/desktop/学生明细表.xlsx')
print(workbook.sheetnames)
sheet = workbook[workbook.sheetnames[0]]
print(sheet.title)
for row in range(2, 7):
    for col in range(65, 70):
        cell_index = chr(col) + str(row)
        print(sheet[cell_index].value, end='\t')
    print()
```

    ['工作表 1 - 学生信息明细表']
    工作表 1 - 学生信息明细表
    学号	姓名	性别	出生日期	联系电话	
    1001	骆昊	男	1980-11-28 00:00:00	13566778899	
    1002	王大锤	男	1990-02-02 00:00:00	13022334567	
    1003	白元芳	男	1987-03-15 00:00:00	13909125566	
    1004	白洁	女	1988-04-14 00:00:00	15811990987	
    


```python
"""
读取PDF文件
"""
from PyPDF2 import PdfFileReader
with open('C:/Users/chris/desktop/轮腿混合机器人机械腿动力学建模与驱动预估.pdf', 'rb') as f:
    reader = PdfFileReader(f, strict=False)
    print(reader.numPages)
    if reader.isEncrypted:
        reader.decrypt('')
    current_page = reader.getPage(5)
    print(current_page)
    print(current_page.extractText())
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-25-1871736a390b> in <module>
          2 读取PDF文件
          3 """
    ----> 4 from PyPDF2 import PdfFileReader
          5 with open('C:/Users/chris/desktop/轮腿混合机器人机械腿动力学建模与驱动预估.pdf', 'rb') as f:
          6     reader = PdfFileReader(f, strict=False)
    

    ModuleNotFoundError: No module named 'PyPDF2'



```python
"""
使用pillow操作图像
"""
from PIL import Image
img = Image.open('C:/Users/chris/desktop/背景3.jpg')
print(img.size)
print(img.format)
print(img.format_description)
img.save('C:/Users/chris/desktop/背景3.png')

img2 = Image.open('C:/Users/chris/desktop/背景3.png')
img3 = img2.crop((335, 435, 430, 615))
for x in range(4):
    for y in range(5):
        img2.paste(img3, (95 * y , 180 * x))
img2.resize((img.size[0] // 2, img.size[1] // 2))
img2.rotate(90)
img2.save('C:/Users/chris/desktop/背景3.png')
```

    (1400, 980)
    JPEG
    JPEG (ISO 10918)
    


```python
"""
读取Word文件
"""
from docx import Document
doc = Document('C:/Users/chris/desktop/用函数还是用复杂的表达式.docx')
print(len(doc.paragraphs))
print(doc.paragraphs[0].text)
# print(doc.paragraphs[1].runs[0].text)
content = []
for para in doc.paragraphs:
    content.append(para.text)
print(''.join(content))
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-27-6ac3971aa1d1> in <module>
          2 读取Word文件
          3 """
    ----> 4 from docx import Document
          5 doc = Document('C:/Users/chris/desktop/用函数还是用复杂的表达式.docx')
          6 print(len(doc.paragraphs))
    

    ModuleNotFoundError: No module named 'docx'

