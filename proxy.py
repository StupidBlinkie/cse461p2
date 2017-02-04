import socket
import sys
import threading


def handle(conn_tcp, addr_tcp):

    print "a new connection is created, ", addr_tcp 

    request = conn_tcp.recv(1024)
    print request

    ###get web server and port (host line)
    request_lines = request.split("\n");    #split each line
    server_line_str = request_lines[1].replace(" ","").lower()  #strip out whitespace
    server_index = server_line_str.find("host:") + 5

    server_str = '%s' % server_line_str[server_index:] 
    print server_str

    port = 0
    if (server_str.find(":") > 0):
        port = server_str[server_str.find(":"):] #find port in second line
    else:
        if (request_lines[0].lower().find("https://") > 0):
            port = 443
        else:
            port = 80

    # server_str = server_str + ':' + str(port)  #??BUGGY--appeding to fornt?????
    # print server_str
        

    ###Turning off keep-alive
    request = request.replace("Connection: keep-alive", "Connection: close")
    #print request

    print "<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>"



    ###establish tcp connection to server
    # tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # tcp_socket.coonet((server_str, port))





if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print "usage: proxy <port>"
        sys.exit(1)


    host = ''
    port = int (sys.argv[1])

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((host, port))
    tcp_socket.listen(100)



    while True:
        conn_tcp, addr_tcp = tcp_socket.accept()

        tcp_thread = threading.Thread(target=handle, args=(conn_tcp, addr_tcp))
        tcp_thread.daemon = True
        tcp_thread.start()





# ref:  http://luugiathuy.com/2011/03/simple-web-proxy-python/

# question: when opening one site, multiple connections are created. 





# POST http://clients1.google.com/ocsp HTTP/1.1
# Host: clients1.google.com
# User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate
# Content-Length: 75
# Content-Type: application/ocsp-request
# Connection: keep-alive
