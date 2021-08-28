from http import server
from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi

tasklist=['Task 1', 'Task 2', 'Task 3']

class requestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path.endswith('/'):
                
                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()

                output = ''
                output += '<html><body>'
                output += '<h1> task List </h1>'
                output += '<h3><a href ="/tasklist/new">Add new task</a></h3>'
                for task in tasklist:
                    output += task   
                    output += '<a href ="/tasklist/%s/remove">X</a>' % task
                    output += '</br>'

                output += '</body></html>'
                self.wfile.write(output.encode())

            if self.path.endswith('/new'):
                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()

                output = ''
                output += '<html><body>'
                output += '<h1> Add new Task</h1>'

                output += '<form method ="POST" enctype="multipart/form-data" action="/tasklist/new">'
                output += '<input name="task" type="text" placeholder="Add new task">'
                output += '<input type="submit" value="Add">'
                output += '</form>'
                output += '</body></html>'

                self.wfile.write(output.encode())

            if self.path.endswith('/remove'):
                listIDPath = self.path.split('/')[2]
                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()
                output = ''
                output += '<html><body>'
                output += '<h1>Remove task: %s</h1>' % listIDPath.replace('%20',' ')
                output += '<form method ="POST" enctype="multipart/form-data" action="/tasklist/%s/remove">' % listIDPath 
                output += '<input type="submit" value="Remove">'
                output += '<a href ="/tasklist">Cancel</a>' 
                output += '</body></html>'
                self.wfile.write(output.encode())

        def do_POST(self):
            if self.path.endswith('/new'):
                ctype,pdict = cgi.parse_header(self.headers.get('content-type'))
                pdict['boundary'] = bytes(pdict['boundary'],"utf-8")
                content_len = int(self.headers.get('Content-length'))
                pdict['CONTENT-LENGTH'] = content_len
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    new_task = fields.get('task')
                    tasklist.append(new_task[0])
                    print('Se agrego:',new_task[0])
                    self.send_response(301)
                    self.send_header('content-type', 'text/html')
                    self.send_header('Location','/')
                    self.end_headers()
                    print('La informacion es:')
                    for i in range(0,len(tasklist)):
                        print(tasklist[i])

            if self.path.endswith('/remove'):
                listIDPath = self.path.split('/')[2]
                ctype,pdict = cgi.parse_header(self.headers.get('content-type'))
                if ctype == 'multipart/form-data':
                    list_item = listIDPath.replace('%20', ' ')
                    tasklist.remove(list_item)
                    print('Se elimino:',list_item)
                    self.send_response(301)
                    self.send_header('content-type', 'text/html')
                    self.send_header('Location','/')
                    self.end_headers()
                    print('La informacion es:')
                    for i in range(0,len(tasklist)):
                        print(tasklist[i])
def main():
    PORT = 8000
    server_adress=('localhost',PORT)
    server = HTTPServer(server_adress,requestHandler)
    print('Server running on port %s' % PORT)
    print('La informacion es:',)    
    for i in range(0,len(tasklist)):
        print(tasklist[i])
    server.serve_forever()


if __name__ == '__main__':
    main()