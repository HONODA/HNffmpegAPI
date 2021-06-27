import requests
from config.myconfig import myconfig
import requests
import you_get
import hashlib


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
        if res.status_code == 1:
            return True
        else:
            return False
    def video_auth(self,url=""):
        if url == "":
            return False
        #根据url查询数据库是否存在该数据。如果存在则直接在对应文件夹下进行视频剪辑
        #否则下载该url下的视频并生成对应数据库数据


    def get_video(self,url=""):
        pass
        #如果不存在则下载视频
    def download(self,url=""):
        pass
        