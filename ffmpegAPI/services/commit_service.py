from ffmpegAPI.config.myconfig import myconfig
from ffmpegAPI.util.auth import auth
import time
from ffmpegAPI.dao.videodao import HnVideoDao
from ffmpegAPI.util.threadpool import threadpool
from ffmpegAPI.util.util import util
import os
import subprocess
from ffmpegAPI.dao.generatevideodao import GenerateVideoDao
import json


class commit_servies:
    def __init__(self):
        self.SUBPROCESSNOTICE = None
        super().__init__()
        
    '''
        提交信息，确认合法性，并下载视频服务
    '''
    async def commit_url(self,userId="",url="",token="",start_timestamp = "",end_timestamp = ""):
        mauth = auth()
        if token == "" or mauth.user_auth(token) == False:
            return myconfig.AUTH_MESSAGE['AUTHERR']
        video_authmsg = await mauth.video_auth(url=url,end_timestamp=end_timestamp)
        if video_authmsg["state_code"] == 0:
            #TODO 否则下载该url下的视频并生成对应数据库数据 #如果url有误则退出
            pass
        else:#成功或者失败了
            if video_authmsg["state_code"] != 200:
                return video_authmsg
            #开始进行视频剪辑
            return await self.video_clip(userId,url,start_timestamp,end_timestamp)

    async def video_clip(self,userId,url,startstamp,endstamp):
            videodao = HnVideoDao()
            video = await videodao.get_video(url=url)
            if video.path != "":
                path = os.path.join(os.getcwd(),myconfig.VIDEO_PATH["dir"])
                cache_path = os.path.join(os.getcwd(),myconfig.VIDEO_PATH["dir"]+"\\cache")
                uidname = util.get_uuid()
                cmd = "ffmpeg -i {}\\{} -vcodec copy -acodec copy -ss {} -to {} {}\\{}.mp4".format(path,video.path,startstamp,endstamp,cache_path,uidname)
                #generateVideo 插入更新
                try:
                    generatevideodao = GenerateVideoDao()
                    await generatevideodao.saveinfo(int(userId),0,0,url,0)
                except Exception as e:
                    print(e)
                    #TODO 错误日志
                    return myconfig.SYS_MESSAGE["ERROR"]
                #视频剪辑
                # args = cmd.split()
                # p = subprocess.Popen(args)
                u = util()
                p = u.do_ffmpeg_transcode(cmd)
                if threadpool.THREADMAP.get(userId,"") == "":
                    userlist = []
                    threadpool.THREADMAP[userId] = userlist
                sub_msg = {"process":p,"url":url}#子线程信息
                threadpool.THREADMAP[userId].append(sub_msg)
                if self.SUBPROCESSNOTICE != None:
                    msg = json.dumps(myconfig.SYS_MESSAGE["CONTINUE"])
                    await self.SUBPROCESSNOTICE.send(msg)#子进程添加通知
                return await u.wait_after_do(p,userId)

                

