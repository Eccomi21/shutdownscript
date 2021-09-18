import time
import socket
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()


def host_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = "192.168.178.22"
    port = 8080
    s.bind((host, port))
    print("waiting for EDVA")
    s.listen(1)
    global conn
    conn, addr = s.accept()
    print(addr, "Has connected to Remote")
    send_command()


def send_command():
    command = input(str("Command: "))
    conn.send(command.encode())
    print("Command has been sent. Waiting for confirmation")

    data = conn.recv(1024)
    data = data.decode()

    if data == "shutdown":
        print("shutdown command received and executed")
    elif data == "sleep":
        print("sleep command received and executed")
    elif data == "test":
        print("test command received and executed")
        send_command()
    elif data == "exit":
        print("exit command received and executed")
        exit(0)
    elif data == "error":
        print("some shit occurred, check client")
        send_command()


if __name__ == '__main__':
    print("server running...")
    time.sleep(1)
    host_server()