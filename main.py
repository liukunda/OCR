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

# 定义参数变量  

options = { 
'detect_direction': 'true',  
'language_type': 'CHN_ENG',  
}  

image = get_file_content('image00003.jpg')


""" 调用通用文字识别, 图片参数为本地图片 """
p = client.basicGeneral(image)
print(json.dumps(p).decode("unicode-escape")) 