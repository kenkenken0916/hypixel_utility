import cv2
import numpy as np
import pyautogui
import os

# ==== Template 載入 ====
def load_templates(folder):
    templates = {}
    for filename in os.listdir(folder):
        if filename.endswith(".png"):
            label = os.path.splitext(filename)[0]
            path = os.path.join(folder, filename)
            img = cv2.imread(path)  # 讀取彩色圖片
            if img is not None:
                templates[label] = img
    return templates

# ==== 擷取畫面指定區域 ====
def capture_region(x, y, width, height):
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return frame


# ==== 模板比對 ====
def match_template(input_img, templates):
    best_score = -1
    best_label = None
    best_location = None
    
    for label, tmpl in templates.items():
        if input_img.shape[0] < tmpl.shape[0] or input_img.shape[1] < tmpl.shape[1]:
            continue
        res = cv2.matchTemplate(input_img, tmpl, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
        if max_val > best_score:
            best_score = max_val
            best_label = label
            best_location = max_loc  # 只儲存左上角位置
            
    return best_label, best_score, best_location

# ==== 單一模板比對 ====
def match_single_template(input_img, template):
    
    if input_img is None or template is None:
        return 0, None

    # 確保兩張圖片大小合適
    if input_img.shape[0] < template.shape[0] or input_img.shape[1] < template.shape[1]:
        return 0, None
    
    # 進行模板匹配
    res = cv2.matchTemplate(input_img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    # 計算匹配區域的中心點
    w, h = template.shape[1], template.shape[0]
    center_x = max_loc[0] + w//2
    center_y = max_loc[1] + h//2
    best_location = (center_x, center_y)
    
    return max_val, best_location  # 返回最高匹配分數和中心點位置

templates_1to8 = load_templates("./pic/pestnum")
templates_custom12 = load_templates("./pic/plotnum")

def which_plot():
    # 指定區域（例如左上角 400x300 的範圍）
    img=capture_region(1400, 100, 519, 400)
    plotlabel, plotscore, plotloc= match_template(img, templates_custom12)
    if plotlabel is not None and plotscore > 0.8:
        print(f"地塊編號匹配結果：類別：{plotlabel}，信心值：{plotscore:.2f}，位置：{plotloc}")
        return plotlabel, plotscore, plotloc
    else:
        print("未找到地塊編號")
        return None, 0.0, None

pic_garden=cv2.imread("./pic/whereami/garden.png")

def pestingarden():
    img = capture_region(1400, 100, 519, 400)
    
    if img is None or pic_garden is None:
        print("無法載入圖片")
        return -2
        
    score, loc = match_single_template(img, pic_garden)
    
    if score > 0.8 and loc is not None:  # 確保 loc 不是 None
        try:
            # 確保座標不會超出圖片範圍
            y_start = max(0, loc[1]-1)  # 不能小於 0
            y_end = min(img.shape[0], loc[1]+30)  # 不能超過圖片高度
            x_start = loc[0]
            x_end = min(img.shape[1], 1920)  # 不能超過圖片寬度
            
            # 裁切圖片
            new_img = img[y_start:y_end, x_start:x_end]
            pestlabel, pestscore,pestloc=match_template(new_img, templates_1to8)
            if pestlabel is not None and pestscore > 0.8:
                print(f"害蟲數字匹配結果：類別：{pestlabel}，信心值：{pestscore:.2f}，位置：{pestloc}")
                return pestlabel
            
        except Exception as e:
            print(f"裁切圖片時發生錯誤：{e}")
            return -3
    else:
        print("未找到花園")
        return -1



# ==== 主程式 ====
if __name__ == "__main__":
    # 範例：擷取畫面
    x, y, w, h = 960, 0, 960, 1080
    img = capture_region(x, y, w, h)

    print("=== 測試多模板匹配 ===")
    # 載入模板（兩組）

    # 多模板比對
    label1, score1, loc1 = match_template(img, templates_1to8)
    label2, score2, loc2 = match_template(img, templates_custom12)

    # 判斷結果
    print(f"害蟲數字匹配結果：類別：{label1}，信心值：{score1:.2f}，位置：{loc1}")
    print(f"地塊編號匹配結果：類別：{label2}，信心值：{score2:.2f}，位置：{loc2}")

    # 在圖片上標記找到的位置（綠色是害蟲數字，藍色是地塊編號）
    if loc1 is not None and score1 > 0.7:
        # 在左上角位置畫圓
        cv2.circle(img, loc1, 5, (0, 255, 0), 2)
        # 添加標籤
        cv2.putText(img, f"{label1}:{score1:.2f}", 
                   (loc1[0]-20, loc1[1]-10),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    if loc2 is not None and score2 > 0.7:
        # 在左上角位置畫圓
        cv2.circle(img, loc2, 5, (255, 0, 0), 2)
        # 添加標籤
        cv2.putText(img, f"{label2}:{score2:.2f}", 
                   (loc2[0]-20, loc2[1]-10),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    print("\n=== 測試單一模板匹配 ===")
    # 載入單一模板圖片
    single_template = cv2.imread("./pic/pestnum/pest1.png")  # 使用害蟲數量 1 的圖片作為範例
    location=None
    score = 0
    if single_template is not None:
        # 單一模板比對
        score, location = match_single_template(img, single_template)
        print(f"單模板偵測結果：信心值：{score:.2f}，位置：{location}")
    else:
        print("無法載入單一模板圖片")

    # 在圖片上標記找到的位置
    if loc1 is not None:
        cv2.circle(img, loc1, 5, (0, 255, 0), 2)  # 用綠色圓圈標記多模板匹配位置
    if location is not None and score > 0.7:  # 設定閾值 0.7
        cv2.circle(img, location, 5, (0, 0, 255), 2)  # 用紅色圓圈標記單模板匹配位置

    # 顯示截圖
    cv2.imshow("Captured Region", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
