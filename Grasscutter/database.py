from pymongo import MongoClient
from bson.objectid import ObjectId  # 用于创建和处理 MongoDB 的 ObjectId

# 创建MongoDB连接
client = MongoClient('localhost', 27017)

# 选择数据库grasscutter
db = client['grasscutter']

class player():
    class nickname():
        def get(uid:int):
            collection = db['players']
            # 要查询的文档的 id
            results = collection.find({"_id": uid})
            rlist = list(results)
            status = 0
            for result in rlist:
                nickname = result['nickname']
                return(str(nickname))
        def change(uid:int,change:str):
            collection = db['players']
            condition = {"_id":uid}
            player = collection.find_one(condition)
            player["nickname"] = change
            collection.update_one(condition,{"$set":player})
            return(1)
        
    class avatars():
        def have(uid:int,_avatar_id:int):
        # 选择数据库中的集合（即表）avatars
            collection = db['avatars']
            # 要查询的文档的 id
            results = collection.find({"ownerId": uid})
            rlist = list(results)
            status = 0
            for result in rlist:
                avatar_id = result['avatarId']
                if(avatar_id == _avatar_id):
                    status = 1
            return status#返回值0-没有这个角色 1-有这个角色

        def delete(uid:int,_avatar_id:int):
        # 选择数据库中的集合（即表）avatars
            collection = db['avatars']
            # 要查询的文档的 id
            results = collection.find({"ownerId": uid})
            rlist = list(results)
            status = 0
            for result in rlist:
                avatar_id = result['avatarId']
                if(avatar_id == _avatar_id):
                    collection.delete_one({"_id": result['_id']})
                    status = 1
            return status #返回值0-没有这个角色 1-成功删除这个角色
