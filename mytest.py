import keyboard
import threading
import math
import time
import pyautogui
import random
import os
from datetime import datetime
import numpy as np
import cv2
import mytract
import freez
import numMatch
import re
import traceback
# import discord_webhook
# import message

def handle_error(error_msg):
    """
    错误管理函数：记录错误信息和截图
    :param error_msg: 错误信息
    :param take_screenshot: 是否需要截图
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 确保错误目录存在
    if not os.path.exists("./error"):
        os.makedirs("./error")
    
    # 记录错误信息到日志
    with open("./error/error.log", "a", encoding='utf-8') as f:
        f.write(f"\n[{get_time()}] {'='*50}\n")
        f.write(f"Error Message: {error_msg}\n")
        if isinstance(error_msg, Exception):
            f.write(f"Traceback:\n{traceback.format_exc()}\n")
    
    # 如果需要，保存截图
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(f"./error/error_{timestamp}.png")
    except Exception as e:
        with open("./error/error.log", "a", encoding='utf-8') as f:
            f.write(f"Screenshot Error: {str(e)}\n")

def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

stop=threading.Event()
cleaning_end = threading.Event()
farming_end = threading.Event()
error_count=0
nopest=True
checkable=threading.Event()
checkable.set()

def color_check(r,g,b):
    bgr_color = np.array([[[b, g, r]]], dtype=np.uint8)
    hsv_color = cv2.cvtColor(bgr_color, cv2.COLOR_BGR2HSV)[0][0]
    # 判斷是否為深紅色
    h, s, v = hsv_color
    if(((0 <= h <= 10) or (170 <= h <= 180)) and
        s >= 100 and
        v <= 150):
        return True
    return False

def tycode(str):
    pyautogui.keyUp('w')
    pyautogui.keyUp('a')
    pyautogui.keyUp('s')
    pyautogui.keyUp('d')
    pyautogui.keyUp('t')
    pyautogui.keyUp('shiftleft')
    pyautogui.mouseUp(button='left',x=0,y=0)
    pyautogui.mouseUp(button='right',x=0,y=0)
    time.sleep(.5)
    pyautogui.press('t')
    pyautogui.press('backspace')
    pyautogui.write(str)
    time.sleep(.5)
    pyautogui.press('enter')

def gohome():
    pyautogui.keyUp('w')
    pyautogui.keyUp('a')
    pyautogui.keyUp('s')
    pyautogui.keyUp('d')
    pyautogui.keyUp('t')
    pyautogui.mouseUp(button='left',x=0,y=0)
    time.sleep(.5)
    pyautogui.press('t')
    pyautogui.press('backspace')
    time.sleep(1)
    pyautogui.write("/warp garden")
    time.sleep(1)
    pyautogui.press('enter')
    

go_list= [[False for _ in range(5)] for _ in range(3)]

def lookup():
    checkable.clear()
    for i in range(10):
        tycode('/desk')

        time.sleep(2)
        leaving=False
        try:
            loc= pyautogui.locateOnScreen('./pic/whereami/desk.png', confidence=0.8)
            if loc:
                leaving = True
        except Exception as e:
            print(f"[{get_time()}] Error locating desk image: {e}")
            handle_error(f"Error locating desk image: {e}")
            
        if leaving:
            break    
    else:
        print("not in desk")
        checkable.set()
        return False
    
    pyautogui.click(x=743, y=361)
    time.sleep(2)
    global go_list
    for i in range (3):
        for o in range(5):
            go_list[i][o]=False
            pyautogui.moveTo(x=819+72*o,y=353+72*i)
            time.sleep(0.3)
            #todo find pic /plothas.png
            try:
                loc= pyautogui.locateOnScreen('./pic/whereami/plothas.png', confidence=0.8)
                if loc:
                    go_list[i][o]=True
            except Exception as e:
                ...
    
    pyautogui.press('e')
    print(go_list)
    checkable.set()
    return True
    



def checking_farm():
    if not checkable.is_set():
        print("waiting for checking")
        return
    mytract.take_screenshot()
    result=mytract.search_plot() 
    if not result:
        time.sleep(5)
        mytract.take_screenshot()
        result=mytract.search_plot()
        if result:
            stop.clear()
            return

        print(f"[{get_time()}] out of plot")
        stop.set()
        result=mytract.search_vill()
        if result:
            print(f"[{get_time()}] in village")
            gohome()
            time.sleep(10)
        else:
            print(f"[{get_time()}] out of village")
            result=mytract.search_hypi()
            if result:
                print(f"[{get_time()}] in hypixel")
                tycode('/skyblock')
                time.sleep(20)
                gohome()
                time.sleep(10)
            else:
                print(f"[{get_time()}] out of hypixel")
                found=(0,0)
                result,found=mytract.search_back_to_list()
                if result:
                    print(f"[{get_time()}] going back to list")
                    x,y=found
                    pyautogui.click(x=956, y=643)
                    pyautogui.click(x=x, y=y)
                    time.sleep(5)
                    linking()
                else:
                    print("might in limbo")
                    pyautogui.press('esc')
                    pyautogui.click(x=950,y=550)
                    pyautogui.click(x=950,y=550)
                    pyautogui.click(x=950,y=550)
                    time.sleep(5)
                    linking()
    else:
        stop.clear()

def linking():
    while True:
        pyautogui.click(x=746, y=200)
        pyautogui.click(x=746, y=200)
        time.sleep(30)
        mytract.take_screenshot()
        result=mytract.search_hypi()
        if result:
            break
        result=mytract.search_back_to_list()
        if result:
            print("going back to list")
            pyautogui.click(x=956, y=643)
            time.sleep(5)
        else:
            global error_count
            error_count+=1
            error_msg = f"Not in hypixel or back to list, need help or waiting. Error count: {error_count}"
            handle_error(error_msg)
            print(f"[{get_time()}] {error_msg}")
            # message.send_discord_message()
            if error_count>5:
                critical_error = f"Too many errors ({error_count}), shutting down system"
                handle_error(critical_error)
                print(f"[{get_time()}] {critical_error}")
                pyautogui.press('esc')
                pyautogui.click(x=950,y=550)
                pyautogui.click(x=950,y=550)
                pyautogui.click(x=950,y=550)
                os.system("shutdown -h now")
                return
            time.sleep(10)

    tycode('/skyblock')
    time.sleep(20)
    gohome()
    time.sleep(10)
        #checking
        
def freez_and_wait(loop):#10min for 1 loop
    freez.freeze(freez.find_minecraft_pid())
    print(f'sleeping for {loop/6} hours')
    for i in range(0,loop):
            time.sleep(600)
            pyautogui.keyDown('w')
            time.sleep(.5)
            pyautogui.keyUp('w')
            pyautogui.keyDown('s')
            time.sleep(.5)
            pyautogui.keyUp('s')
    freez.unfreeze(freez.find_minecraft_pid())


def func(delayhour=2, wait=False):
    delaytime = delayhour* 6
    if wait:
        freez_and_wait(delaytime)

        pyautogui.click(x=746, y=200)
        pyautogui.click(x=746, y=200)
        time.sleep(30)
        tycode('/skyblock')
        time.sleep(20)
        gohome()
        time.sleep(10)
        #checking

    for i in range (0,10):
        checking_farm()
        error_count=0
        print('runing'+str(i))
        for n in range(4):

            if nopest:# and n!=0:
                thread2= threading.Thread(target=pestout)
                print(f"[{get_time()}] cleaning1")
                cleaning_end.set()
                thread2.start()
                time.sleep(10)
                # while cleaning_end.is_set():
                #     time.sleep(10)
                #     checking_farm()

                print(f"[{get_time()}] cleaning1 end")
                thread2.join()
                cleaning_end.clear()

                thread2= threading.Thread(target=pestout)
                print(f"[{get_time()}] cleaning2")
                cleaning_end.set()
                thread2.start()
                time.sleep(10)
                # while cleaning_end.is_set():
                #     time.sleep(10)
                #     checking_farm()

                print(f"[{get_time()}] cleaning2 end")
                thread2.join()
                cleaning_end.clear()

            thread1= threading.Thread(target=mepu)
            print(f"[{get_time()}] farming")
            farming_end.set()
            thread1.start()
            time.sleep(10)
            while farming_end.is_set():
                time.sleep(10)
                checking_farm()

            print(f"[{get_time()}] farming end")
            thread1.join()
            farming_end.clear()
            

        time.sleep(2)

        pyautogui.press('esc')
        pyautogui.click(x=950,y=550)
        pyautogui.click(x=950,y=550)
        pyautogui.click(x=950,y=550)

        print(f"[{get_time()}] start waiting")

        rep=random.randint(24, 30)
        freez_and_wait(rep)

        print(f"[{get_time()}] going back to game")
        
        pyautogui.click(x=746, y=200)
        pyautogui.click(x=746, y=200)
        time.sleep(30)
        tycode('/skyblock')
        time.sleep(20)
        gohome()
        time.sleep(10)
        
        


def restartfarming(loop):
    
    while stop.is_set():
        time.sleep(10)
        
    print(f"[{get_time()}] restart farming")
    mepu(loop)
    
        

def mepu(loop=3):
    pyautogui.mouseUp(button='left',x=0,y=0)
    t=67
    pyautogui.press('3')
    time.sleep(1)
    pyautogui.keyDown('shiftleft')
    time.sleep(.1)
    pyautogui.keyUp('shiftleft')
    for i in range (loop):
        print('m'+str(i))
        checkable.clear()
        gohome()
        checkable.set()
        time.sleep(.5)
        pyautogui.mouseDown(button='left',x=0,y=0)
        pyautogui.keyDown('w')
        for n in range(0,6):
            pyautogui.keyDown('a')
            time.sleep(2)
            #delay?
            
            for p in range(25):
                if stop.is_set():
                    pyautogui.keyUp('a')
                    pyautogui.mouseUp(button='left',x=0,y=0)
                    pyautogui.keyUp('w')
                    print(f"[{get_time()}] stop farming")
                    restartfarming(loop-i)
                    return
                if p>12:
                    r,g,b=pyautogui.pixel(11, 766)
                    if color_check(r,g,b):
                        break
                    r,g,b=pyautogui.pixel(291,947)
                    if color_check(r,g,b):
                        break
                
                time.sleep(5)
            
            pyautogui.keyUp('a')
            pyautogui.keyDown('d')
            time.sleep(2)
            #delay?

            for p in range(25):
                if stop.is_set():
                    pyautogui.keyUp('d')
                    pyautogui.mouseUp(button='left',x=0,y=0)
                    pyautogui.keyUp('w')
                    print(f"[{get_time()}] stop farming")
                    restartfarming(loop-i)
                    return
                if p>12:
                    r,g,b=pyautogui.pixel(1909, 766)
                    if color_check(r,g,b) or n==5:
                        break
                time.sleep(5)
            
            pyautogui.keyUp('d')

    pyautogui.keyUp('w')
    pyautogui.mouseUp(button='left',x=0,y=0)
    farming_end.clear()

def oldpestout():
    gohome()
    time.sleep(2)
    pyautogui.press('4')
    time.sleep(1)
    
    for n in range(0,6):
        pyautogui.mouseDown(button='right',x=0,y=0)
        # if(n==1 or n==4):
        #     pyautogui.keyDown('a')
        #     pyautogui.keyDown('shiftleft')
        #     time.sleep(159)
        #     pyautogui.keyUp('a')
        #     pyautogui.keyUp('shiftleft')
        # else:
        pyautogui.keyDown('a')
        time.sleep(49)
        pyautogui.keyUp('a')

        pyautogui.mouseUp(button='right',x=0,y=0)

        if stop.is_set():
            print(f"[{get_time()}] stop cleaning")
            cleaning_end.clear()
            return

        pyautogui.keyDown('w')
        time.sleep(1)
        pyautogui.keyUp('w')

        pyautogui.mouseDown(button='right',x=0,y=0)

        if(n==1 or n==3 or n==5):
            pyautogui.keyDown('d')
            pyautogui.keyDown('shiftleft')
            time.sleep(159)
            pyautogui.keyUp('d')
            pyautogui.keyUp('shiftleft')
        else:
            pyautogui.keyDown('d')
            time.sleep(50)
            pyautogui.keyUp('d')

        pyautogui.keyDown('w')
        time.sleep(1)
        pyautogui.keyUp('w')

        pyautogui.mouseUp(button='right',x=0,y=0)

        if stop.is_set():
            print(f"[{get_time()}] stop cleaning")
            cleaning_end.clear()
            return
    
    print(f"[{get_time()}] clean")
    cleaning_end.clear()

def restartpest():
    while stop.is_set():
        time.sleep(10)
    print(f"[{get_time()}] restart pest")
    pestout()

plotname=[[10,2,-1,3,11],[17,7,4,8,18],[23,19,12,20,24]]

def pestout():
    checkable.clear()
    gohome()
    checkable.set()
    time.sleep(2)
    if(lookup()):
        print(f"[{get_time()}] cleaning")
    else:
        print(f"[{get_time()}] not in desk or no plot error")
        return
    
    for i in range (5):
        if go_list[0][i]:
            print(f"[{get_time()}] cleaning layer 1 plot {i}")
            checkable.clear()
            gohome()
            checkable.set()
            pyautogui.keyDown('space')
            time.sleep(6)
            pyautogui.keyDown('s')
            time.sleep(1)
            pyautogui.keyUp('space')
            pyautogui.keyUp('s')
            pyautogui.press('5')
            time.sleep(0.5)
            pyautogui.click(x=0,y=0)
            pyautogui.click(x=0,y=0)
            time.sleep(1)
            pyautogui.press('4')
            pyautogui.mouseDown(button='right',x=0,y=0)

            if stop.is_set():
                print(f"[{get_time()}] stop cleaning")
                restartpest()
                cleaning_end.clear()
                return
                
            pyautogui.keyDown('s')
            time.sleep(6)
            pyautogui.keyUp('s')

            pyautogui.keyDown('a')
            time.sleep(3.6)
            for o in range(0,i):
                time.sleep(5.6)
                if stop.is_set():
                    print(f"[{get_time()}] stop cleaning")
                    restartpest()
                    cleaning_end.clear()
                    return
                
            pyautogui.click(button='left',x=0,y=0)
            pyautogui.keyDown('w')
            time.sleep(3)
            pyautogui.keyUp('w')
            pyautogui.keyUp('a')
            pyautogui.mouseUp(button='right',x=0,y=0)
            pestnum,plotnum=numMatch.pestinplot()
            if pestnum<1 or plotnum!=plotname[0][i]:
                error_msg = f"Plot mismatch error: Expected plot {plotname[0][i]}, found plot {plotnum}"
                handle_error(error_msg)
                print(f"[{get_time()}] {error_msg}")
            pyautogui.click(button='right',x=0,y=0)
            pyautogui.keyDown('w')
            
            for o in range(5):
                pyautogui.click(button='left',x=0,y=0)
                pyautogui.mouseDown(button='right',x=0,y=0)
                pyautogui.keyDown('d')
                time.sleep(8)
                pyautogui.keyUp('d')

                if stop.is_set():
                    print(f"[{get_time()}] stop cleaning")
                    restartpest()
                    cleaning_end.clear()
                    return
                pyautogui.mouseUp(button='right',x=0,y=0)
                pyautogui.click(button='left',x=0,y=0)
                pyautogui.mouseDown(button='right',x=0,y=0)
                pyautogui.keyDown('a')
                time.sleep(8)
                pyautogui.keyUp('a')
                if stop.is_set():
                    print(f"[{get_time()}] stop cleaning")
                    restartpest()
                    cleaning_end.clear()
                    return
                pyautogui.mouseUp(button='right',x=0,y=0)
            
            pyautogui.click(button='left',x=0,y=0)

            pyautogui.mouseDown(button='right',x=0,y=0)
            pyautogui.keyDown('d')
            time.sleep(8)
            pyautogui.keyUp('d')

            pyautogui.keyUp('w')
            pyautogui.mouseUp(button='right',x=0,y=0)
            
            if stop.is_set():
                print(f"[{get_time()}] stop cleaning")
                restartpest()
                cleaning_end.clear()
                return
            
            #keep on higher layer
            for o in range(i,5):
                if go_list[1][o]:
                    print(f"[{get_time()}] cleaning layer 2 plot {o}")
                    pyautogui.mouseDown(button='right',x=0,y=0)
                    pyautogui.keyDown('a')
                    time.sleep(3.6)
                    for u in range(0,o-i):
                        time.sleep(5.6)
                        if stop.is_set():
                            print(f"[{get_time()}] stop cleaning")
                            restartpest()
                            cleaning_end.clear()
                            return
                        
                    pyautogui.click(button='left',x=0,y=0)    
                    pyautogui.keyDown('w')
                    time.sleep(3)
                    pyautogui.keyUp('w')
                    pyautogui.keyUp('a')
                    pyautogui.mouseUp(button='right',x=0,y=0)
                    pestnum,plotnum=numMatch.pestinplot()
                    if pestnum<1 or plotnum!=plotname[1][o]:
                        print(f"sth went wrong, plot{plotname[1][o]} didnt match found plot:{plotnum}")
                    pyautogui.click(button='right',x=0,y=0)
                    pyautogui.keyDown('w')
                    
                    for u in range(5):
                        pyautogui.click(button='left',x=0,y=0)
                        pyautogui.mouseDown(button='right',x=0,y=0)
                        pyautogui.keyDown('d')
                        time.sleep(8)
                        pyautogui.keyUp('d')

                        if stop.is_set():
                            print(f"[{get_time()}] stop cleaning")
                            restartpest()
                            cleaning_end.clear()
                            return
                        pyautogui.mouseUp(button='right',x=0,y=0)
                        pyautogui.click(button='left',x=0,y=0)
                        pyautogui.mouseDown(button='right',x=0,y=0)
                        pyautogui.keyDown('a')
                        time.sleep(8)
                        pyautogui.keyUp('a')
                        if stop.is_set():
                            print(f"[{get_time()}] stop cleaning")
                            restartpest()
                            cleaning_end.clear()
                            return
                        pyautogui.mouseUp(button='right',x=0,y=0)
                    
                    pyautogui.click(button='left',x=0,y=0)

                    pyautogui.mouseDown(button='right',x=0,y=0)
                    pyautogui.keyDown('d')
                    time.sleep(8)
                    pyautogui.keyUp('d')

                    pyautogui.keyUp('w')
                    pyautogui.mouseUp(button='right',x=0,y=0)
                    
                    if stop.is_set():
                        print(f"[{get_time()}] stop cleaning")
                        restartpest()
                        cleaning_end.clear()
                        return
                    go_list[1][o]=False

                    for p in range(o,5):
                        if go_list[2][p]:
                            print(f"[{get_time()}] cleaning layer 3 plot {p}")
                            pyautogui.mouseDown(button='right',x=0,y=0)
                            pyautogui.keyDown('a')
                            time.sleep(3.6)
                            for u in range(0,p-o):
                                time.sleep(5.6)
                                if stop.is_set():
                                    print(f"[{get_time()}] stop cleaning")
                                    restartpest()
                                    cleaning_end.clear()
                                    return
                                
                            pyautogui.click(button='left',x=0,y=0)
                            pyautogui.keyDown('w')
                            time.sleep(3)
                            pyautogui.keyUp('w')
                            pyautogui.keyUp('a')
                            pyautogui.mouseUp(button='right',x=0,y=0)
                            pestnum,plotnum=numMatch.pestinplot()
                            if pestnum<1 or plotnum!=plotname[2][p]:
                                print(f"sth went wrong, plot{plotname[2][p]} didnt match found plot:{plotnum}")
                            pyautogui.click(button='right',x=0,y=0)
                            pyautogui.keyDown('w')
                            
                            for o in range(5):
                                pyautogui.click(button='left',x=0,y=0)
                                pyautogui.mouseDown(button='right',x=0,y=0)
                                pyautogui.keyDown('d')
                                time.sleep(8)
                                pyautogui.keyUp('d')

                                if stop.is_set():
                                    print(f"[{get_time()}] stop cleaning")
                                    restartpest()
                                    cleaning_end.clear()
                                    return
                                pyautogui.mouseUp(button='right',x=0,y=0)
                                pyautogui.click(button='left',x=0,y=0)
                                pyautogui.mouseDown(button='right',x=0,y=0)
                                pyautogui.keyDown('a')
                                time.sleep(8)
                                pyautogui.keyUp('a')
                                if stop.is_set():
                                    print(f"[{get_time()}] stop cleaning")
                                    restartpest()
                                    cleaning_end.clear()
                                    return
                                pyautogui.mouseUp(button='right',x=0,y=0)
                            
                            pyautogui.click(button='left',x=0,y=0)

                            pyautogui.mouseDown(button='right',x=0,y=0)
                            pyautogui.keyDown('d')
                            time.sleep(8)
                            pyautogui.keyUp('d')

                            pyautogui.keyUp('w')
                            pyautogui.mouseUp(button='right',x=0,y=0)
                            
                            if stop.is_set():
                                print(f"[{get_time()}] stop cleaning")
                                restartpest()
                                cleaning_end.clear()
                                return
                            go_list[2][p]=False
                            break
                    
                    break


    for i in range (5):
        if go_list[1][i]:
            print(f"[{get_time()}] cleaning layer 2 plot {i}")
            checkable.clear()
            gohome()
            checkable.set()
            pyautogui.keyDown('space')
            time.sleep(6)
            pyautogui.keyDown('a')
            time.sleep(1)
            pyautogui.keyUp('space')
            pyautogui.keyUp('a')
            pyautogui.press('5')
            time.sleep(0.5)
            pyautogui.click(x=0,y=0)
            pyautogui.click(x=0,y=0)
            time.sleep(1)
            pyautogui.press('4')
            pyautogui.mouseDown(button='right',x=0,y=0)
            pyautogui.keyDown('a')
            time.sleep(3.6)
            for o in range(0,i):
                time.sleep(5.6)
                if stop.is_set():
                    print(f"[{get_time()}] stop cleaning")
                    restartpest()
                    cleaning_end.clear()
                    return
            
            pyautogui.click(button='left',x=0,y=0)
            pyautogui.keyDown('w')
            time.sleep(3)
            pyautogui.keyUp('w')
            pyautogui.keyUp('a')
            pyautogui.mouseUp(button='right',x=0,y=0)
            pestnum,plotnum=numMatch.pestinplot()
            if pestnum<1 or plotnum!=plotname[1][i]:
                error_msg = f"Plot mismatch error: Expected plot {plotname[1][i]}, found plot {plotnum}"
                handle_error(error_msg)
                print(f"[{get_time()}] {error_msg}")
            pyautogui.click(button='right',x=0,y=0)
            pyautogui.keyDown('w')
            
            for o in range(5):
                pyautogui.click(button='left',x=0,y=0)
                pyautogui.mouseDown(button='right',x=0,y=0)
                pyautogui.keyDown('d')
                time.sleep(8)
                pyautogui.keyUp('d')

                if stop.is_set():
                    print(f"[{get_time()}] stop cleaning")
                    restartpest()
                    cleaning_end.clear()
                    return
                pyautogui.mouseUp(button='right',x=0,y=0)
                pyautogui.click(button='left',x=0,y=0)
                pyautogui.mouseDown(button='right',x=0,y=0)
                pyautogui.keyDown('a')
                time.sleep(8)
                pyautogui.keyUp('a')
                if stop.is_set():
                    print(f"[{get_time()}] stop cleaning")
                    restartpest()
                    cleaning_end.clear()
                    return
                pyautogui.mouseUp(button='right',x=0,y=0)
            
            pyautogui.click(button='left',x=0,y=0)

            pyautogui.mouseDown(button='right',x=0,y=0)
            pyautogui.keyDown('d')
            time.sleep(8)
            pyautogui.keyUp('d')

            pyautogui.keyUp('w')
            pyautogui.mouseUp(button='right',x=0,y=0)
            
            if stop.is_set():
                print(f"[{get_time()}] stop cleaning")
                restartpest()
                cleaning_end.clear()
                return
            
            #keep on higher layer
            for o in range(i,5):
                if go_list[2][o]:
                    print(f"[{get_time()}] cleaning layer 3 plot {o}")
                    pyautogui.mouseDown(button='right',x=0,y=0)
                    pyautogui.keyDown('a')
                    time.sleep(3.6)
                    for u in range(0,o-i):
                        time.sleep(5.6)
                        if stop.is_set():
                            print(f"[{get_time()}] stop cleaning")
                            restartpest()
                            cleaning_end.clear()
                            return
                    
                    pyautogui.click(button='left',x=0,y=0)
                    pyautogui.keyDown('w')
                    time.sleep(3)
                    pyautogui.keyUp('w')
                    pyautogui.keyUp('a')
                    pyautogui.mouseUp(button='right',x=0,y=0)
                    pestnum,plotnum=numMatch.pestinplot()
                    if pestnum<1 or plotnum!=plotname[2][o]:
                        print(f"sth went wrong, plot{plotname[2][o]} didnt match found plot:{plotnum}")
                    pyautogui.click(button='right',x=0,y=0)
                    pyautogui.keyDown('w')
                    
                    for u in range(5):
                        pyautogui.click(button='left',x=0,y=0)
                        pyautogui.mouseDown(button='right',x=0,y=0)
                        pyautogui.keyDown('d')
                        time.sleep(8)
                        pyautogui.keyUp('d')

                        if stop.is_set():
                            print(f"[{get_time()}] stop cleaning")
                            restartpest()
                            cleaning_end.clear()
                            return
                        pyautogui.mouseUp(button='right',x=0,y=0)
                        pyautogui.click(button='left',x=0,y=0)
                        pyautogui.mouseDown(button='right',x=0,y=0)
                        pyautogui.keyDown('a')
                        time.sleep(8)
                        pyautogui.keyUp('a')
                        if stop.is_set():
                            print(f"[{get_time()}] stop cleaning")
                            restartpest()
                            cleaning_end.clear()
                            return
                        pyautogui.mouseUp(button='right',x=0,y=0)
                    
                    pyautogui.click(button='left',x=0,y=0)

                    pyautogui.mouseDown(button='right',x=0,y=0)
                    pyautogui.keyDown('d')
                    time.sleep(8)
                    pyautogui.keyUp('d')

                    pyautogui.keyUp('w')
                    pyautogui.mouseUp(button='right',x=0,y=0)
                    
                    if stop.is_set():
                        print(f"[{get_time()}] stop cleaning")
                        restartpest()
                        cleaning_end.clear()
                        return
                    go_list[2][o]=False
                    break
                
    for i in range (5):
        if go_list[2][i]:
            print(f"[{get_time()}] cleaning layer 3 plot {i}")
            checkable.clear()
            gohome()
            checkable.set()
            pyautogui.keyDown('space')
            time.sleep(6)
            pyautogui.keyDown('w')
            time.sleep(1)
            pyautogui.keyUp('space')
            pyautogui.keyUp('w')
            pyautogui.press('5')
            time.sleep(0.5)
            pyautogui.click(x=0,y=0)
            pyautogui.click(x=0,y=0)
            time.sleep(1)
            pyautogui.press('4')
            pyautogui.mouseDown(button='right',x=0,y=0)

            if stop.is_set():
                print(f"[{get_time()}] stop cleaning")
                restartpest()
                cleaning_end.clear()
                return
             
            pyautogui.keyDown('w')
            time.sleep(6)
            pyautogui.keyUp('w')

            pyautogui.keyDown('a')
            time.sleep(3.6)
            for o in range(0,i):
                time.sleep(5.6)
                if stop.is_set():
                    print(f"[{get_time()}] stop cleaning")
                    restartpest()
                    cleaning_end.clear()
                    return
            
            pyautogui.click(button='left',x=0,y=0)
            pyautogui.keyDown('w')
            time.sleep(3)
            pyautogui.keyUp('w')
            pyautogui.keyUp('a')
            pyautogui.mouseUp(button='right',x=0,y=0)
            pestnum,plotnum=numMatch.pestinplot()
            if pestnum<1 and plotnum!=plotname[2][i]:
                print(f"sth went wrong, plot{plotname[2][i]} didnt match found plot:{plotnum}")
            pyautogui.click(button='right',x=0,y=0)
            pyautogui.keyDown('w')
            
            for o in range(5):
                pyautogui.click(button='left',x=0,y=0)
                pyautogui.mouseDown(button='right',x=0,y=0)
                pyautogui.keyDown('d')
                time.sleep(8)
                pyautogui.keyUp('d')

                if stop.is_set():
                    print(f"[{get_time()}] stop cleaning")
                    restartpest()
                    cleaning_end.clear()
                    return
                pyautogui.mouseUp(button='right',x=0,y=0)
                pyautogui.click(button='left',x=0,y=0)
                pyautogui.mouseDown(button='right',x=0,y=0)
                pyautogui.keyDown('a')
                time.sleep(8)
                pyautogui.keyUp('a')
                if stop.is_set():
                    print(f"[{get_time()}] stop cleaning")
                    restartpest()
                    cleaning_end.clear()
                    return
                pyautogui.mouseUp(button='right',x=0,y=0)
            
            pyautogui.click(button='left',x=0,y=0)

            pyautogui.mouseDown(button='right',x=0,y=0)
            pyautogui.keyDown('d')
            time.sleep(8)
            pyautogui.keyUp('d')

            pyautogui.keyUp('w')
            pyautogui.mouseUp(button='right',x=0,y=0)
            
            if stop.is_set():
                print(f"[{get_time()}] stop cleaning")
                restartpest()
                cleaning_end.clear()
                return
    
    num=numMatch.pestingarden()
    print(f"[{get_time()}] cleaning end found {num} pest left")
    cleaning_end.clear()
    
    

def execute_command(command):
    """
    执行指定的命令
    :param command: 要执行的命令名称
    """
    command = command.strip()  # 移除多余空格
    if not command:  # 跳过空行
        return
    
    try:
        if command == 'func':
            func()
        elif command.startswith('func '):
            # 解析参数，例如 "func 2 true" -> func(2, True)
            args = command.split()[1:]
            if len(args) >= 1:
                delayhour = int(args[0])
                wait = bool(args[1].lower() == 'true') if len(args) > 1 else False
                func(delayhour, wait)
            else:
                func()
        elif command == 'oldpestout':
            oldpestout()
        elif command == 'pestout':
            pestout()
        elif command.startswith('mepu '):
            # 解析参数，例如 "mepu 3" -> mepu(3)
            loop = int(command.split()[1])
            mepu(loop)
        elif command == 'mepu':
            mepu()
        else:
            print(f"[{get_time()}] Unknown command: {command}")
            handle_error(f"Unknown command: {command}")
    except Exception as e:
        print(f"[{get_time()}] Error executing command {command}: {str(e)}")
        handle_error(e)

def run_command_file():
    """
    从 command.txt 读取并执行命令
    文件格式：每行一个命令
    例如：
    func 2 true
    pestout
    mepu 3
    """
    try:
        with open('command.txt', 'r', encoding='utf-8') as f:
            commands = f.readlines()
        
        print(f"[{get_time()}] Found {len(commands)} commands")
        
        for i, command in enumerate(commands, 1):
            print(f"[{get_time()}] Executing command {i}/{len(commands)}: {command.strip()}")
            execute_command(command)
            
        print(f"[{get_time()}] All commands executed")
        
    except FileNotFoundError:
        print(f"[{get_time()}] command.txt not found")
        handle_error("command.txt not found")
    except Exception as e:
        print(f"[{get_time()}] Error reading command file: {str(e)}")
        handle_error(e)

# Set up the hotkeys
keyboard.add_hotkey('u+i',func)  # func2
keyboard.wait('esc')