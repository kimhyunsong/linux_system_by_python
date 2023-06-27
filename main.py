from system.system_server import create_system_server
from web_server.web_server import create_web_server
from ui.gui import create_gui
from ui.input import create_custom_input
import os
import signal

def sigchldHandler(signum, frame):
    print('handler: Caught SIGCHLD')
    while True:
        try:
            # Reap child processes
            pid, status = os.waitpid(-1, os.WNOHANG)
            if pid <= 0:
                break
            print(f'handler: Reaped child {pid}')
        except OSError:
            break

print("메인함수를 시작합니다")
print("시스템 서버 프로세스 생성 함수 호출합니다")
# 시그널 핸들러 등록
signal.signal(signal.SIGCHLD, sigchldHandler)

server_pid = create_system_server()
webserver_pid = create_web_server()
input_pid = create_custom_input()
gui_pid = create_gui()

# 부모 프로세스가 자식 프로세스의 종료를 기다림
try:
    while True:
        pass
except KeyboardInterrupt:
    # 부모 프로세스에 대한 인터럽트 시그널 처리
    print("KeyboardInterrupt: 프로세스를 종료합니다.")

# 자식 프로세스들을 종료시키고 좀비 프로세스 방지
os.kill(server_pid, signal.SIGTERM)
os.kill(webserver_pid, signal.SIGTERM)
os.kill(input_pid, signal.SIGTERM)
os.kill(gui_pid, signal.SIGTERM)

_, _ = os.waitpid(server_pid, 0)
_, _ = os.waitpid(webserver_pid, 0)
_, _ = os.waitpid(input_pid, 0)
_, _ = os.waitpid(gui_pid, 0)

print("프로세스 종료")
