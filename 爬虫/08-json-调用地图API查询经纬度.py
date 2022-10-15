# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 19:02
# @Author  : sihao
# @File    : 08-json-调用地图API查询经纬度.py
# from urllib import parse
# import hashlib
#
# # -*- coding: utf-8 -*-
# # 第一行必须有，否则报中文字符非ascii码错误
# from urllib import parse
# import hashlib
#
# # 以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak
# queryStr = '/geocoder/v2/?address=百度大厦&output=json&ak=34yo6Ck9NuAcWHztI1sIjY8NswygVBIQ'
#
# # 对queryStr进行转码，safe内的保留字符不转换
# encodedStr = parse.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
#
# # 在最后直接追加上yoursk
# rawStr = encodedStr + 'WllmTq3L5qy7FGP4AhtZmpHVO6XD15Pd'
#
# # md5计算出的sn值7de5a22212ffaa9e326444c75a58f9a0
# # 最终合法请求url是http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak&sn=7de5a22212ffaa9e326444c75a58f9a0
# print(hashlib.md5(parse.quote_plus(rawStr).encode("utf-8")).hexdigest())
# url='http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=34yo6Ck9NuAcWHztI1sIjY8NswygVBIQ&sn=a60c558767a90e96eddfb578f0b49118'
#
# import requests
# import json
# import pprint
# # address=input("请输入地点：")
# # par={'address':address,'key':'7ec25a9c6716bb26f0d25e9fdfa012b8'}
# # url='http://restapi.amap.com/v3/geocode/geo'
# res=requests.get(url)
# json_data=json.loads(res.text)
# # geo=json_data['geocodes'][0]['location']
# # longitude=geo.splite(',')[0]
# # latitude=geo.splite(',')[1]
# # print(longitude,latitude)
# pprint.pprint(json_data)
import requests
import uuid

#将具体的地址 转为经纬度
def getcode(site,city):
    parameters = {'address': site,'city':city, 'key': '69cf34f89d36243f973fe86b2642d363'}
    base_url = 'https://restapi.amap.com/v3/geocode/geo'
    response = requests.get(url=base_url, params=parameters)
    info_site = response.json()
    return info_site['geocodes'][0]['location']
    # print(info_site['geocodes'][0]['location'])

#将经纬度 转化为 具体的地址
def lo_to_addr(location):
    parameters = {'location': location, 'key': '69cf34f89d36243f973fe86b2642d363'}
    base_url = 'https://restapi.amap.com/v3/geocode/regeo'
    response = requests.get(url=base_url, params=parameters)
    info_site = response.json()
    # return info_site
    return info_site['regeocode']['formatted_address']
    # print(info_site['regeocode']['formatted_address'])


if __name__ == '__main__':
    #具体的地址，在包含城市的情况下 city 可以为空
    address = input("请输入地址名：")
    #城市
    city = ''
    location = getcode(address,city)
    address_from_location = lo_to_addr(location)

    print('根据输入的地址获取到的经纬度为：',location)
    print('根据经纬度得到的地址为：',address_from_location)


'''
使用高德地图api批量将地址转换为经纬度
'''
#
# import requests
# import json
# import codecs
# from openpyxl import Workbook
#
# wb = Workbook()
# sheet = wb.active
# sheet.title = "qiang"
#
#
# def get_location(address, i):
#     print(i)
#     url = "http://restapi.amap.com/v3/geocode/geo"
#     data = {
#         'key': '69cf34f89d36243f973fe86b2642d363',  # 在高德地图开发者平台申请的key，需要替换为自己的key
#         'address': address
#     }
#     r = requests.post(url, data=data).json()
#     sheet["A{0}".format(i)].value = address.strip('\n')
#     print(r)
#     if r['status'] == '1':
#         if len(r['geocodes']) > 0:
#             GPS = r['geocodes'][0]['location']
#             sheet["B{0}".format(i)].value = '[' + GPS + ']'
#         else:
#             sheet["B{0}".format(i)].value = '[]'
#     else:
#         sheet["B{0}".format(i)].value = '未找到'
#     # 将地址信息替换为自己的文件，一行代表一个地址，根据需要也可以自定义分隔符
#
#
# f = codecs.open(r"地址信息.txt", "r", "utf-8")
# i = 0
# while True:
#     line = f.readline()
#     i = i + 1
#     if not line:
#         f.close()
#         wb.save(r"保存文件.xlsx")
#         break
#     get_location(line, i)
#
#
#
