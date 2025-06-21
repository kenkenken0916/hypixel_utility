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


def func():
    t=100 #66.4
    repeat=3
    for o in range(0,2):
        gohome()
        #winsound.Beep(1000,1000)
        time.sleep(.5)
        pyautogui.mouseDown(button='left',x=0,y=0)
        for i in range(0,9):
            pyautogui.keyDown('w')
            time.sleep(1.5)
            pyautogui.keyUp('w')
            pyautogui.keyDown('d')
            time.sleep(18.5)
            #time.sleep(random.random())
            pyautogui.keyUp('d')
            pyautogui.keyDown('w')

            time.sleep(1.5)
            pyautogui.keyUp('w')
            pyautogui.keyDown('a')
            time.sleep(18.5)
            #time.sleep(random.random())
            pyautogui.keyUp('a')
        pyautogui.mouseUp(button='left',x=0,y=0)
    
    # pyautogui.press('esc')
    # pyautogui.click(x=950,y=550)
    # pyautogui.click(x=950,y=550)
    # os.system("shutdown -h now")

#
def func2():
    for i in range (0,5):
        print('f'+str(i))
        
        mepu()
        time.sleep(2)
        pyautogui.press('esc')
        pyautogui.click(x=950,y=550)
        pyautogui.click(x=950,y=550)

        rep=random.randint(18,24)
        for i in range(0,rep):
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
        




#Mouse Position: (x=1490, y=220)
#Mouse Position: (x=1919, y=820)

def mepu():
    t=67
    pyautogui.keyDown('shiftleft')
    time.sleep(.1)
    pyautogui.keyUp('shiftleft')
    for i in range (15):
        print('m'+str(i))
        if(i%4==3):
            pyautogui.press('4')
            time.sleep(1)
            pestout()
            time.sleep(1)
            pyautogui.press('3')
        
        gohome()
        time.sleep(.5)
        pyautogui.mouseDown(button='left',x=0,y=0)
        pyautogui.keyDown('w')
        for n in range(0,6):
            pyautogui.keyDown('a')
            time.sleep(t)
            #time.sleep(random.random())
            pyautogui.keyUp('a')
            pyautogui.keyDown('d')
            time.sleep(t)
            #time.sleep(random.random())
            pyautogui.keyUp('d')
    pyautogui.keyUp('w')
    pyautogui.mouseUp(button='left',x=0,y=0)
    # pyautogui.press('esc')
    # pyautogui.click(x=950,y=550)
    # pyautogui.click(x=950,y=550)
    # os.system("shutdown -h now")

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
    pyautogui.mouseDown(button='right',x=0,y=0)
    for n in range(0,6):
        if(n==1 or n==4):
            pyautogui.keyDown('a')
            pyautogui.keyDown('shiftleft')
            time.sleep(163)
            pyautogui.keyUp('a')
            pyautogui.keyUp('shiftleft')
        else:
            pyautogui.keyDown('a')
            time.sleep(50)
            pyautogui.keyUp('a')

        pyautogui.keyDown('w')
        time.sleep(1)
        pyautogui.keyUp('w')

        if(n==2 or n==5):
            pyautogui.keyDown('d')
            pyautogui.keyDown('shiftleft')
            time.sleep(163)
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

def cati()->None:#spd400 仰角~0
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

def fino():#300
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


def flyaround():
    #gohome()
    time.sleep(1)
    pyautogui.press('9')
    time.sleep(1)
    pyautogui.click(x=0, y=0, button='right')
    time.sleep(1)
    pyautogui.click(x=749, y=283)
    time.sleep(1)
    pyautogui.click(x=749, y=354)
    time.sleep(1)
    pyautogui.click(x=963, y=433, button='right')
    time.sleep(2)
    pyautogui.keyDown(' ')
    pyautogui.keyUp(' ')
    pyautogui.keyDown(' ')
    time.sleep(0.5)
    pyautogui.keyDown('w')
    time.sleep(1)
    pyautogui.keyUp('w')
    time.sleep(0.5)
    pyautogui.press('8')
    time.sleep(0.5)
    pyautogui.click(x=0, y=0)
    time.sleep(0.5)
    pyautogui.press('4')
    pyautogui.mouseDown(button='right',x=0,y=0)
    pyautogui.keyDown('a')
    time.sleep(30)
    pyautogui.keyUp('a')
    for i in range (0,9):
        pyautogui.keyDown('w')
        time.sleep(2)
        pyautogui.keyUp('w')
        pyautogui.keyDown('d')
        time.sleep(45)
        pyautogui.keyUp('d')
        pyautogui.keyDown('w')
        time.sleep(2)
        pyautogui.keyUp('w')
        pyautogui.keyDown('a')
        time.sleep(45)
        pyautogui.keyUp('a')
    pyautogui.mouseUp(button='right',x=0,y=0)
    pyautogui.keyDown('shiftleft')
    time.sleep(5)
    pyautogui.keyUp('shiftleft')
    pyautogui.press('3')

# Set up the hotkeys
keyboard.add_hotkey('u+i',func2)#func2
keyboard.wait('esc')