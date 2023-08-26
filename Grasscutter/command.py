import requests
import json
import Grasscutter.Server as Server

def command(command:str,muit_command:bool=False):
    url = "https://" + Server.GCServer.url() + ":" + str(Server.GCServer.port()) + "/opencommand/api"
    try:
        if(muit_command == True):
            commands = command.split("|")
            for i in commands:
                data = {"action":"command","data":str(i),"server":url,"token":str(Server.GCServer.console_token())}
                x = requests.post(url, json=data,verify=False)
            return("done!")
        else:
            data = {"action":"command","data":str(command),"server":url,"token":Server.GCServer.console_token()}
            x = requests.post(url, json=data,verify=False)
            print(json.loads(x.text))
            return(json.loads(x.text))["data"]

    except requests.Timeout as e:
        print(e)
        return "请求接口时发生异常，请稍后再试"