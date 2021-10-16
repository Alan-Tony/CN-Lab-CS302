import socket as sktlib

#Create socket for server
s_conn = sktlib.socket(sktlib.AF_INET, sktlib.SOCK_DGRAM)
s_conn.bind((sktlib.gethostname(), 1500))

#Input server name
server_name = input("Enter server name: ")

#Identifying client
client_name, client_addr = s_conn.recvfrom(1024)
client_name = client_name.decode("utf-8")
print(f"{client_name} has joined the chat")

#Sending server name
s_conn.sendto(bytes(server_name, "utf-8"), client_addr)

#Start of chat
print("(Type \"Bye\" to exit chat)")

stop = False
while not stop:
    
    #Receiving message
    recv_msg, client_addr = s_conn.recvfrom(1024)
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
        s_conn.sendto(bytes(send_msg, "utf-8"), client_addr)

s_conn.close()