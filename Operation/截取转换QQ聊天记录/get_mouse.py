"""
分享源：结衣机械召唤师。
這個代碼可以用來測量座標，打開之後用滑鼠點擊哪裡，就能顯示哪裡的座標
"""

import pynput.mouse as pm


def on_click(x, y, button, pressed):
    if pressed:
        xy = "{},{}".format(x, y)
        print('座標：',xy)


while 1:
    with pm.Listener(on_click=on_click) as listener:
        listener.join()