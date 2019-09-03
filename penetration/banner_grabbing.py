import socket

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0800))
# s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

target_host = str(input("Enter the host name: "))
# target_host = "https://www.python.org/"
target_port = int(input("Enter port: "))
# target_port = 443
s.connect((target_host, target_port))


def garb(s, sock=None):
    try:
        s.send('GET HTTP/1.1 \r\n')
        ret = sock.recv(1024)
        print('[+]' + str(ret))
        return
    except Exception as error:
        print('[-]' + "Not information grabbed: " + str(error))
        return
