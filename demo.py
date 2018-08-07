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


def _run_Distinguish(filePath):
    image = get_file_content(filePath)
    p = client.basicGeneral(image)
    n = p["words_result"]
    a = p["words_result_num"]

    s = ""
    counter = 0
    while counter < a:
        l = n[counter]
        s = s + (l["words"] + "\n")
        counter += 1
    
    return s





