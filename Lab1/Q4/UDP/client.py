import socket as sktlib

from threading import Thread
import pickle
import argparse

stop = False

def receive_msgs(c_conn):

    global stop
    while not stop:
        recv_msg, server_addr = c_conn.recvfrom(1024)
        recv_msg = recv_msg.decode("utf-8")
        if recv_msg == "exit":
            print("Exiting chat...")
            stop = True
        else:    
            print(recv_msg)

def send_msgs(c_conn, client_name):

    global stop
    while not stop:
        msg = input()
        msg_dict = {"name": client_name, "msg": msg}
        send_obj = pickle.dumps(msg_dict)

        #Send the message
        c_conn.sendto(send_obj, (sktlib.gethostname(), 1500))

        if msg == "Bye":
            stop = True


#Get port number from command line
parser = argparse.ArgumentParser()
parser.add_argument("--port", help="Enter port number for client socket")
args = parser.parse_args()
port = int(args.port)

#Input client name
client_name = input("Enter client name: ")

#Create socket for client
c_conn = sktlib.socket(sktlib.AF_INET, sktlib.SOCK_DGRAM)
c_conn.bind((sktlib.gethostname(), port))

#Start receiving messages
receive_thread = Thread(target= receive_msgs, args=(c_conn, ))
receive_thread.start()
#Start sending messages
send_thread = Thread(target= send_msgs, args=(c_conn, client_name, ))
send_thread.start()

send_thread.join()
receive_thread.join()

