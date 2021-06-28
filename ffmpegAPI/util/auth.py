import requests
from ffmpegAPI.config.myconfig import myconfig
import requests
import you_get
import hashlib
from ffmpegAPI.dao.videodao import HnVideoDao
from django.core.exceptions import ObjectDoesNotExist

class auth:

    def __init__(self):
        super().__init__()

    '''
        用户登陆验证
    '''
    def user_auth(self,token="",userId=""):
        #外部API 默认接口使用http POST 参数为token，根据实际情况重写，暂时默认为 return True
        data = '{}"token":"{}","userId":"{}"{}'.format("{",token,userId,"}")
        #post 格式 {"token":""."userId":""}
        host = myconfig.USER_AUTH_API["host"]
        closed = myconfig.USER_AUTH_API["closed"]
        if closed == True:
            return True
    
        res = requests.post(host,data=data)
        #获取userId
        if res.status_code == 1:
            return True
        else:
            return False
    '''
        视频合法性验证
    '''
    async def video_auth(self,url="",end_timestamp=""):
        if url == "":
            return myconfig.AUTH_MESSAGE["VIDEOERR"]
        #数据库检查是否在本地存在视频
        exist_auth = self.get_video(url)
        #本地找不到视频
        if exist_auth == "0":
            return myconfig.AUTH_MESSAGE["VIDEONOTFOUND"]
        if exist_auth == "-1":
            return myconfig.AUTH_MESSAGE['UNKNOWERR']
        #视频时间合法性检查
        time_auth = self.video_time_auth(url=url,end_timestamp=end_timestamp)
        if time_auth == "-1":
            return myconfig.AUTH_MESSAGE['TIMEERR']

        return myconfig.AUTH_MESSAGE['SUCCESS']
    '''
        查询后台是否存在视频
    '''
    def get_video(self,url=""):
        vdao = HnVideoDao()
        a = None
        try:
            a = vdao.get_video(url)
        except ObjectDoesNotExist:
            return "0"  
        except Exception as e:
            #错误日志
            print(e)
            return "-1"
        return "1"
    '''
        查询改视频的合法时间
    '''
    async def video_time_auth(self,url ,end_timestamp):
        vdao = HnVideoDao()
        a = None
        try:
            a = await vdao.get_video_end_timestamp(url)
        except ObjectDoesNotExist:
            return "0"  
        except Exception as e:
            #错误日志
            print(e)
            return "-1" 
        if a.endtime < end_timestamp:
            return "-1" 
        return "1"
    #下载视频功能
    def download(self,url=""):
        pass
        