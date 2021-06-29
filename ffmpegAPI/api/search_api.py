from channels.generic.websocket import AsyncWebsocketConsumer
import json
from ffmpegAPI.services.search_service import SearchService



class SearchAPI(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.accept()
    async def disconnect(self,close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        recevie_msg = json.loads(text_data)
        #获取用户id
        #获取token
        seachserivce = SearchService()
        msg = await seachserivce.search_url(userId = recevie_msg["userId"],url=recevie_msg["url"],token=recevie_msg["token"])
        msgstr = json.dumps(msg)
        await self.send(msgstr)
        print(text_data)
        return super().receive(text_data=text_data, bytes_data=bytes_data)