import socket
import time

def port_listener(ip, port_to_listen):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port_to_listen))
    server.listen(1)
    conn, addr = server.accept()
    while True:
        print('Server is listening...')
        time.sleep(5)
        data = conn.recv(1024)
        if data.lower() == b'q':
            print('\nConnection terminated')
            server.close()
            break
        print('Recieved:', data)

ip = '127.0.0.1'
port = 9090
port_listener(ip, port)