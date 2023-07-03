import sys 
sys.path.append('/home/ssong/.local/lib/python3.10/site-packages')
import prctl
from time import sleep
import os, signal, time, threading
from ctypes import *
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
count = 0


def receive_message(ch, method, properties, body):
    print(f'토끼의 메시지 : {body}')
channel.basic_consume(queue= 'MQ' , 
                      auto_ack= True , 
                      on_message_callback=receive_message)


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
        # output = os.popen(cmd, "r").read()
        # print(output)
        time.sleep(5)

def camera_service_thread():
    print("camera service thread")
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    # cpp ctypes로 가져오기 실패
    # lib = CDLL("/home/ssong/system_programming/system/HAL/camera_HAL.so")
    # lib.toy_camera_open()
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
        prctl.set_name("system_server")
        system_server()
    else:
        return pid
    
