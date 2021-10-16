import socket as sktlib
from threading import Thread

S_conn=sktlib.socket(sktlib.AF_INET, sktlib.SOCK_STREAM)
#S_conn.setsockopt(sktlib.SOL_SOCKET, sktlib.SO_REUSEADDR, 1)
S_conn.bind((sktlib.gethostname(),1500))
S_conn.listen(15)

client_conns=[]
names=[]

def clients_conn(C_conn, client_name):

    stop = False
    while not stop:

        client_message = C_conn.recv(1024)
        client_message = client_message.decode("utf-8")

        if len(client_message):

            if client_message == "Bye":
                C_conn.send(bytes("exit", "utf-8")) # For receive_msgs thread on client side to exit
                stop = True

            send_msg = f"{client_name}: {client_message}"
            Send_to_all_clients(send_msg, C_conn)

        if stop:
            print(f"{client_name} has left the chat")
            client_conns.remove(C_conn)

def Send_to_all_clients(send_msg, conn):

    for send_conn in client_conns:

        if send_conn!=conn:
            send_conn.send(bytes(send_msg, "utf-8"))


if __name__ == '__main__':

    while True:

        #Accept connection
        C_conn, C_IP = S_conn.accept()        
        print(f"Client with IP address {C_IP} has joined the chat")
        C_conn.send(bytes("Welcome to the chatroom", "utf-8"))

        #Receive client name
        client_name = C_conn.recv(1024)
        client_name = client_name.decode("utf-8")
        names.append(client_name)

        t = Thread(target= clients_conn, args= (C_conn, client_name, ))
        t.start()

        client_conns.append(C_conn)

            






