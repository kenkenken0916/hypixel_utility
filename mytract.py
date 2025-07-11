import pyautogui
import time
import cv2
import numpy as np
from PIL import Image

# Global variables declaration
screenshot = None
found_at = None

hypi=Image.open("./pic/whereami/hypi.png")
plot=Image.open("./pic/whereami/garden.png")
vill=Image.open("./pic/whereami/vill.png")
back_to_list_img=Image.open("./pic/whereami/back_to_list.png")

# todo plot numbers pest numbers

def take_screenshot(region=None):
    global screenshot
    screenshot = pyautogui.screenshot(region=region)

def search_hypi():
    found_at, confidence = match_template_with_transparency(screenshot, hypi)
    if found_at:
        return True
    else:
        return False
    
def search_plot():
    found_at, confidence = match_template_with_transparency(screenshot, plot)
    if found_at:
        return True
    else:
        return False

def search_vill():
    found_at, confidence = match_template_with_transparency(screenshot, vill)
    if found_at and confidence > 0.9:  # Adjust confidence threshold as needed
        return True
    else:
        return False
    
def search_back_to_list():
    found_at, confidence = match_template_with_transparency(screenshot, back_to_list_img)
    if found_at:
        return True
    else:
        return False



# 子圖比對 + 支援透明遮罩
def match_template_with_transparency(screen_img, template_img, region=None):
    try:
        # 确保图片格式正确
        screen = np.array(screen_img.convert('RGB'))
        
        # 如果指定了区域，裁剪图片
        if region is not None:
            x, y, w, h = region
            screen = screen[y:y+h, x:x+w]
        
        template_rgba = template_img.convert('RGBA')
        template = np.array(template_rgba)

        # 打印图片尺寸信息
        # print(f"屏幕截图尺寸: {screen.shape}")
        # print(f"模板图片尺寸: {template.shape}")

        # 处理透明通道
        alpha = template[:, :, 3]
        mask = cv2.threshold(alpha, 1, 255, cv2.THRESH_BINARY)[1]
        
        # 转换颜色空间并确保类型正确
        screen_bgr = cv2.cvtColor(np.array(screen, dtype=np.uint8), cv2.COLOR_RGB2BGR)
        template_bgr = cv2.cvtColor(np.array(template[:, :, :3], dtype=np.uint8), cv2.COLOR_RGB2BGR)

        # # 保存调试图像 (已注释)
        # cv2.imwrite("debug_screen.png", screen_bgr)
        # cv2.imwrite("debug_template.png", template_bgr)

        # 使用 TM_SQDIFF_NORMED 方法（值越小越匹配）
        res = cv2.matchTemplate(screen_bgr, template_bgr, cv2.TM_SQDIFF_NORMED, mask=mask)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
        # 使用 TM_SQDIFF_NORMED 时，最小值才是最佳匹配
        match_val = 1.0 - min_val  # 转换为相似度分数（1最匹配，0最不匹配）
        match_loc = min_loc
        
        # print(f"匹配值: {match_val}")  # 打印匹配度
        # print(f"匹配位置: {match_loc}")
        
        # 降低阈值，增加调试信息
        if match_val >= 0.9:  # 降低阈值到0.6
            h, w = template_bgr.shape[:2]
            # # 在匹配位置画个框并保存图片 (已注释)
            # # 在框上标注匹配值 (已注释)
            # cv2.putText(screen_bgr, f"Match: {match_val:.2f}", (match_loc[0], match_loc[1]-10),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
            # cv2.imwrite("debug_match.png", screen_bgr)
            # 如果使用了区域，需要调整返回的坐标
            if region is not None:
                match_loc = (match_loc[0] + region[0], match_loc[1] + region[1])
            return match_loc, match_val
        return None, match_val
        
    except Exception as e:
        print(f"错误: {str(e)}")
        # try:
        #     # 尝试保存原始截图用于调试
        #     screen_debug = np.array(screen_img.convert('RGB'))
        #     cv2.imwrite("error_screen.png", cv2.cvtColor(screen_debug, cv2.COLOR_RGB2BGR))
        # except:
        #     print("无法保存错误截图")
        return None, 0.0

# 指定區域（例如左上角 400x300 的範圍）
search_region = (1400, 100, 519, 400)  # (left, top, width, height)


# 載入模板圖


def search_image(image,image_region):
    global screenshot, found_at
    found_at= None
    screenshot = pyautogui.screenshot(region=image_region)
    found_at, confidence = match_template_with_transparency(screenshot, image)
    if found_at:
        # 將區域內座標轉成螢幕座標
        screen_pos = (found_at[0] + image_region[0], found_at[1] + image_region[1])
        print(f"found image{image.filename} at {screen_pos} with confidence {confidence:.2f}")
        return 1
    else:
        print(f"{image.filename} not found")
        return 0


#back to list Mouse Position: (x=956, y=643) 

#region Mouse Position: (x=1435, y=166)
# Mouse Position: (x=1919, y=828)

def make_decision():
    global screenshot, found_at
    try:
        while True:
            screenshot = pyautogui.screenshot(region=search_region)
            search_htpi= search_image(hypi, search_region)
            search_plot= search_image(plot, search_region)
            search_vill= search_image(vill, search_region)
            search_back_to_list= search_image(back_to_list_img, search_region)


                
            time.sleep(10)

    except KeyboardInterrupt:
        print("已停止")

# make_decision()

