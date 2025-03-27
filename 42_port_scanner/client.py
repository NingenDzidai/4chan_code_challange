import socket

def port_sendmessage(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Connecting to', ip, ':', port)
    sock.connect((ip, port))
    while True:
        message = input('Send message to port ').encode()
        print(message)
        sock.send(message)
        if message == b'q':
            sock.close()
            break

ip = '127.0.0.1'
port = 9090
port_sendmessage(ip, port)