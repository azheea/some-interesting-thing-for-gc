from Grasscutter.command import *
from Grasscutter.database import *
from color import *
from designatiom import *

#职业使用方法 professions字典的键为职业名称,值是一个列表例如[a,b,c],第一个值a的意思是它是第几个职业(不是键的位置!!!),b是指角色的id,c是角色的长id.此外需要在designatiom.py中填写称号
professions = {"伐木工":[1,"10000057","1057"],"厨子":[2,"10000023","1023"],"奶妈":[3,"10000054","1054"],"增益师":[4,"10000047","1047"],"护盾":[5,"10000030","1030"],"输出":[6,"10000049","1049"]}


def professions_choose(uid:int,major:str):
    if(int(player.avatars.have(uid, int(professions[major][1]))) == 0):#检测是否已有此角色，防止诈骗
        #移除所有非当前职业的角色与命星
        for profession in professions.values():
            if profession[1] != major:
                player.avatars.delete(uid, int(profession[1]))
                #command("clear @"+str(uid)+" "+str(int(profession[1])+100),False)#好像命星不能用/clear删除
        # command("clear @"+str(uid)+str(int(professions[major][2])+10),False)#同理
        command("kick @"+str(uid),False)
        designation_change(uid,"major",int(professions[major][0]))
        command("sendMail "+str(uid)+"|sendMail 您已获得职业！ |sendMail <color=#8cb6f6>恭</color><color=#8db0f7>喜</color><color=#8fa9f8>你</color><color=#90a3f9>获</color><color=#919cfa>得</color><color=#9396fb>职</color><color=#9490fb>业</color><color=#9589fc>[</color>"+str(major)+"<color=#9683fd>]</color><color=#987cfe>!</color> |sendMail System |sendMail "+professions[major][2] +" 1 1 |sendMail finish",True)

            
    else:
        command("sendMail " + str(uid) + " |sendMail <color=red>警告</color> |sendMail <color=red>请勿重复选择相同角色！你的行为已被标记！</color> |sendMail System |sendMail finish ",True)