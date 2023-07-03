from time import sleep
import os
import sys 
sys.path.append('/home/ssong/.local/lib/python3.10/site-packages')
import pyprctl

def create_gui():
    print("GUI 프로세스를 생성합니다.")
    pid = os.fork()
    if pid == 0:
        pyprctl.set_name("gui")
        os.execl("/usr/bin/google-chrome-stable", "google-chrome-stable", "http://localhost:8282")
    else:
        return pid

