import pyautogui
import time
import numpy as np
import cv2

# 目標座標
x, y = 1909, 766
time.sleep(8)
# 取得 RGB 顏色
r, g, b = pyautogui.pixel(x, y)

# 構造正確型別：np.uint8(NumPy 陣列，形狀為 (1, 1, 3))
bgr_color = np.array([[[b, g, r]]], dtype=np.uint8)

# 轉 HSV
hsv_color = cv2.cvtColor(bgr_color, cv2.COLOR_BGR2HSV)[0][0]

print(f"Pixel at ({x},{y}) -> HSV: {hsv_color}")

# 判斷是否為深紅色
h, s, v = hsv_color
is_deep_red = (
    ((0 <= h <= 10) or (170 <= h <= 180)) and
    s >= 100 and
    v <= 150
)

if is_deep_red:
    print("這是深紅色！")
else:
    print("這不是深紅色。")
