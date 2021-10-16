import socket
from threading import Thread

#Global variable to indicate whether client has exited or not
stop = False
client_name=""

def receive_msgs(C_conn):

    global stop
    while not stop:

        recv_msg = C_conn.recv(1024)
        recv_msg = recv_msg.decode("utf-8")
        if recv_msg == "exit":
            print("Exiting chat...")
            stop = True
        else:    
            print(recv_msg)

    print("Exiting receive_msgs")

def send_msgs(C_conn):

    global stop
    while not stop:

        send_msg = input()
        C_conn.send(bytes(send_msg, "utf-8"))

        if send_msg == "Bye":
            stop = True

    print("Exiting send_msgs")

if __name__ == '__main__':

    #Create socket
    C_conn=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connect to server
    C_conn.connect((socket.gethostname(),1500))

    #Get welcome message
    welcome_msg = C_conn.recv(1024)
    welcome_msg = welcome_msg.decode("utf-8")
    print(welcome_msg)

    #Send client name
    client_name = input("Enter client name: ")
    C_conn.send(bytes(client_name, "utf-8"))

    #Start receiving messages
    receive_thread = Thread(target= receive_msgs, args=(C_conn, ))
    receive_thread.start()
    #Start sending messages
    send_thread = Thread(target= send_msgs, args=(C_conn, ))
    send_thread.start()

    send_thread.join()
    receive_thread.join()




