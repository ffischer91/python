import socket

UDP_IP = "fe80::cafe:2%enx00e04c13590c"#fe80::302:45ff:fe19:0"#%enx00e04c13590c"  # localhost
UDP_PORT = 8809
MESSAGE = "Hello, from python!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

try:
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) # UDP
except socket.error , msg:
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print "Socket open"

try:
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
except socket.error , msg:
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
print "Send!"
