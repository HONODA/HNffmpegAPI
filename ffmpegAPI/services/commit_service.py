from ffmpegAPI.config.myconfig import myconfig
from ffmpegAPI.util.auth import auth
import time
from ffmpegAPI.dao.videodao import HnVideoDao
import sys

class commit_servies:
    def __init__(self):
        super().__init__()
    
    '''
        提交信息，确认合法性，并下载视频服务
    '''
    async def commit_url(self,url="",token="",end_timestamp = None):
        mauth = auth()
        if token == "" or mauth.user_auth(token) == False:
            return myconfig.AUTH_MESSAGE['AUTHERR']
        video_authmsg = await mauth.video_auth(url=url,end_timestamp=end_timestamp)
        if video_authmsg.state_code == 0:
            #TODO 否则下载该url下的视频并生成对应数据库数据 #如果url有误则退出
            pass
        else:#成功或者失败了
            if video_authmsg.state_code != 200:
                return video_authmsg
            #开始进行视频剪辑
            videodao = HnVideoDao()
            video = await videodao.get_video(url=url)
            if video.path != "":
                sys.argv[""]
    async def video_clip(self,source,target,start,end):
        pass
