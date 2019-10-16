import socket
from roboclaw_3 import Roboclaw

client
# Windows comport name
comport = "COM5"
rc = Roboclaw(comport, 115200)

rc.Open()
address = 0x80

rc.ForwardMixed(address, 0)
rc.TurnRightMixed(address, 0)


def connect():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("10.24.178.220", 65432))

    client.send("HANDSHAKE\n".encode())

    global from_server
    from_server = client.recv(4096)


def controller():

    command = from_server.decode()
    print(command)
    if command.strip() == 'W':
        rc.ForwardMixed(address, 32)

    if command.strip() == 'S':
        rc.BackwardMixed(address, 32)

    if input() == 'c':
        client.close()


def main():
    connect()  # connect to server
    while 1:
        controller()   # Read from server and control car


if __name__ == "__main__":
    main()






