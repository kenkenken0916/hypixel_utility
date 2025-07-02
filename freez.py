import os
import time

def find_minecraft_pid():
    lines = os.popen("pgrep -fa java").read().splitlines()
    for line in lines:
        if "net.minecraft.client.main.Main" in line or "BLClient" in line or "badlion" in line.lower():
            parts = line.strip().split(None, 1)
            print(f"找到：{line}")
            return int(parts[0])
    return None

def freeze(pid):
    print(f"暫停 Minecraft (PID={pid})")
    os.system(f"kill -STOP {pid}")

def unfreeze(pid):
    print(f"恢復 Minecraft (PID={pid})")
    os.system(f"kill -CONT {pid}")

def main():
    pid = find_minecraft_pid()
    if not pid:
        print("❌ 找不到 Minecraft 進程")
        return

    freeze(pid)
    print("Sleep 10 秒（此時 Minecraft 完全凍結）")
    time.sleep(10)
    unfreeze(pid)

if __name__ == "__main__":
    main()
