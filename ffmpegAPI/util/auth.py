import requests
from ffmpegAPI.config.myconfig import myconfig
import requests
import you_get
import hashlib
from ffmpegAPI.dao.videodao import HnVideoDao

class auth:

    def __init__(self):
        super().__init__()

    '''
        用户登陆验证
    '''
    def user_auth(self,token=""):
        #外部API 默认接口使用http POST 参数为token，根据实际情况重写，暂时默认为 return True
        data = '{}token":{}{}'.format("{",token,"}")
        res = requests.post(myconfig.USER_AUTH_API,data=data)
        #TODO 获取userId
        if res.status_code == 1:
            return True
        else:
            return False
    '''
        视频合法性验证
    '''
    def video_auth(self,url=""):
        if url == "":
            return myconfig.AUTH_MESSAGE["VIDEOERR"]
        #TODO 视频时间合法性检查
        if self.video_time_auth() == "-1":
            return myconfig.AUTH_MESSAGE['TIMEERR']
        #数据库检查是否在本地存在视频
        if self.get_video(url) != "1":
            return myconfig.AUTH_MESSAGE['UNKNOWERR']
        return "1"
    '''
        查询后台是否存在视频
    '''
    def get_video(self,url=""):
        vdao = HnVideoDao()
        a = None
        try:
            a = vdao.get_video(url)
        except Exception as e:
            pass
        finally:
            pass
        return "1"
        #如果不存在则下载视频
    '''
        查询改视频的合法时间
    '''
    def video_time_auth(self,url ,end_timestamp):
        vdao = HnVideoDao()
        a = None
        try:
            a = vdao.get_video_end_timestamp(url)
        except Exception as e:
            pass
        finally:
            pass
        if a < end_timestamp:
            return "-1" 
        return "1"
    #下载视频功能
    def download(self,url=""):
        pass
        