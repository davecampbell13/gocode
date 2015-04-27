'''

Phase three: Templating

Templating allows a program to replace data dynamically in an html file. 

Ex: A blog page, we wouldn't write a whole new html file for every blog page. We want to write
the html part, and styling just once, then just inject the different blog data into that page. 


1) Add the following line to index.html in the body

<h2>###Title###</h2>

2) When a request come in for index (/)
   
   - read the file data for index.html 

   - change the ###Title### string to the string "This is templating"
  
   - return the changed html 

3) Write a function render_template to take an html template, and a hash context

   Ex: render_template("<html>...",{"Title":"This is templating"})

   - Render will the try to replace all the fields in that hash

   Ex: context = {"Title":"This is the title","BlogText":"this is blog data"}

   In the html template replace ###Title### and ###BlogText### with corresponding key values.

   - Test by using this context {"Title":"This is the title","BlogText":"this is blog data"}

4) Add render_template to index_page with the sample context above

'''
import socket

HOST, PORT = '', 8888
VIEWS_DIR = "./views"

def create_string(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        string = "\n".join(lines)
        html = "\HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + string
        return html

def render_string(html_string, context):
	print context
	new_html = html_string
	for i in context:
		new_html = new_html.replace("###" + i + "###", context[i])
	return new_html

def index_page():
	context = {
	"Title":"Welcome to the Home Page",
	"BlogText":"This is the home page content."}
	html_string = create_string("views/index.html")
	new_html = render_string(html_string, context)
	return new_html

def about_page():
	context = {
	"Title":"About Page",
	"BlogText":"This is about page data"}
	html_string = create_string("views/about.html")
	new_html = render_string(html_string, context)
	return new_html

def page_404():
	return create_string("views/404.html")

urls = {"/" : index_page, "/about" : about_page}

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
            page_404()

        if request_file == "/favicon.ico":
            continue

        http_response = urls[request_file]()
        
        client_connection.sendall(http_response)
        client_connection.close()


run_server()

