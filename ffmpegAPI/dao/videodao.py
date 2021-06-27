from ffmpegAPI.models import HnVideo

class HnVideoDao:
    def get_video(self,url):
        return HnVideo.objects.get(url=url)
    def get_video_end_timestamp(self,url):
        return HnVideo.objects.get(url).endtime