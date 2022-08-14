#encoding=UTF-8

'''
这里是MisakaAE写的辣鸡脚本
bilibili@MisakaAE
https://space.bilibili.com/66767091

API接口主页  https://zy.xywlapi.cc/
q绑查手机  https://zy.xywlapi.cc/qqapi?qq=
手机查qq  https://zy.xywlapi.cc/qqphone?phone=
qq查lol  https://zy.xywlapi.cc/qqlol?qq=
lolid查qq  https://zy.xywlapi.cc/lolname?name=
qq老密查询  https://zy.xywlapi.cc/qqlm?qq=
微博id查手机  https://zy.xywlapi.cc/wbapi?id=
手机查微博id  https://zy.xywlapi.cc/wbphone?phone=
'''

from time import sleep
import requests
import os

#API
qqtoph = "https://zy.xywlapi.cc/qqapi?qq="
phtoqq = "https://zy.xywlapi.cc/qqphone?phone="
qqtolol = "https://zy.xywlapi.cc/qqlol?qq="
loltoqq = "https://zy.xywlapi.cc/lolname?name="
oldqm = "https://zy.xywlapi.cc/qqlm?qq="
wbtoph = "https://zy.xywlapi.cc/wbapi?id="
phtowb = "https://zy.xywlapi.cc/wbphone?phone="

os.system("color b")
os.system("cls")
while True:
    os.system("color b")
    print("MisakaAEの恶俗脚本\n")
    print("1.QQ查手机")
    print("2.手机查QQ")
    print("3.QQ查LOLid")
    print("4.LOLid查QQ")
    print("5.QQ老密查询")
    print("6.微博id查手机")
    print("7.手机查微博id")
    print("0.退出")
    questapi = input("请输入选项：")


    #Q绑查手机
    if questapi == "1" :
        #cmd命令行清屏
        os.system("cls")

        qq = input("请输入QQ：")
        full_qqtoph = qqtoph+qq
        #从API获得数据
        out_qqtoph = requests.get(full_qqtoph)
        #将获得的数据转换为字典
        dict_out_qqtoph = out_qqtoph.json()

        #判断状态码是否正常
        statuscode = dict_out_qqtoph['status']
        if statuscode == 200 :
            #从字典中筛选信息
            msg = dict_out_qqtoph['message']
            phone = dict_out_qqtoph['phone']
            area = dict_out_qqtoph['phonediqu']
        else :
            msg = "没有找到或输入错误"
            phone = "NULL"
            area = "NULL"

        #输出结果
        out = (f"状态：{msg}\nQQ号：{qq}\n手机号：{phone}\n号码归属地：{area}")


    #手机查Q绑
    elif questapi == "2" :
        os.system("cls")
        ph = input("请输入手机号：")
        full_phtoqq = phtoqq+ph
        out_phtoqq = requests.get(full_phtoqq)
        dict_out_phtoqq = out_phtoqq.json()

        statuscode = dict_out_phtoqq['status']
        if statuscode == 200 :
            msg = dict_out_phtoqq['message']
            area = dict_out_phtoqq['phonediqu']
            qq = dict_out_phtoqq['qq']
        else :
            msg = "没有找到或输入错误"
            area = "NULL"
            qq = "NULL"

        out = (f"状态：{msg}\nQQ号：{qq}\n手机号：{ph}\n号码归属地：{area}")


    elif questapi == "3" :
        os.system("cls")

        qq = input("请输入QQ：")
        full_qqtolol = qqtolol+qq
        out_qqtolol = requests.get(full_qqtolol)
        dict_out_qqtolol = out_qqtolol.json()

        statuscode = dict_out_qqtolol['status']
        if statuscode == 200 :
            msg = dict_out_qqtolol['message']
            lol = dict_out_qqtolol['name']
            daqu = dict_out_qqtolol['daqu']
        
        else :
            msg = "没有找到或输入错误"
            name = "NULL"
            daqu = "NULL"

        out = (f"状态：{msg}\nQQ号：{qq}\n名称：{lol}\n大区：{daqu}")


    elif questapi == "4" :
        os.system("cls")

        lol= input("请输入LOLid：")
        full_loltoqq = loltoqq+lol
        out_loltoqq = requests.get(full_loltoqq)
        dict_out_loltoqq = out_loltoqq.json()
        
        statuscode = dict_out_loltoqq['status']
        if statuscode == 200 :
            msg = dict_out_loltoqq['message']
            qq = dict_out_loltoqq['qq']
            daqu = dict_out_loltoqq['daqu']
        
        else :
            msg = "没有找到或输入错误"
            daqu = "NULL"
            qq = "NULL"

        out = (f"状态：{msg}\nQQ号：{qq}\n名称：{lol}\n大区{daqu}")


    elif questapi == "5" :
        os.system("cls")

        qq = input("请输入QQ：")
        full_qqlm = oldqm+qq
        out_qqlm = requests.get(full_qqlm)
        dict_qqlm  = out_qqlm.json()

        statuscode = dict_qqlm['status']
        if statuscode == 200 :
            msg = dict_qqlm['message']
            qqlm = dict_qqlm['qqlm']
        else :
            msg = "没有找到或输入错误"
            qqlm = "NULL"

        out = (f"状态：{msg}\nQQ：{qq}\nQQ老密：{qqlm}")


    elif questapi == "6" :
        os.system("cls")

        wb = input("请输入微博id：")
        full_wbtoph = wbtoph+wb
        out_wbtoph = requests.get(full_wbtoph)
        dict_wbtoph = out_wbtoph.json()

        statuscode = dict_wbtoph['status']
        if statuscode == 200 :
            msg = dict_wbtoph['message']
            ph = dict_wbtoph['phone']
            area = dict_wbtoph['phonediqu']

        else :
            msg = "没有找到或输入错误"
            ph = "NULL"
            area = "NULL"
        
        out = (f"状态：{msg}\n微博id:{wb}\n手机号：{ph}\n号码归属地：{area}")

    elif questapi == "7" :
        os.system("cls")

        ph = input("请输入手机号：")
        full_phtowb = phtowb+ph
        out_phtowb = requests.get(full_phtowb)
        dict_phtowb = out_phtowb.json()

        statuscode = dict_phtowb['status']
        if statuscode == 200 :
            msg = dict_phtowb['message']
            wb = dict_phtowb['id']
            area = dict_phtowb['phonediqu']

        else :
            msg = "没有找到或输入错误"
            wb = "NULL"
            area = "NULL"
        
        out = (f"状态：{msg}\n微博id:{wb}\n手机号：{ph}\n号码归属地：{area}")



    elif questapi == "0" :
        os.system("color f")
        print("\n\n--------已结束--------\n\n")
        exit()


    else :
        os.system("cls")
        print("你输了个什么玩意？\n")
        out = ("\n给你邦邦来两拳！\n")
    

    print("==================================================================")
    print(out)
    questapi2 = input("\n是否继续查询？(回车继续，输入 \"n\" 退出）")

    if questapi2 == "":
        os.system("cls")
        continue
    
    elif questapi2 == ("n")or("N"):
        os.system("color f")
        print("\n\n--------已结束--------\n\n")
        exit()

    else :
        print("未知指令  3秒后继续\n")
        sleep(3)
        os.system("cls")
        continue

if __name__ == "__main__":
    print("")