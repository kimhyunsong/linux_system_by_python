from time import sleep
import os

def create_gui():
    print("GUI 프로세스를 생성합니다.")
    pid = os.fork()
    if pid == 0:
        os.execl("/usr/bin/google-chrome-stable", "google-chrome-stable", "http://localhost:8282")
    else:
        return pid

