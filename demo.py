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


"""------------------------------------------------------------------"""

def run_Distinguish(filePath):#识别图片返回文字
    image = get_file_content(filePath)
    p = client.basicGeneral(image)
    #p返回的是 字典
    n = p["words_result"]
    #n 是 字典类型 所有识别的文字 
    a = p["words_result_num"]
    #a是有多少段

    s = ""
    counter = 0
    while counter < a:
        l = n[counter]
        s = s + (l["words"] + "\n")
        counter += 1
    return s

"""------------------------------------------------------------------"""

def wenbenxieru(filePath):
    ff = open("11", "a")
    ff.write(run_Distinguish(filePath))
    ff.close()


def run():
    pdf = "1.pdf"
    pdf_size = 607
    index = 0
    while index < pdf_size :
        wenbenxieru(pdf_to_image._run_convert(pdf, index))
        index += 1

run()

