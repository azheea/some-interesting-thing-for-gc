import requests
import json
from Grasscutter.command import command


def trade(player_uid_from:int,player_uid_to:int,item_id:int,item_trade_count:int):
    # item_id = int(100002)
    # item_trade_count = int(2)
    # player_uid_from = 10003
    # player_uid_to = 10003

    print("cheaking itme...")
    command("say 正在进行检测",False)
    clear = command("clear " + "@"+str(player_uid_from) +" " + str(item_id) + " x " + str(item_trade_count),False)
    if ("done!" in clear or "已清除" in clear):
        command("give "  + str(item_id) + " x" + str(item_trade_count)+ " @" + str(player_uid_to),False)
        command("say <color=green>成功!</color>",True)
        command("sendMail " + str(player_uid_to) +"|sendMail 交易已经完成! |sendMail 您的交易已经完成! |sendMail System |sendMail 101 1 1 |sendMail finish",True)
        command("sendMail " + str(player_uid_from) +"|sendMail 交易已经完成! |sendMail 您发起的交易已经完成! |sendMail System |sendMail 101 1 1 |sendMail finish",True)
    else:
          command("sendMail "+str(player_uid_from)+"|sendMail 交易失败！ |sendMail <color=red>交易失败！您没有足够的物品进行交易</color> |sendMail System |sendMail finish",True)


item_id = int(input("需要交易的物品id:"))
item_trade_count = int(input("请输入要交易的数量"))
player_uid_from = input("请输入您的uid:")
player_uid_to = input("请输入您的交易对象的uid:")
trade(player_uid_from,player_uid_to,item_id,item_trade_count)