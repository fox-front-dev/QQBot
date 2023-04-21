import json
import time


def selectStatus(ws,group_id,d):
    d.screen_on()
    time.sleep(1)
    imgbin = d.screenshot(format="raw")
    open('/Users/fox/project/python/QQbot服务/go-cqhttp/data/images/PhoneStatus.jpg', "wb").write(imgbin)
    senMsg = {
        "action": "send_group_msg",
        "params": {
            "group_id": group_id,
            "message": "[CQ:image,file=PhoneStatus.jpg]"
        }}
    ws.send(json.dumps(senMsg))