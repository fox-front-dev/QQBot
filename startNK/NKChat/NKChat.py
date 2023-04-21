import  uiautomator2 as u2
def Chat():
    d = u2.connect('65zdtgir6dcqpvkb')
    d(text="喊话").click(offset=(0.5, 0.5), timeout=5)
    imgbin = d.screenshot(format="raw")
    open('/Users/fox/project/python/QQbot服务/go-cqhttp/data/images/startChat.jpg', "wb").write(imgbin)