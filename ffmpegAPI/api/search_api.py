from channels.generic.websocket import WebsocketConsumer
import json

class SearchAPI(WebsocketConsumer):
    
    def connect(self):
        self.accept()
    def disconnect(self,close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        
        return super().receive(text_data=text_data, bytes_data=bytes_data)