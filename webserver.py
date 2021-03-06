from http import server
from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
import os
import shutil
buckets=['bucket 1', 'bucket 2', 'bucket 3']

class requestHandler(BaseHTTPRequestHandler):

        def do_GET(self):
            if self.path.endswith('/'):
                
                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()

                output = ''
                output += '<html><body>'
                output += '<h1> Bucket List </h1>'
                output += '<h3><a href ="/bucket/new">Add new bucket</a></h3>'
                output += '<ul >'
                for item in os.listdir('Buckets'):
                    
                    output += '<li id="ull">%s<a href ="/buckets/%s/remove">X</a></li> ' % (item,item)
                    
                    
                output += '</ul>'        

                output += '</body></html>'
                self.wfile.write(output.encode())
                dirtree()


            if self.path.endswith('/new'):
                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()

                output = ''
                output += '<html><body>'
                output += '<h1> Add new bucket</h1>'

                output += '<form method ="POST" enctype="multipart/form-data" action="/buckets/new">'
                output += '<input name="bucket" type="text" placeholder="Add new bucket">'
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
                output += '<h1>Remove bucket: %s</h1>' % listIDPath.replace('%20',' ')
                output += '<form method ="POST" enctype="multipart/form-data" action="/buckets/%s/remove">' % listIDPath 
                output += '<input type="submit" value="Remove">'
                output += '<a href ="/">Cancel</a>' 
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
                   
                    new_task = fields.get('bucket')
                    if isinstance(new_task[0],str):
                        buckets.append(new_task[0])
                        if(os.path.isdir('Buckets/' + new_task[0]) == False):
                            print('Se creo el bucket:'+ new_task[0])
                            os.mkdir('Buckets/' + new_task[0])
                        
                    else:
                        buckets.append(bytes.decode(new_task[0]))
                        urla = bytes.decode(new_task[0])
                        if(os.path.isdir(('Buckets/' + urla)) == False):
                            print('Se creo el bucket:',bytes.decode(new_task[0]))
                            os.mkdir(('Buckets/' + urla))
                        
                    
                    self.send_response(301)
                    self.send_header('content-type', 'text/html')
                    self.send_header('Location','/')
                    self.end_headers()
                    

            if self.path.endswith('/remove'):
                listIDPath = self.path.split('/')[2]
                print(self.headers)
                ctype,pdict = cgi.parse_header(self.headers.get('content-type'))
                if ctype == 'multipart/form-data':
                    list_item = listIDPath.replace('%20', ' ')
                    print(list_item)
                    
                    nombre = 'Buckets/' + list_item
                    shutil.rmtree(nombre)
                    print("Se ha eliminado el bucket " + list_item)
                    print('Se elimino:',list_item)
                    self.send_response(301)
                    self.send_header('content-type', 'text/html')
                    self.send_header('Location','/')
                    self.end_headers()

def main():
    
    if(os.path.isdir('Buckets/') == False):
     os.mkdir('Buckets/')
    dirtree()
    print('Se instancio la carpeta para almacenar los buckets')
    PORT = 5050
    server_adress=('0.0.0.0',PORT)
    server = HTTPServer(server_adress,requestHandler)
    print('Server running on port %s' % PORT)

    server.serve_forever()

def dirtree():
    rootDir = "Buckets"
    for root, dirs, files in os.walk(rootDir):
        level = root.replace(rootDir, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
    for f in files:
            print('{}{}'.format(subindent, f))
if __name__ == '__main__':
    main()
