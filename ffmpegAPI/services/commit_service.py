from ffmpegAPI.config.myconfig import myconfig
from ffmpegAPI.util.auth import auth

class commit_servies:
    def __init__(self):
        super().__init__()
    def commit_url(url="",token=""):
        if token == "" or auth.user_auth(token) == False:
            return myconfig.AUTH_MESSAGE['401']
        if url == "":
            return myconfig.AUTH_MESSAGE['402']
        
    
    def download(url):
        pass