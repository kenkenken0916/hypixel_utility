
import pyautogui
import keyboard
import time
from PIL import ImageGrab

'''
滑鼠位置: (861, 258)，顏色: RGB(166, 92, 177)

滑鼠位置: (789, 258)，顏色: RGB(138, 138, 138)
滑鼠位置: (1078, 475)，顏色: RGB(138, 138, 138)
滑鼠位置: (860, 476)，顏色: RGB(138, 138, 138)
滑鼠位置: (861, 331)，顏色: RGB(200, 123, 210)

(1078-789)/4=72.25
(475-256)/3=73.25
861-789=72
331-256=145
476-331=145 ::2

滑鼠位置: (998, 321)，顏色: RGB(58, 58, 58)
滑鼠位置: (1070, 394)，顏色: RGB(58, 58, 58)
滑鼠位置: (998, 322)，顏色: RGB(58, 58, 58) #72
global use 72.5
'''
def search_spot1():
    while True:
        time.sleep(0.3)


'''
滑鼠位置: (646, 260)，顏色: RGB(157, 115, 165)
滑鼠位置: (1222, 476)，顏色: RGB(157, 115, 165)
滑鼠位置: (1005, 257)，顏色: RGB(196, 54, 226) real click
滑鼠位置: (1077, 258)，顏色: RGB(177, 79, 195) 
1078-646=432
432/6=72
1222-646=576
576/8=72
1005-646=359
359/5=71.8
1077-1005=72

'''
def search_spot2():
    while True:
        time.sleep(0.3)
        