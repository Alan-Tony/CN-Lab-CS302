import socket
from timeit import default_timer as timer

def port_scan(server_IP, port_num):
    
    #We need multiple scokets for different outgoing connections, otherwise we get the error:
    #  "A connect request was made on an already connected socket"
    #Therefore each port_scan() call creates a new socket. 
    # Instead of binding, we let the OS assign an ephemeral port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Try to connect
    try:
        s.connect((server_IP, port_num))
        s.close()
        return True

    except:
        return False


if __name__ == '__main__':

    domain = input("Enter domain of remote host: ")
    if not len(domain):
        domain = 'www.google.com'
    # Get IP address of domain
    server_IP = socket.gethostbyname(domain)

    # input range of ports
    print("Enter range of ports to scan: ")
    lo = max(int(input("Lower bound: ")), 1)
    up = max(int(input("Upper bound: ")), lo)

    start_time = timer()
    for port_num in range(lo, up+1):

        if port_scan(server_IP, port_num):
            print(f"IP : {server_IP}, port : {port_num} is OPEN")
        else:
            print(f"IP : {server_IP}, port : {port_num} is CLOSED")
    end_time = timer()

    print(f"Elapsed time: {end_time - start_time} seconds")