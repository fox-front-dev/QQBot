import json

import websocket


def on_message(ws, message):
        if json.loads(message)["post_type"] == "message":
            print(message)
        else:
            print()

def on_error(ws, error):
        print("error")


def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send("Hello, Server!")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:40002",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

