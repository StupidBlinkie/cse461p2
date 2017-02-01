import socket
import sys


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print "usage: proxy <port>"
        sys.exit(1)


    host = ''
    port = int (sys.argv[1])

    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.bind((host, port))
        tcp_socket.listen(1)

    except socket.error :
        sys.exit(1)


    #while 1:
    conn_tcp, addr_tcp = tcp_socket.accept()












# ref:  http://luugiathuy.com/2011/03/simple-web-proxy-python/
