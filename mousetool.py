import pyautogui
import keyboard

import time
from PIL import ImageGrab






# 設定初始移動距離
distance_a = 1
distance_b = 2
current_distance = distance_a

def move_mouse(dx, dy):
    x, y = pyautogui.position()
    pyautogui.moveTo(dx,dy)

def print_position():
    x, y = pyautogui.position()
    print(f"Mouse Position: (x={x}, y={y})")

def switch_distance():
    global current_distance
    current_distance = distance_b if current_distance == distance_a else distance_a
    print(f"Switched distance to: {current_distance}")
    

def bzone():
    pyautogui.moveTo(664, 705)
    pyautogui.click()
    time.sleep(0.7)
    pyautogui.moveTo(1109, 359)
    pyautogui.click()
    time.sleep(0.7)
    pyautogui.moveTo(1168, 358)
    pyautogui.click()
    time.sleep(0.7)
    pyautogui.write("71680")
    time.sleep(0.7)
    pyautogui.moveTo(954, 908)
    pyautogui.click()
    time.sleep(0.7)
    pyautogui.moveTo(767, 363)
    pyautogui.click()
    time.sleep(0.7)
    pyautogui.moveTo(954, 358)
    pyautogui.click()



def get_mouse_pos_and_color():
    x, y = pyautogui.position()  # 取得滑鼠位置
    screen = ImageGrab.grab()   # 擷取整個螢幕
    color = screen.getpixel((x, y))  # 取得該位置顏色 (R,G,B)
    print(f"滑鼠位置: ({x}, {y})，顏色: RGB{color}")

def getcolor():
    # r,g,b = pyautogui.pixel(19, 705)  # 取得指定位置顏色 (R,G,B)
    # # print(f"指定位置顏色: RGB{leftcolor}")
    # if (r-79)*(r-79)+(g-79)*(g-79)+(b-79)*(b-79)<1000:
    #         print("leftget")
    
    # print(f"right顏色: RGB{r,g,b}") #54, 23, 17
    r ,g, b= pyautogui.pixel(1909, 766)  # 取得指定位置顏色 (R,G,B)
    # print(f"指定位置顏色: RGB{rightcolor}")
    if r>45 and g<45:
            print("rightget")
    print(f"左側顏色: RGB{r,g,b}")

# 綁定快捷鍵
keyboard.add_hotkey('m+up', lambda: move_mouse(0, -current_distance))
keyboard.add_hotkey('m+down', lambda: move_mouse(0, current_distance))
keyboard.add_hotkey('m+left', lambda: move_mouse(-current_distance, 0))
keyboard.add_hotkey('m+right', lambda: move_mouse(current_distance, 0))
keyboard.add_hotkey('m+x', switch_distance)
keyboard.add_hotkey('m+h', print_position)
keyboard.add_hotkey('m+j', bzone)
keyboard.add_hotkey('m+k', get_mouse_pos_and_color)
keyboard.add_hotkey('m+n', getcolor)

print("Hotkeys activated! Press ESC to exit.")
keyboard.wait('esc')
