from time import sleep
import os, signal, threading, time #prctl,
import sys 
sys.path.append('/home/ssong/.local/lib/python3.10/site-packages')
import pyprctl
from command_thread import toy_loop, global_message
# from rpython.rlib import rthread
mutex = threading.Lock()
#Threads function

def command_thread():
    print("커맨드 입력을 시작합니다.")
    toy_loop()
    return


def sensor_thread():
    print("camera service thread")
    global global_message
    while True:
        #?????
        mutex.acquire()
        for i in range(len(global_message)):
            print(global_message[i])
            time.sleep(1)

        mutex.release()
        time.sleep(1)


def segfault_handler(sig_num, sig_frame):
    caller_address = str(sig_frame)
    if sig_num == signal.SIGSEGV:
        print("signal {} ({}), address is {} from {}".format(sig_num,signal.strsignal(sig_num), sig_frame, caller_address))
    else:
        print("signal {} ({})".format(sig_num, signal.strsignal(sig_num)))
    exit(1)



def custom_input():
    print("input 프로세스를 실행합니다.")
    signal.signal(signal.SIGSEGV, segfault_handler)
    commandThead = threading.Thread(target=command_thread)
    sensorThead = threading.Thread(target=sensor_thread)
    Threads = [commandThead, sensorThead]
    for thread in Threads:
        thread.start()
    for thread in Threads:
        thread.join()
    
    while True:
        sleep(1)

def create_custom_input():
    print("input 프로세스를 생성합니다.")
    pyprctl.set_name("input")
    pid = os.fork()
    if pid == 0:
        custom_input()
    else:
        return pid
    