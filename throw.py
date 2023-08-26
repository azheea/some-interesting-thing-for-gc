import requests
import json
from Grasscutter.command import command

def throw(uid:int,item_id:int,item_throw_amount:int):
    print("cheaking itme...")
    command("say 正在进行检测",False)
    clear = command("clear " + "@"+str(uid) +" " + str(item_id) + " x " + str(item_throw_amount),False)
    if ("已清除" in clear):
        command("spawn " + "@" + str(uid) +" "+ str(item_id) + " x" + str(item_throw_amount),False)
    else:
        command("sendMail "+str(uid)+"|sendMail 投掷失败！ |sendMail <color=red>投掷失败！您没有足够的物品进行交易</color> |sendMail System |sendMail finish",True)

item_id = int(input("需要投掷的物品id:"))
item_throw_count = int(input("请输入要丢出的数量:"))
uid = input("uid:")

throw(uid,item_id,item_throw_count)