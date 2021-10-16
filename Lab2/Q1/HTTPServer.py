import socket


# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:    
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    try:
        # Get the content of webpage
        file_name = request.split()[1]
        if file_name == "/":
            file_name = "/index.html"
        fin = open('htdocs' + file_name)
        content = fin.read()
        fin.close()
        response = 'HTTP/1.0 200 OK\n\n' + content
    except:
        content= "<h1>Content not found</h1>"
        response = 'HTTP/1.0 404 Not Found\n\n' + content

    # Send HTTP response
    client_connection.sendall(response.encode())
    client_connection.close()