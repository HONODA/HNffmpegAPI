from ffmpegAPI.config.myconfig import myconfig
from ffmpegAPI.util.auth import auth

import time

class commit_servies:
    def __init__(self):
        super().__init__()
    
    #获取url并且判断合法性
    def commit_url(self,url="",token="",end_stamp = None):
        if token == "" or auth.user_auth(token) == False:
            return myconfig.AUTH_MESSAGE['AUTHERR']
        video_authmsg = auth.video_auth(url=url,end_stamp = end_stamp)
        if  video_authmsg != "1":
            return video_authmsg
        
        #否则下载该url下的视频并生成对应数据库数据
        #如果url有误则退出