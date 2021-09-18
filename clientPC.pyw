from time import sleep as pause
import socket
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()


def enter_command():
    command = s.recv(1024)
    command = command.decode()
    if command.lower() == "shutdown":
        print("Shutdown command received")
        s.send("shutdown".encode())
        pause(3)
        os.system("shutdown /s /f")
    elif command.lower() == "sleep":
        print("Sleep command received")
        s.send("sleep".encode())
        pause(3)
        os.system("shutdown /f /h")
    elif command.lower() == "test":
        print("test command received")
        s.send("test".encode())
        pause(1)
        enter_command()
    elif command.lower() == "exit":
        print("exit command received")
        s.send("exit".encode())
        pause(2)
        establish_connection()
    else:
        print("failed to execute the command")
        s.send("error".encode())
        pause(1)
        enter_command()


def establish_connection():
    global s
    s = socket.socket()
    host = "192.168.178.22"
    port = 8080
    connected = False
    while not connected:
        try:
            s.connect((host, port))
            connected = True
            clear()
            print("Connected to Remote")
            enter_command()
        except:
            print("attempting to connect...")
            pass


if __name__ == '__main__':
    print("client running...")
    establish_connection()
