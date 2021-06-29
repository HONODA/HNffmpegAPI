# from config.myconfig import myconfig
# from util.auth import auth
# import json
#from models import HnVideo

import asyncio
import websockets
import json
    
# 向服务器端发送url的消息
async def send_commit_msg(websocket):
   # while True:
        _text = '{"userId":"11","token":"11","url":"www.video.com","start_timestamp":"00:00:00","end_timestamp":"00:01:00"}'
        await websocket.send(_text)
        # if websocket.close_code != None:
        # await websocket.close(reason="user exit")
        recv_text = await websocket.recv()
        recv_json = json.loads(recv_text)
        if recv_json["state_code"] !=200 and recv_json["state_code"] !=100:
            await websocket.close(reason="user exit")
        if recv_json["state_code"] == 100:
            print(f"{recv_text}")
            recv_text = await websocket.recv()
            recv_json = json.loads(recv_text)
        print(f"{recv_text}")
        await websocket.close(reason="user exit")

# 向服务器端发送search查询的消息
async def send_search_msg(websocket):
   # while True:
        _text = '{"userId":"11","token":"11","url":"www.video.com"}'
        await websocket.send(_text)
        recv_text = await websocket.recv()
        recv_json = json.loads(recv_text)
        if recv_json["state_code"] !=200 and recv_json["state_code"] !=100:
            await websocket.close(reason="user exit")
        if recv_json["state_code"] == 100:
            print(f"{recv_text}")
            recv_text = await websocket.recv()
            recv_json = json.loads(recv_text)
        print(f"{recv_text}")
        await websocket.close(reason="user exit")
# 客户端主逻辑
async def main_logic():
    #用户url提交进行视频剪辑
    async with websockets.connect('ws://localhost:8000/commit/') as websocket:
        await send_commit_msg(websocket)
    #进行用户进度搜索
    async with websockets.connect('ws://localhost:8000/sp/') as websocket:
        await send_search_msg(websocket)
if __name__ == '__main__':
    #测试myconfig
    # auth_message = myconfig.AUTH_MESSAGE g
    # print(auth_message['AUTHERR'])
    #测试auth
    #user_auth = auth()
    #user_auth.user_auth("")
    #print(data)
    #测试数据库可用性
    #HnVideo.save()
    #HnVideo.objects.get(url="233")

    print("websocket开始测试")
    asyncio.get_event_loop().run_until_complete(main_logic())
    #commit/消息格式
    #{"userId":"11","token":"11","url":"www.video.com","start_timestamp":"00:00:00","end_timestamp":"00:01:00"}
    #search/消息格式
    #{"userId":"11","token":"11"}
    pass