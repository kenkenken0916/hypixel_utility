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
# import discord_webhook
# import message

def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

stop=threading.Event()
cleaning_end = threading.Event()
farming_end = threading.Event()
error_count=0

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
    for i in range(10):
        tycode('/desk')
        #todo fimd pic /desk.png break
        if():
            break
        time.sleep(2)
    else:
        print("not in desk")
        return False
    
    pyautogui.click(x=743, y=361)
    time.sleep(2)
    for i in range (3):
        for o in range(5):
            go_list[i][o]=False
            pyautogui.moveTo(x=819+72*i,y=353+72*o)
            #todo find pic /plothas.png
            if() :
                go_list[i][o]=True
    
    pyautogui.press('e')
    return True
    

def checking_farm():
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
            print(f"[{get_time()}] not in hypixel or back to list need help or waiting")
            # message.send_discord_message()
            if error_count>5:
                print(f"[{get_time()}] too many errors, stopping")
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


def func(delayhour=3, wait=False):
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

    for i in range (0,5):
        checking_farm()
        error_count=0
        print('runing'+str(i))
        for n in range(4):
            thread1= threading.Thread(target=mepu)
            thread2= threading.Thread(target=pestout)

            if n!=0:
                print(f"[{get_time()}] cleaning")
                cleaning_end.set()
                thread2.start()
                while cleaning_end.is_set():
                    time.sleep(10)
                    checking_farm()

                print(f"[{get_time()}] cleaning end")
                thread2.join()
                cleaning_end.clear()

            print(f"[{get_time()}] farming")
            farming_end.set()
            thread1.start()

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
    print(f"[{get_time()}] restart farming")
    while stop.is_set():
        time.sleep(10)
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
        gohome()
        time.sleep(.5)
        pyautogui.mouseDown(button='left',x=0,y=0)
        pyautogui.keyDown('w')
        for n in range(0,6):
            pyautogui.keyDown('a')
            time.sleep(t)
            #delay?
            
            for p in range(12):
                if stop.is_set():
                    pyautogui.keyUp('a')
                    print(f"[{get_time()}] stop farming")
                    restartfarming(loop-i)
                    return
                r,g,b=pyautogui.pixel(11, 766)
                if color_check(r,g,b):
                    break
                r,g,b=pyautogui.pixel(291,947)
                if color_check(r,g,b):
                    break
                
                time.sleep(5)
            
            pyautogui.keyUp('a')
            pyautogui.keyDown('d')
            time.sleep(t)
            #delay?

            for p in range(12):
                if stop.is_set():
                    pyautogui.keyUp('a')
                    print(f"[{get_time()}] stop farming")
                    restartfarming(loop-i)
                    return
                r,g,b=pyautogui.pixel(1909, 766)
                if color_check(r,g,b) or n==5:
                    break
                time.sleep(5)
            
            pyautogui.keyUp('d')

    pyautogui.keyUp('w')
    pyautogui.mouseUp(button='left',x=0,y=0)
    farming_end.clear()

def mepush():
    mepu()
    time.sleep(2)
    pyautogui.press('esc')
    pyautogui.click(x=950,y=550)
    pyautogui.click(x=950,y=550)
    pyautogui.click(x=950,y=550)
    os.system("shutdown -h now")

def pestout():
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


'''
def new_pestout():
    gohome()
    time.sleep(2)
    pyautogui.press('4')
    time.sleep(1)
    while not stop.is_set():
        tycode('/desk')
        #todo take picture and check is in desk menu
    
        if result is True:
            break
    
    #todo go to plot map

    #todo hover on everyplot and screen shot find pest amount
    # plot_status is a 3*5 array store pestamount
    plot_status = [[0 for _ in range(5)] for _ in range(3)]
    
    #todo start from bottom layer use path goto entry and do small pestout
    #then second layer some has faster way dont walt from the start
    # if third layer has pest keep doinkg layer 3 and dont go to start and go there again
    #always go up left plot if has pest
    #then is the left layer 3



'''
#use comm /desk
#while not exist picture_dirt
#   check if exist picture_dirt
#click on dirt
#go_list: bool[3][5]
#for15
#   hover on 15 plot pic
#   find pic is_pest
#   if yes append to list

def coco()->None:#spd我忘了ㄏ 仰角45
    t=41
    for i in range(0,1):
        gohome()
        time.sleep(.5)
        pyautogui.mouseDown(button='left',x=0,y=0)
        for n in range(0,10):
            pyautogui.keyDown('s')
            pyautogui.keyDown('a')
            time.sleep(t)
            pyautogui.keyUp('a')
            pyautogui.keyUp('s')
            pyautogui.keyDown('d')
            pyautogui.keyDown('w')
            time.sleep(t+0.5)
            pyautogui.keyUp('w')
            pyautogui.keyUp('d')
    pyautogui.mouseUp(button='left',x=0,y=0)
    #winsound.Beep(1000,1000)

def sugar()->None:#spd328 仰角~0
    for o in range(0,5):
        gohome()
        time.sleep(.5)
        pyautogui.mouseDown(button='left',x=0,y=0)
        for n in range(0,15):
            pyautogui.keyDown('s')
            time.sleep(19.1)
            pyautogui.keyUp('s')
            pyautogui.keyDown('d')
            time.sleep(19.1)
            pyautogui.keyUp('d')
        pyautogui.keyDown('s')
        time.sleep(19.1)
        pyautogui.keyUp('s')
    pyautogui.mouseUp(button='left',x=0,y=0)

def cati()->None:#spd500 仰角~0
    t=18.5
    for i in range(0,5):
        gohome()
        time.sleep(.5)
        pyautogui.mouseDown(button='left',x=0,y=0)
        for n in range(0,13):
            pyautogui.keyDown('d')
            time.sleep(t)
            pyautogui.keyUp('d')
            pyautogui.keyDown('s')
            time.sleep(0.15)
            pyautogui.keyUp('s')
            pyautogui.keyDown('a')
            time.sleep(t)
            pyautogui.keyUp('a')
            pyautogui.keyDown('s')
            time.sleep(0.15)
            pyautogui.keyUp('s') 
        pyautogui.mouseUp(button='left',x=0,y=0)


def mush()->None:#spd232 仰角~5.5
    for o in range(0,20):
        gohome()
        time.sleep(.5)
        pyautogui.mouseDown(button='left',x=0,y=0)
        for n in range (0,3):
            pyautogui.keyDown('a')
            time.sleep(51.5)#85.3
            pyautogui.keyDown('s')
            time.sleep(0.7)
            pyautogui.keyUp('a')
            pyautogui.keyDown('d')
            time.sleep(56)#92.5
            pyautogui.keyUp('d')
            pyautogui.keyUp('s')
        pyautogui.mouseUp(button='left',x=0,y=0)
    #winsound.Beep(1000,1000)

def fino():#spd300
    t=89
    pyautogui.keyDown('shiftleft')
    time.sleep(.1)
    pyautogui.keyUp('shiftleft')
    for i in range (0,8):
        gohome()
        time.sleep(.5)
        pyautogui.mouseDown(button='left',x=0,y=0)
        pyautogui.keyDown('w')
        for n in range(0,4):
            pyautogui.keyDown('d')
            time.sleep(t)
            pyautogui.keyUp('d')
            pyautogui.keyDown('a')
            time.sleep(t)
            pyautogui.keyUp('a')
    pyautogui.keyUp('w')
    pyautogui.mouseUp(button='left',x=0,y=0)



# Set up the hotkeys
keyboard.add_hotkey('u+i',func)#func2
keyboard.wait('esc')