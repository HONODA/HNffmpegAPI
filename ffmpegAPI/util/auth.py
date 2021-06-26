import requests

from ffmpegAPI.config import myconfig
import requests

class auth:

    def __init__(self):
        super().__init__()

    '''
        用户登陆验证
    '''
    def user_auth(token):
        data = '{"token":{}}'.format(token)
        res = requests.post(myconfig.USER_AUTH_API,data=data)
        if res.status_code == 1:
            return True
        else:
            return False
