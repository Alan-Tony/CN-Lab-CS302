import socket as sktlib

s_conn = sktlib.socket(sktlib.AF_INET, sktlib.SOCK_STREAM)
s_conn.bind((sktlib.gethostname(), 1500))           
s_conn.listen(1)

#Accepting server name
server_name = input("Enter server name: ")

#Accepting client conection
c_conn, c_IP = s_conn.accept()
#Sending server name
c_conn.send(bytes(server_name, "utf-8"))

client_name = c_conn.recv(1024)
client_name = client_name.decode("utf-8")
print(f"{client_name} has joined the chat")

#Start of chat
print("(Type \"Bye\" to exit chat)")

# Tell client that the server is ready to chat
send_msg = "Server is ready"
c_conn.send(bytes(send_msg, "utf-8"))

stop = False
while not stop:
    
    #Receiving message
    recv_msg = c_conn.recv(1024)
    recv_msg = recv_msg.decode("utf-8")
    print(f"{client_name} : {recv_msg}")

    if recv_msg == "Bye":
        print(f"{client_name} has exited the chat...")
        stop = True    
    
    if not stop:
        #Sending message
        send_msg = input(f"{server_name}: ")
        if send_msg == "Bye":
            stop = True
        c_conn.send(bytes(send_msg, "utf-8"))

s_conn.close()