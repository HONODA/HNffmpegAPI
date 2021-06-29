import uuid
import subprocess
import re
from asgiref.sync import sync_to_async
from ffmpegAPI.dao.generatevideodao import GenerateVideoDao
from ffmpegAPI.config.myconfig import myconfig
from ffmpegAPI.util.threadpool import threadpool
class util:

    def __init__(self):
        super().__init__()

    '''
        获取唯一码
    '''
    def get_uuid():
        return uuid.uuid1()

    '''
        秒数格式转换
    '''
    def get_seconds(time):
        h = int(time[0:2])
        m = int(time[3:5])
        s = int(time[6:8])
        ms = int(time[9:12])
        ts = (h * 60 * 60) + (m * 60) + s + (ms / 1000)
        return ts


    '''
        运行指令
    '''
    def do_ffmpeg_transcode(self,cmd):
        process = subprocess.Popen(cmd,stderr=subprocess.PIPE,bufsize=0,universal_newlines=True,shell=True)
        return process

    '''
        显示用户所有进度
    '''
    def compute_progress_and_get_all_progress(self,userId):
        msglist = []
        if threadpool.THREADMAP.get(userId,"") != "":
            processlist = threadpool.THREADMAP[userId]
            for i in processlist:
                url , progress = self.compute_progress_and_send_progress(i)
                a = {"url":url,"progress":progress}
                msglist.append(a)
        return msglist
    '''
        显示进度
    '''
    def compute_progress_and_send_progress(self,msg):
        duration = None
        process = msg["process"]
        while process.poll() is None:
            line = process.stderr.readline().strip()
            if line:
                duration_res = re.search(r'Duration: (?P<duration>\S+)', line)
                if duration_res is not None:
                    duration = duration_res.groupdict()['duration']
                    duration = re.sub(r',', '', duration)

                result = re.search(r'time=(?P<time>\S+)', line)
                if result is not None and duration is not None:
                    elapsed_time = result.groupdict()['time']

                    currentTime =  get_seconds(elapsed_time)
                    allTime = get_seconds(duration)

                    progress = currentTime * 100/allTime
                    return msg["url"],progress
    '''
        process执行后更新数据库,且退出threadmap
    '''
    async def wait_after_do(self,process,userId):
        while process.poll() is None:
            pass
        if process.poll() == 0:
            if userId != "":
                generdao = GenerateVideoDao()
                url = None
                value = None
                try:
                    value = await generdao.getinfo(userId = userId)
                    value.finished = 1
                    url = value.url
                    await generdao.saveinfo2(value)
                except Exception as e:
                    print(e)
                    #TODO 错误日志
                    return myconfig.SYS_MESSAGE["ERROR"]
                sub_msg = {"process":process,"url":url}#子线程信息
                threadpool.THREADMAP[userId].remove(sub_msg)
                return myconfig.SYS_MESSAGE["SUCCESS"]
        print(process.poll())
        print(process.returncode)
        return myconfig.SYS_MESSAGE["ERROR"]