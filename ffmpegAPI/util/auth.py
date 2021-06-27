import requests
from config.myconfig import myconfig
import requests

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
