import json
import time


def NKOpen(ws,group_id,d):
    if d.info.get('screenOn')==False:
        # 亮屏幕
        time.sleep(2)
        d.screen_on()
        time.sleep(2)
        d.swipe_points([(452, 2046), (0, 375)], 0.05)  # 滑动屏幕
    else:
        d.swipe_points([(452,2046), (0,375)], 0.05)#滑动屏幕
    d.press("home")
    time.sleep(2)
    d(text="奶块").click(offset=(0.5, 0.5),timeout=5)
    time.sleep(10)
    d(text="登录").click(offset=(0.5, 0.5),timeout=5)


