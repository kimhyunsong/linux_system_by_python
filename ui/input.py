from time import sleep
import os, prctl, signal, threading, time
from .command_thread import toy_loop
#Threads function
def command_thread():
    print("커맨드 입력을 시작합니다.")
    toy_loop()
    pass


def sensor_thread():
    print("camera service thread")
    while True:
        time.sleep(5000)


def segfault_handler(sig_num, sig_frame):
    caller_address = str(sig_frame)
    if sig_num == signal.SIGSEGV:
        print(f"signal {sig_num} ({signal.strsignal(sig_num)}), address is {sig_frame} from {caller_address}")
    else:
        print(f"signal {sig_num} ({signal.strsignal(sig_num)})")
    exit(1)



def custom_input():
    print("input 프로세스를 실행합니다.")
    commandThead = threading.Thread(target=command_thread)
    sensorThead = threading.Thread(target=sensor_thread)
    Threads = [commandThead, sensorThead]
    for thread in Threads:
        thread.start()

    signal.signal(signal.SIGSEGV, segfault_handler)
    while True:
        sleep(1)
    return

def create_custom_input():
    print("input 프로세스를 생성합니다.")
    prctl.set_name("input")
    pid = os.fork()
    if pid == 0:
        custom_input()
        pass
    else:
        return pid
    