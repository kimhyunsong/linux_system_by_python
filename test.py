import threading
import time
import os

def disk_service_thread():
    print("disk service thread")

    while True:
        cmd = "df -h ./"
        output = os.popen(cmd, "r").read()
        print(output)
        
        time.sleep(5)  # 5초 대기

# 메인 스레드에서 스레드 생성 및 실행
if __name__ == "__main__":
    thread = threading.Thread(target=disk_service_thread)
    thread.start()

    # 메인 스레드는 계속 실행되도록 유지
    while True:
        time.sleep(1)