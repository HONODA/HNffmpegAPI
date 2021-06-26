"""
配置类
"""
import json

class config:

    def read_user_auth():
        try:
            f = open('api.json')
            return json.load(f)[0]["data"]
        except BaseException as e:
            print("无法读取json文件。")
            print(e)
        return None
    def read_auth_message():
        try:
            f = open('api.json')
            return json.load(f)[1]["data"]
        except BaseException as e:
            print("无法读取json文件。")
            print(e)
        return None

    #用户验证外部api配置
    USER_AUTH_API = read_user_auth()
    #验证返回信息
    AUTH_MESSAGE = read_auth_message()
    


