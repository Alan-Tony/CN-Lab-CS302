import socket as sktlib
import time

#Use the same socket
s = sktlib.socket(sktlib.AF_INET, sktlib.SOCK_STREAM)
# Connect to server
s.connect((sktlib.gethostname(), 1500))

# Receive message from server
msg = s.recv(1024)
print(msg.decode("utf-8"))

#Requesting time 5 times every 1 seconds
for i in range(5):

    #Request
    send_msg = str(0)
    s.send(bytes(send_msg, "utf-8"))

    #Receive
    recv_msg = s.recv(1024)
    recv_msg = recv_msg.decode("utf-8")
    print(f"Date & Time received from server: {recv_msg}")

    #Wait
    time.sleep(1)

# Signal end of requests
send_msg = str(1)
s.send(bytes(send_msg, "utf-8"))
