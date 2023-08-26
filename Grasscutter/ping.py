import Grasscutter.Server as Server
import os

def ping():
   #windows only
   result = os.popen("ping "+ str(Server.GCServer.url()))
   res = result.read()
   min_time, max_time, avg_time = None, None, None
   for line in res.splitlines():
        if "最短" in line:
            min_time = int(line.split("=")[1].split("ms")[0].strip())
        elif "最长" in line:
            max_time = int(line.split("=")[1].split("ms")[0].strip())
   return [min_time,max_time]