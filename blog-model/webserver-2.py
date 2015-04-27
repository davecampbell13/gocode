'''

Phase two: Routing + Controllers

On Modern web sites we drop the .html for things, and it is more action based.

In your browser a user would request <your site.com> + 

/ 
/about
/blog
/blog/1

1) Add two new functions index_page and about_page

2) Create a hash called urls that maps between a http request like "/" and call index_page(), 
   "/about" calls about_page()

3) Move your file reading code into both of those functions, so index_page reads index.html and
   returns that data, about_page() the same but for about.html


'''

import socket

HOST, PORT = '', 8888
VIEWS_DIR = "./views"

urls = {"/" : index_page, "/about" : about_page}

def create_string(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        string = "\n".join(lines)
        http_response = "\HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + string
        return http_response

def index_page():
	return create_string("views/index.html")

def about_page():
	return create_string("views/about.html")

def run_server():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)

 
    print 'Serving HTTP on port %s ...' % PORT
    while True:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(4096)
        split_request = request.split()
        request_verb = split_request[0]
        request_file = split_request[1]

        if not request:
            continue

        if request_file == "/favicon.ico":
            continue

        http_response = url[request_file]()
        
        client_connection.sendall(http_response)
        client_connection.close()


run_server()
