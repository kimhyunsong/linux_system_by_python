import os, prctl

def create_web_server():
    print("web server 프로세스를 생성합니다.")
    pid = os.fork()
    if pid == 0:
        prctl.set_name("web_server")
        os.execl("/usr/local/bin/filebrowser", "filebrowser", "-p", "8282")
    else:
        return pid

    