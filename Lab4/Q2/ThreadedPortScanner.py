import threading
import socket
from timeit import default_timer as timer

lock = threading.Lock()
curr_port = hi = lo = 1

def port_scan(i):

    global curr_port, up, lo
    while True :

        #print(f"Entered thread {i}")

        # Get next port to scan
        lock.acquire()
        if curr_port > up:
            lock.release()
            break
        port_num = curr_port
        curr_port += 1
        lock.release()

        print(f"Thread {i} is scanning port {port_num}")

        #We need multiple scokets for different outgoing connections, otherwise we get the error:
        #  "A connect request was made on an already connected socket"
        #Therefore each port_scan() call creates a new socket. 
        # Instead of binding, we let the OS assign an ephemeral port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Try to connect
        try:
            s.connect((server_IP, port_num))
            s.close()
            print(f"IP : {server_IP}, port : {port_num} is OPEN")

        except:
            print(f"IP : {server_IP}, port : {port_num} is CLOSED")


if __name__ == '__main__':

    domain = input("Enter domain of remote host: ")
    if not len(domain):
        domain = 'www.google.com'
    # Get IP address of domain
    server_IP = socket.gethostbyname(domain)
    print(f"IP address of {domain} = {server_IP}")

    # input range of ports
    print("Enter range of ports to scan: ")
    lo = max(int(input("Lower bound: ")), 1)
    up = max(int(input("Upper bound: ")), lo)
    curr_port = lo

    num_threads = int(input("Enter number of threads: "))

    start_time = timer()
    
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=port_scan, args=(i,))
        t.daemon = True
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = timer()

    print(f"Elapsed time: {end_time - start_time} seconds")
