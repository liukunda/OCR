# -*- coding: UTF-8 -*-  
from aip import AipOcr
import json  

""" 你的 APPID AK SK """
APP_ID = '11581347'
API_KEY = 'lA59Kw0LE0uuNLwaSkmbGr2M'
SECRET_KEY = 'yDAH4VwbOki6ByTc85cc1sj6wpM8lBjX'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('image00003.jpg')

# 定义参数变量  
options = { 
'detect_direction': 'true',  
'language_type': 'CHN_ENG',  
}  

""" 调用通用文字识别, 图片参数为本地图片 """
p = client.basicGeneral(image)
"""格式化 json p 的内容"""
js = json.dumps(p,sort_keys=True, indent=4, separators=(',', ':')).decode("unicode-escape")
#print(json.dumps(p).decode("unicode-escape")) 
print(js)
