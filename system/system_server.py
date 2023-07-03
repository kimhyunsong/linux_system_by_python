import sys 
sys.path.append('/home/ssong/.local/lib/python3.10/site-packages')
import pyprctl
from time import sleep
import os, signal, time, threading
from ctypes import *
import pyprctl
count = 0
#Threads function
def watchdog_thread():
    print("watchdog thread")
    while True:
        time.sleep(5)

def monitor_thread():
    print("monitor thread")
    while True:
        time.sleep(5)

def disk_service_thread():
    print("disk service thread")
    cmd = "df -h ./"
    
    while True:
        output = os.popen(cmd, "r").read()
        print(output)
        time.sleep(5)

def camera_service_thread():
    print("camera service thread")
    # cpp ctypes로 가져오기 실패
    lib = CDLL("/home/ssong/system_programming/system/HAL/camera_HAL.so")
    lib.toy_camera_open()
    while True:
        time.sleep(5)






def timer_expire_signal_handler(signum, frame):
    global count
    # print(f'timer_expire_signal_handler : {count}')
    count += 1

def set_timer(interval):
    # 타이머 신호 등록
    signal.signal(signal.SIGALRM, timer_expire_signal_handler)
    # 타이머 주기 설정 (초 단위)
    signal.setitimer(signal.ITIMER_REAL, interval, interval)

def system_server():
    print("system_server 프로세스 호출")



    watchdogThread = threading.Thread(target=watchdog_thread)
    monitorThread = threading.Thread(target=monitor_thread)
    diskServiceThread = threading.Thread(target=disk_service_thread)
    cameraServiceThread = threading.Thread(target=camera_service_thread)
    Threads = [watchdogThread, monitorThread, diskServiceThread, cameraServiceThread]
    for thread in Threads:
        thread.start()
    while True:
        set_timer(5)
        time.sleep(1)
    


def create_system_server():
    print("시스템 서버를 생성합니다.")
    pid = os.fork()
    if pid == 0:
        pyprctl.set_name("system_server")
        system_server()
    else:
        return pid
    
