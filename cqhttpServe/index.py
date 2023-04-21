import json
from startNK.NKChat import NKChat
from startNK.NKOpen import NKOpen
from  utils.utils import determineNumber
from startNK.NKStatus import NKStatus
import  uiautomator2 as u2
import websocket

D = u2.connect('65zdtgir6dcqpvkb')
def on_message(ws,message):
    messageObj = json.loads(message)
    if messageObj["post_type"] == "message" and determineNumber(messageObj["group_id"]):
      if messageObj["message"]=="test":
          senMsg = {
              "action": "send_group_msg",
              "params": {
                  "group_id": messageObj["group_id"],
                  "message": "[CQ:image,file=test.jpg]"
              }}
          ws.send(json.dumps(senMsg))
      elif messageObj["message"]=="打开奶块":
          # 执行打开游戏（配合连点器）
          NKOpen.NKOpen(ws,messageObj["group_id"],D)
      elif messageObj["message"]=="查看状态":
          # 查看当前的奶块所处页面
          NKStatus.selectStatus(ws,messageObj["group_id"],D)
    else:
        print()


def on_error(ws, error):
    print("error")


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    ws.send("Hello, Server!")


def startServe():
    websocket.enableTrace(True)

    ws = websocket.WebSocketApp("ws://127.0.0.1:40002",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
