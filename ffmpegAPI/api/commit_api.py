from channels.generic.websocket import AsyncWebsocketConsumer

import json

class CommitAPI(AsyncWebsocketConsumer):

    async def connect(self):
        print("已连接")
        await self.accept()
    async def disconnect(self,close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):

        return super().receive(text_data=text_data, bytes_data=bytes_data)