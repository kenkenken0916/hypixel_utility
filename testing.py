import pyautogui
import time
import numpy as np
import cv2
import numMatch

plot_img=cv2.imread("./pic/whereami/plot.png")
hypi_img=cv2.imread("./pic/whereami/hypi.png")
vill_img=cv2.imread("./pic/whereami/vill.png")
back_to_list_img=cv2.imread("./pic/whereami/back_to_list.png")
redgarden_img=cv2.imread("./pic/whereami/redgarden.png")
garden_img=cv2.imread("./pic/whereami/garden.png")

def capture_region(x, y, width, height):
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return frame
while True:
    screenshot = capture_region(0,0,1920,1080)

    score, loc=numMatch.match_single_template(screenshot, plot_img)
    if score > 0.8:
        print(f"Plot found with score: {score} at location: {loc}")
    else:
        print(f"Plot not found with score: {score}")
    time.sleep(3)