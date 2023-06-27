from time import sleep
import os, prctl, signal, time

count = 0
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

    while True:
        set_timer(5)
        time.sleep(5000)
    return


def create_system_server():
    print("시스템 서버를 생성합니다.")
    pid = os.fork()
    if pid == 0:
        prctl.set_name("system_server")
        system_server()
    else:
        return pid
    
