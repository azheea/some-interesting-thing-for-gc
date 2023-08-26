from Grasscutter.database import *
from color import *

designations = {"major":["","[光头强]","[大厨子]","[五星观赏鱼]","[快乐风男]","[岩王爷]","[长野原烟花店]"],"custom":["","[管理]","[赞助者]","[炉管王]"]}
colors = {"[管理]":[[77,147,230],[162,150,234]],"[赞助者]":[[252, 255, 134],[252, 255, 134]],"[炉管王]":[[254,150,154],[254,150,154]]}

def designation_change(uid:int,designation_type:str,index:int=0,delete:bool=True):
    player_name = player.nickname.get(uid)


    if(designation_type in designations and len(designations[designation_type])-1 >= index):
        major = designations[designation_type][index]

        for i in range(2):
            for major_designation in designations[designation_type]:
                colorful_designations = major_designation

                if designation_type == "major":
                    colorful_designations = color_change(major_designation,[254,150,154],[254,150,154])
                else:
                    colorful_designations = color_change(major_designation,colors[major][0],colors[major][1])
                    

                colorful_designations = colorful_designations
                if major_designation in player_name and delete == True:
                    player_name = player_name.replace("<i>","")
                    player_name = player_name.replace("</i>","")
                    player_name = player_name.replace(colorful_designations, "")

                if(major == major_designation and i==1):
                    end_name = "<i>" + colorful_designations+"</i>" + player_name
                    print("<i>" + colorful_designations+"</i>")
                    break

        # end_name = "<i>"+end_name+"</i>"
        player.nickname.change(uid,end_name)
        return(player.nickname.get(uid))

    else:
        return("Fail")

