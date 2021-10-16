import os
from threading import Thread

num_clients = int(input("Enter number of clients: "))

def create_client(port):

    command = f"python client.py --port {port}"
    os.system(f"start /wait cmd /k {command}")


threads=[]
for i in range(num_clients):
    port = 1501 + i
    thread = Thread(target=create_client, args=(port, ))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
