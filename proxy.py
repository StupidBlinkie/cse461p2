import socket
import sys
import threading


def handle(conn_tcp, addr_tcp):

    print "a new connection is created, ", addr_tcp 
    conn_tcp.settimeout(30)

    try:
        request = conn_tcp.recv(1024)
        print request

    except socket.timeout:
        print "timeout"
        conn_tcp.close()






if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print "usage: proxy <port>"
        sys.exit(1)


    host = ''
    port = int (sys.argv[1])

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((host, port))
    tcp_socket.listen(10)



    while True:
        conn_tcp, addr_tcp = tcp_socket.accept()

        tcp_thread = threading.Thread(target=handle, args=(conn_tcp, addr_tcp))
        tcp_thread.daemon = True
        tcp_thread.start()





# ref:  http://luugiathuy.com/2011/03/simple-web-proxy-python/
