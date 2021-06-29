from ffmpegAPI.models import Generatevideo
import datetime
from asgiref.sync import sync_to_async

class GenerateVideoDao:
    @sync_to_async
    def saveinfo(self,userId,finished,pushback,url,Iurl):
        a = Generatevideo(id=userId,userid=userId,finished=finished,pushback=pushback,url=url,iurl=Iurl,operadate = datetime.date.today())
        a.save()
    @sync_to_async
    def saveinfo2(self,info):
        info.save()
    
    @sync_to_async    
    def getinfo(self,userId):
        a = Generatevideo.objects.get(userid=userId)
        return a