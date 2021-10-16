import socket as sktlib
import pickle

#Input server name
server_name = input("Enter server name: ")

#Create set to store client addresses
clients = set()

#Create socket for server
s_conn = sktlib.socket(sktlib.AF_INET, sktlib.SOCK_DGRAM)
s_conn.bind((sktlib.gethostname(), 1500))

stop = False
while True:

    #Receive from client
    recv_msg, client_addr = s_conn.recvfrom(1024)
    #Add client to the set of clients
    clients.add(client_addr)

    #The messages are sent to the server in the format of a dictionary 
    #{"msg" : msg_from_client, "name" : name_of_client}
    msg_dict = pickle.loads(recv_msg)

    #Exit of client
    if msg_dict["msg"] == "Bye":

        stop = True
        #Announce exit of client
        client_name = msg_dict["name"]
        exit_msg = f"{client_name} has left the chatroom"


    #Broadcast to other known clients
    for receiver in clients:
        if receiver != client_addr:
            #To prevent stopping client to receive messages
            msg = "{0} : {1}".format(msg_dict["name"],  msg_dict["msg"])
            if msg == "exit":
                msg = "(exit)"

            s_conn.sendto(bytes(msg, "utf-8"), receiver)

            if stop:
                s_conn.sendto(bytes(exit_msg, "utf-8"), receiver)

    #Remove client
    if stop:
        print(exit_msg)
        s_conn.sendto(bytes("exit", "utf-8"), client_addr)
        clients.remove(client_addr)
        stop = False
            

    


