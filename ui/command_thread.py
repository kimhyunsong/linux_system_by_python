import os, threading, pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# from rpython.rlib import rthread
mutex = threading.Lock()
global_message =''

def toy_send(args):
    print("send message:", args[1])
    return 1

def toy_message_queue(args):
    if args[1] == "camera":
        msg_type = args[2]
        channel.basic_publish(exchange='',
                      routing_key='MQ',
                      body=msg_type)
        # connection.close()
    return 


def toy_exit(args):
    return 0

def toy_mutex(args):
    mutex.acquire()
    global global_message
    global_message = args[1]
    mutex.release()
    return 1

def toy_shell(args):
    pid = os.fork()
    if pid == 0:
        os.execvp(args[0], args)
        # sys.exit(os.EXEC_FAILURE)
    elif pid < 0:
        print("toy:", os.strerror(os.errno))
    else:
        while True:
            try:
                _, status = os.waitpid(pid, 0)
                if os.WIFEXITED(status) or os.WIFSIGNALED(status):
                    break
            except OSError as e:
                print("toy:", os.strerror(e.errno))
    return 1


def toy_execute(args):
    if not args:
        return 1
    for i in builtin_str:
        if i == args[0]:
            return builtin_func[i](args)
    return 1


def toy_read_line():
    line = input("TOY>")
    return line

def toy_split_line(line):
    tokens = line.split()
    return tokens


def toy_loop():
    while True:
        line = toy_read_line()
        args = toy_split_line(line)
        status = toy_execute(args)
        if not status:
            break

builtin_str = ["send", "sh", "exit", "mu", "mq"]

builtin_func = {
    "send": toy_send,
    "sh": toy_shell,
    "exit": toy_exit,
    "mu": toy_mutex,
    "mq" : toy_message_queue
}

