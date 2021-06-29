from ffmpegAPI.config.myconfig import myconfig
from ffmpegAPI.util.auth import auth
from ffmpegAPI.util.util import util
from ffmpegAPI.util.threadpool import threadpool


class SearchService:
    def __init__(self):
        super().__init__()
    
    async def search_url(self,userId="",url="",token=""):
        #用户认证
        mauth = auth()
        if token == "" or mauth.user_auth(token) == False:
            return myconfig.AUTH_MESSAGE['AUTHERR']
        u = util()
        msglist = []
        if url == "":
            msglist = u.compute_progress_and_get_all_progress(userId)
        else:
            if threadpool.THREADMAP.get(userId,"") != "":
                processlist = threadpool.THREADMAP[userId]
                for i in processlist:
                    if i["url"] == url:
                        url , progress = self.compute_progress_and_send_progress(i)
                        a = {"url":url,"progress":progress}
                        msglist.append(a)
        msg = {"state_code":200,"data":msglist}
        return msg