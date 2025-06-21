import os

def list_and_run_scripts():
    # 取得當前目錄下的所有 Python 腳本 (.py)
    scripts = [f for f in os.listdir() if f.endswith(".py")]

    if not scripts:
        print("當前目錄沒有 Python 腳本！")
        return

    last_choice = None  # 記錄上次選擇的腳本索引

    while True:
        if last_choice is None:  # 第一次必須選擇腳本
            print("\n可選擇的腳本:")
            for i, script in enumerate(scripts):
                print(f"{i + 1}. {script}")
        
        print("0. 退出")
        print("1. 重新選擇腳本")
        
        # 提示輸入
        choice = input("請選擇腳本 (輸入數字，Enter 執行上次選擇的腳本): ").strip()

        if choice == "0":  # 退出1
            print("退出選單。")
            break
        elif choice == "1" or (last_choice is None):  # 重新選擇腳本
            try:
                choice = int(input("請選擇要執行的腳本 (輸入數字): ").strip())
                if 1 <= choice <= len(scripts):
                    last_choice = choice - 1  # 記錄選擇的腳本索引
                else:
                    print("選擇錯誤！請選擇有效數字。")
                    continue
            except ValueError:
                print("請輸入有效的數字！")
                continue
        elif choice == "":  # 直接按 Enter
            if last_choice is None:
                print("尚未選擇任何腳本！請先選擇。")
                continue
        else:
            print("無效輸入，請輸入數字 (0, 1 或 Enter)")
            continue

        # 執行選擇的腳本
        print(f"正在執行腳本: {scripts[last_choice]}")
        os.system(f"sudo python \"{scripts[last_choice]}\"")

if __name__ == "__main__":
    list_and_run_scripts()
