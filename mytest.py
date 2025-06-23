import keyboard
import time
import pyautogui
import random
import os


def tycode(str):
    pyautogui.keyUp('w')
    pyautogui.keyUp('a')
    pyautogui.keyUp('s')
    pyautogui.keyUp('d')
    pyautogui.keyUp('t')
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




def func(delayhour=6, wait=False):
    delaytime= delayhour* 6
    if wait:
        print("Waiting for", delaytime/6, "hours")
        for i in range(0,delaytime):
            time.sleep(600)
            pyautogui.keyDown('w')
            time.sleep(.5)
            pyautogui.keyUp('w')
            pyautogui.keyDown('s')
            time.sleep(.5)
            pyautogui.keyUp('s')

        pyautogui.click(x=746, y=200)
        pyautogui.click(x=746, y=200)
        time.sleep(30)
        tycode('/skyblock')
        time.sleep(20)
        gohome()
        time.sleep(10)

    for i in range (0,5):
        print('runing'+str(i))
        
        mepu()
        time.sleep(2)

        pyautogui.press('esc')
        pyautogui.click(x=950,y=550)
        pyautogui.click(x=950,y=550)

        print("start waiting")

        rep=random.randint(24, 30)
        for i in range(0,rep):
            time.sleep(600)
            pyautogui.keyDown('w')
            time.sleep(.5)
            pyautogui.keyUp('w')
            pyautogui.keyDown('s')
            time.sleep(.5)
            pyautogui.keyUp('s')

        print("going back to game")
        
        pyautogui.click(x=746, y=200)
        pyautogui.click(x=746, y=200)
        time.sleep(30)
        tycode('/skyblock')
        time.sleep(20)
        gohome()
        time.sleep(10)
        



def mepu(clean=True):
    t=67
    pyautogui.keyDown('shiftleft')
    time.sleep(.1)
    pyautogui.keyUp('shiftleft')
    for i in range (15):
        print('m'+str(i))
        if(i%4==3 and clean):
            pyautogui.press('4')
            time.sleep(1)
            pestout()
            time.sleep(1)
            pyautogui.press('3')
            #continue
        
        gohome()
        time.sleep(.5)
        pyautogui.mouseDown(button='left',x=0,y=0)
        pyautogui.keyDown('w')
        for n in range(0,6):
            pyautogui.keyDown('a')
            time.sleep(t)
            #delay?
            pyautogui.keyUp('a')
            pyautogui.keyDown('d')
            time.sleep(t)
            #delay?
            pyautogui.keyUp('d')
    pyautogui.keyUp('w')
    pyautogui.mouseUp(button='left',x=0,y=0)

def mepush():
    mepu()
    time.sleep(2)
    pyautogui.press('esc')
    pyautogui.click(x=950,y=550)
    pyautogui.click(x=950,y=550)
    os.system("shutdown -h now")

def pestout():
    gohome()
    time.sleep(2)
    
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
    
    print("clean")

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