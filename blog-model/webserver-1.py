'''

Build out a webserver.


The code below will accept and return basic http requests.

After starting the script you can test it out by going to http://localhost:8888/ in your browser.

In the terminal you will see a response like this.

GET /favicon.ico HTTP/1.1
Host: localhost:8888
Connection: keep-alive
Accept: */*
....
....


The first line of the http verb (action) and the desired file.

Second part of the first line is the file or resource requested.

After that is the body of the request.

**** Test your code after each step ****

Phase one: Basic web server

1) Extend the program by parsing the http request (request) to parse out the http verb from the request. The verb is the first part of the first line. 

Lines are seperated by \r\n so recommend using .split('\r\n')

2) Extend webserver to be able to get the file for request. The second part of the first line.

3) Create a directory called views

4) In views create two new files index.html and about.html

5) Enter some basic html into those two files.

6) Using the filename filter out /favicon.ico requests

7) If a request comes in for "/" return views/index.html file data

8) If a request comes in for "/about.html" return the data in views/about.html

'''


import socket


HOST, PORT = '', 8888
VIEWS_DIR = "./views"

def create_string(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        string = "\n".join(lines)
        http_response = "\HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + string
        return http_response

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
        print split_request
        request_verb = split_request[0]
        request_file = split_request[1]
        print request_verb
        print request_file

        if request_file == "/favicon.ico":
            continue

        if request_file == "/":
            http_response = create_string("views/index.html")

        if request_file == "/about":
            http_response = create_string("views/about.html")

        if not request:
            continue

        client_connection.sendall(http_response)
        client_connection.close()


run_server()
