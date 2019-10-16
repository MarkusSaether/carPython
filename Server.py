import socket
from roboclaw_3 import Roboclaw

def controller():
    conn.send(data)
    command = data.decode()
    print(command)
    if command.strip() == 'THROTTLE FORWARD':
        rc.ForwardMixed(address, 32)

    if command.strip() == 'THROTTLE REVERSE':
        rc.BackwardMixed(address, 32)

    if input() == 'c':
        conn.close()

# Windows comport name
comport = "COM5"
rc = Roboclaw(comport, 115200)

rc.Open()
address = 0x80

rc.ForwardMixed(address, 0)
rc.TurnRightMixed(address, 0)


serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('10.24.178.220', 8080))
serv.listen(5)

while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data:
            break
        from_client = data.decode()
        print (from_client.strip())
        if from_client.strip() == "HANDSHAKE":
            conn.send("HANDSHAKE\n".encode())
            #while 1:
              #  controller()
        if from_client.strip() == 'THROTTLE FORWARD':
            rc.ForwardMixed(address, 120 )
        if from_client.strip() == 'THROTTLE NEUTRAL':
            rc.ForwardMixed(address, 0)
        if from_client.strip() == 'THROTTLE REVERSE':
            rc.BackwardMixed(address, 32)

    conn.close()
    print('client disconnected')
