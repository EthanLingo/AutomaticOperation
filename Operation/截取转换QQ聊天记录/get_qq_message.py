"""
分享源：结衣机械召唤师。
這個功能是模擬滑鼠點擊來實現的，你得自己測一下QQ窗口、聊天框的座標
"""

import copy
import pyautogui
import pyperclip
import re
import time


class YuiQq:
    def __init__(self):
        self.sub = ''
        self.qq_num = ''
        self.title = ''
        self.date = ''
        self.time = ''
        self.word = []

    def show(self):
        print('{')
        print('  主體：', self.sub)
        print('  id：', self.qq_num)
        print('  頭銜：', self.title)
        if self.date:
            print('  日期：', self.date)
        print('  時間：', self.time)
        print('  發言：')
        for w in self.word:
            print('     ' + w)
        print('}')


def get_qqsub(item, is_title=1):
    r = YuiQq()
    while 1:
        if is_title:  # 檢測頭銜
            f = re.search('【.*】', item)
            if f is None:
                r = ''
                break
            else:
                r.title = f.group()
                item = item.lstrip(f.group())

        f = re.search('\(\d+\)', item)  # 檢測QQ號
        if f is None:
            f = re.search('<.*\.com>', item)
            if f is None:
                r = ''
                break
            else:
                r.qq_num = f.group()
                id_start = f.span()[0]
                id_end = f.span()[1]
                r.sub = item[:id_start]
                item = item[id_end:]
        else:
            r.qq_num = f.group()
            id_start = f.span()[0]
            id_end = f.span()[1]
            r.sub = item[:id_start]
            item = item[id_end:]

        f = re.search('\d+/\d\d/\d\d', item)
        if f is None:
            r.date = ''
            pass
        else:
            r.date = f.group()
            date_end = f.span()[1]
            item = item[date_end:]

        f = re.search('\d+:\d\d:\d\d', item)
        if f is None:
            pass
        else:
            r.time = f.group()
        break
    return r


def qq_analyze(text):
    text = re.split('\r\n', text)
    discourse = []
    for item in text:
        is_sub = get_qqsub(item)
        if is_sub:
            discourse.append(is_sub)
        elif not discourse:
            pass
        else:
            while item.startswith(' '):
                item = item.lstrip(' ')
            while item.endswith(' '):
                item = item.rstrip(' ')
            if item:
                discourse[-1].word.append(item)
    return discourse


def yui_read_qq():
    pyautogui.click(572, 1058)  # 點擊對話圖標
    pyautogui.click(684, 952)  # 選擇賬號
    pyautogui.click(610, 220)  # 選擇群
    pyautogui.click(1265, 481)  # 選擇聊天窗口

    pyautogui.hotkey('ctrl', 'a')  # 全選
    pyautogui.hotkey('ctrl', 'c')  # 複製
    text = pyperclip.paste()
    discourse = qq_analyze(text)
    #for d in discourse:
     #   d.show()
    return discourse


dis_old = []
while 1:
    dis_new = yui_read_qq()
    if not dis_old:
        dis_old = copy.deepcopy(dis_new)
    elif not dis_new:
        pass
    else:
        t_old = dis_old[-1].time
        t_new = dis_new[-1].time
        if t_new != t_old:  # 有新發言
            start = False
            for d in dis_new:
                t = d.time
                if start:
                    print(d.sub + '說：')
                    for w in d.word:
                        print('  ' + w)
                if t == t_old:
                    start = True
            dis_old = copy.deepcopy(dis_new)
    time.sleep(5)