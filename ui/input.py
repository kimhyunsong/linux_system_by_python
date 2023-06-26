from time import sleep
import os
def custom_input():
    print("input 프로세스를 실행합니다.")
    while True:
        sleep(1)
    return

def create_custom_input():
    print("input 프로세스를 생성합니다.")
    pid = os.fork()
    if pid == 0:
        input()
        pass
    else:
        return pid
    