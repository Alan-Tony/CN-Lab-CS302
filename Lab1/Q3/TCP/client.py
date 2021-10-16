import socket as sktlib

#Accepting client name
client_name = input("Enter client name: ")

c_conn = sktlib.socket(sktlib.AF_INET, sktlib.SOCK_STREAM)
#Connecting to the server
c_conn.connect((sktlib.gethostname(), 1500))

#Accepting server name
server_name = c_conn.recv(1024)
server_name = server_name.decode("utf-8")
print(f"{server_name} has accepted the request. Ready to chat")

#Sending client name
c_conn.send(bytes(client_name, "utf-8"))

#Server ready message
recv_msg = c_conn.recv(1024)
recv_msg = recv_msg.decode("utf-8")
print(recv_msg)
if(recv_msg != "Server is ready"):
    print("Server is not ready. Aborting...")
    c_conn.close()
    exit()

#Start of chat
print("(Type \"Bye\" to exit chat)")

stop = False
while not stop:
    
    #Send message to server
    send_msg = input(f"{client_name}: ")
    if send_msg == "Bye":
        stop = True
    #Sending message
    c_conn.send(bytes(send_msg, "utf-8"))

    if not stop:
        #Receiving message
        recv_msg = c_conn.recv(1024)
        recv_msg = recv_msg.decode("utf-8")
        print(f"{server_name}: {recv_msg}")

        if recv_msg == "Bye":
            print(f"{server_name} has exited the chat...")
            stop = True

c_conn.close()