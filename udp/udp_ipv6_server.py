import socket
import sys  
import datetime
import time

UDP_IP = "" # = 0.0.0.0 u IPv4 fe80::cafe:2%enx00e04c13590c
UDP_PORT = 5555
MESSAGE = "Hello, from python!"
UDP_PORT_DEST = 8809

try:
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) # UDP
except socket.error , msg:
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
try:
    sock.bind((UDP_IP, UDP_PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    print "received from:", addr
    sock.sendto(MESSAGE, (addr[0], UDP_PORT_DEST, 0,5))
    sock.sendto(MESSAGE, (addr[0], UDP_PORT_DEST, 0,5))
    sock.sendto(MESSAGE, (addr[0], UDP_PORT_DEST, 0,5))
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print "send message 3-times:", data, st
