from config.myconfig import myconfig
from util.auth import auth
import json

if __name__ == '__main__':
    #测试myconfig
    auth_message = myconfig.AUTH_MESSAGE
    print(auth_message['200'])
    #测试auth
    #user_auth = auth()
    #user_auth.user_auth("")
    #print(data)
    