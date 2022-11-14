import socket
import sys
from threading import Thread
import time


port = int(sys.argv[1])

commands = {
    "0": "date",
    "1": "uptime",
    "2": "free -m",
    "3": "netstat",
    "4": "w",
    "5": "ps"
}

starts = []
ends = []
times = []


def main():
    handle_input()


def handle_input():
    choice = " "
    while choice != "q":
        print("Input a command number from below or input q to quit:")
        for k, v in commands.items():
            print(k, v)

        choice = str(input())

        if choice == "q":
            send_request("q")
            break

        choice = commands[choice]

        print("How many times would you like to execute this command?")

        amount = int(input())
        generate_threads(amount, choice)


def send_request(command):
    # host = "139.62.210.155"
    host = socket.gethostname()

    client_socket = socket.socket()
    client_socket.connect((host, port))

    client_socket.send(command.encode())
    start = time.perf_counter()
    starts.append(start)
    data = client_socket.recv(1024).decode()
    stop = time.perf_counter()
    ends.append(stop)
    client_socket.close()
    # times.append(stop - start)
    print(data)


def dummy_thread(command):
    print(command)


def generate_threads(amount, comamnd):
    threads = []
    for n in range(amount):
        t = Thread(target=send_request, args=(comamnd,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    for i in range(len(starts)):
        times.append(ends[i]-starts[i])

    time_stats(amount)
    times.clear()
    starts.clear()
    ends.clear()


def time_stats(amount):

    for i in range(len(times)):
        print("Thread " + str(i) + " took " + str(times[i]))

    print("Total time : " + str(sum(times)))
    print("Average time : " + str(sum(times)/amount))
    print()


main()
