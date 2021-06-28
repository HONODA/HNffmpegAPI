from channels.generic.websocket import AsyncWebsocketConsumer
from ffmpegAPI.services.commit_service import commit_servies

import json

class CommitAPI(AsyncWebsocketConsumer):

    
    userlist = []
    async def connect(self):
        print("已连接")
        await self.accept()
    async def disconnect(self,close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        recevie_msg = json.loads(text_data)
        #获取用户id
        #获取token
        #获取url
        #获取start_timestamp
        #获取end_timestamp
        commitservice = commit_servies()
        comitmsg = await commitservice.commit_url(url = recevie_msg["url"],token= recevie_msg["token"],
        end_timestamp = recevie_msg["end_timestamp"])
        commitstr = json.dumps(comitmsg)
        await self.send(commitstr)
        print(text_data)
        # print(bytes_data)
        #return super().receive(text_data=text_data, bytes_data=bytes_data)