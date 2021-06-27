# from config.myconfig import myconfig
# from util.auth import auth
# import json
#from models import HnVideo

import asyncio
import websockets

    
# 向服务器端发送认证后的消息
async def send_msg(websocket):
    while True:
        _text = input("please enter your context: ")
        if _text == "exit":
            print(f'you have enter "exit", goodbye')
            await websocket.close(reason="user exit")
            return False
        await websocket.send(_text)
        # if websocket.close_code != None:
        # await websocket.close(reason="user exit")
        recv_text = await websocket.recv()
        print(f"{recv_text}")

# 客户端主逻辑
async def main_logic():
    async with websockets.connect('ws://localhost:8000/commit/') as websocket:
        #await auth_system(websocket)
        
        await send_msg(websocket)

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

    print("开始测试")
    asyncio.get_event_loop().run_until_complete(main_logic())
    #"{"userId":"","token":"","url":"","start_timestamp":"","end_timestamp":""}"
    pass