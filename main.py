## -*- coding: UTF-8 -*-  
from aip import AipOcr
import json  
import pdf_to_image

""" 你的 APPID AK SK """
APP_ID = '11581347'
API_KEY = 'lA59Kw0LE0uuNLwaSkmbGr2M'
SECRET_KEY = 'yDAH4VwbOki6ByTc85cc1sj6wpM8lBjX'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 定义参数变量  

options = { 
'detect_direction': 'true',  
'language_type': 'CHN_ENG',  
}  

image = get_file_content('arduino权威指南 第4页.png')


""" 调用通用文字识别, 图片参数为本地图片 """
p = client.basicGeneral(image)
#js = json.dumps(p,sort_keys=True, indent=4, separators=(',', ':')).decode("unicode-escape")
#print(json.dumps(p).decode("unicode-escape")) 
print()
#ff = open("1.json","w")
#ff.write(js)
#ff.close()
#查看返回类型
#print(type(p))
#返回了 字典 类型
#"words_result" 是识别的文字
n = p["words_result"]
a = p["words_result_num"]

s = ""
counter = 0
while counter < a:
    l = n[counter]
    s = s + ( l["words"] + "\n" )
    counter += 1

#s = n[0]
#print(s["words"])

print(s)
ff = open("文本","w")
ff.write(s)
ff.close()
