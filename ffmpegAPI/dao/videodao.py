from ffmpegAPI.models import HnVideo
from asgiref.sync import sync_to_async


class HnVideoDao:
    @sync_to_async
    def get_video(self,url):
        return HnVideo.objects.get(url=url)
    @sync_to_async
    def get_video_end_timestamp(self,url):
        value = HnVideo.objects.get(url=url)
        return value
    