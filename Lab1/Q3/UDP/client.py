import socket as sktlib

#Create socket for client
c_conn = sktlib.socket(sktlib.AF_INET, sktlib.SOCK_DGRAM)
c_conn.bind((sktlib.gethostname(), 1501))

#Accepting client name
client_name = input("Enter client name: ")

#Sending client name
c_conn.sendto(bytes(client_name, "utf-8"), (sktlib.gethostname(), 1500))

#Accepting server name
server_name, server_addr = c_conn.recvfrom(1024)
server_name = server_name.decode("utf-8")
print(f"{server_name} is the server name.\nStart of chat")

#Start of chat
print("(Type \"Bye\" to exit chat)")

stop = False
while not stop:
    
    #Send message to server
    send_msg = input(f"{client_name}: ")
    if send_msg == "Bye":
        stop = True
    #Sending message
    c_conn.sendto(bytes(send_msg, "utf-8"), server_addr)

    if not stop:
        #Receiving message
        recv_msg, server_addr = c_conn.recvfrom(1024)
        recv_msg = recv_msg.decode("utf-8")
        print(f"{server_name}: {recv_msg}")

        if recv_msg == "Bye":
            print(f"{server_name} has exited the chat...")
            stop = True

c_conn.close()