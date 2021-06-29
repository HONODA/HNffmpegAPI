"""
配置类
"""

import json
import os
class myconfig:
    
    def __init__(self):
        super().__init__()
    
    def read_user_auth():
        try:
            f = open(os.path.dirname(os.path.abspath(__file__)) +'\\api.json','r',encoding='utf-8')
            print("reading")
            return json.load(f)[0]["data"]

        except BaseException as e:
            print("无法读取json文件:{}",e)

        return None
    def read_auth_message():
        try:
            f = open(os.path.dirname(os.path.abspath(__file__)) +'\\api.json','r',encoding='utf-8')
            return json.load(f)[1]["data"]
        except BaseException as e:
            print("无法读取json文件:{}",e)
            
        return None
    def read_video_path():
        try:
            f = open(os.path.dirname(os.path.abspath(__file__)) +'\\api.json','r',encoding='utf-8')
            return json.load(f)[2]["data"]
        except BaseException as e:
            print("无法读取json文件:{}",e)
            
        return None
    def read_message_path():
        try:
            f = open(os.path.dirname(os.path.abspath(__file__)) +'\\api.json','r',encoding='utf-8')
            return json.load(f)[3]["data"]
        except BaseException as e:
            print("无法读取json文件:{}",e)
        
        return None

    #用户验证外部api配置
    USER_AUTH_API = read_user_auth()
    #验证返回信息
    AUTH_MESSAGE = read_auth_message()
    #视频存放位置
    VIDEO_PATH = read_video_path()
    #系统信息
    SYS_MESSAGE = read_message_path()

