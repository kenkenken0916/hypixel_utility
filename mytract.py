import pyautogui
import time
import cv2
import numpy as np
from PIL import Image

# 子圖比對 + 支援透明遮罩
def match_template_with_transparency(screen_img, template_img):
    screen = np.array(screen_img.convert('RGB'))
    template_rgba = template_img.convert('RGBA')
    template = np.array(template_rgba)

    alpha = template[:, :, 3]
    mask = cv2.threshold(alpha, 1, 255, cv2.THRESH_BINARY)[1]

    template_bgr = cv2.cvtColor(template[:, :, :3], cv2.COLOR_RGB2BGR)
    screen_bgr = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

    res = cv2.matchTemplate(screen_bgr, template_bgr, cv2.TM_CCORR_NORMED, mask=mask)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val > 0.9:
        return max_loc, max_val
    return None, max_val

# 指定區域（例如左上角 400x300 的範圍）
search_region = (100, 100, 400, 300)  # (left, top, width, height)

# 載入模板圖
hypi=Image.open("hypi.png")
plot=Image.open("plot.png")
vill=Image.open("vill.png")

print("每 5 秒截圖指定區域並比對... Ctrl+C 停止")
try:
    while True:
        screenshot = pyautogui.screenshot(region=search_region)
        found_at, confidence = match_template_with_transparency(screenshot, plot)

        if found_at:
            # 將區域內座標轉成螢幕座標
            screen_pos = (found_at[0] + search_region[0], found_at[1] + search_region[1])
            print(f"✅ 圖片找到於螢幕座標 {screen_pos}，信心值：{confidence:.3f}")
        else:
            print(f"❌ 沒找到，最高信心值：{confidence:.3f}")
            found_at, confidence = match_template_with_transparency(screenshot, vill)
            if found_at:
                # 將區域內座標轉成螢幕座標
                screen_pos = (found_at[0] + search_region[0], found_at[1] + search_region[1])
                print(f"✅ 圖片找到於螢幕座標 {screen_pos}，信心值：{confidence:.3f}")
                #stop thread
                gohome()
                #rstart
            else:
                print(f"❌ 沒找到，最高信心值：{confidence:.3f}")
                found_at, confidence = match_template_with_transparency(screenshot, hypi)
                if found_at:
                    # 將區域內座標轉成螢幕座標
                    screen_pos = (found_at[0] + search_region[0], found_at[1] + search_region[1])
                    print(f"✅ 圖片找到於螢幕座標 {screen_pos}，信心值：{confidence:.3f}")
                    #stop
                    tycode('/skyblock')
                    gohome()
                    #srart
                else:
                    print(f"❌ 沒找到，最高信心值：{confidence:.3f}")
                    #stop
                    pyautogui.press('esc')
                    pyautogui.click(x=950,y=550)
                    pyautogui.click(x=950,y=550)
                    time.sleep(10)
                    pyautogui.click(x=746, y=200)
                    pyautogui.click(x=746, y=200)
                    time.sleep(30)
                    tycode('/skyblock')
                    gohome()
                    #srart

            
        time.sleep(10)

except KeyboardInterrupt:
    print("已停止")
