from system.system_server import system_server, create_system_server
from web_server.web_server import create_web_server
from ui.gui import create_gui
from ui.input import create_custom_input

print("메인함수를 시작합니다")
print("시스템 서버 프로세스 생성 함수 호출합니다")
server_pid = create_system_server()
webserver_pid = create_web_server()
input_pid = create_custom_input()
gui_pid = create_gui()

print (server_pid, webserver_pid, input_pid, gui_pid)