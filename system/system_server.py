from time import sleep
import os
def system_server():
    print("system_server 프로세스 호출")
    while True:
        sleep(1)
    return


def create_system_server():
    print("시스템 서버를 생성합니다.")
    pid = os.fork()
    if pid == 0:
        system_server()
    else:
        return pid
    
