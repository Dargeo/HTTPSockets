import requests as req
import urllib,bs4


def postTask(bucket):
    cert = req.certs.where()
    
    resp = req.post("http://100.25.117.202:5050/buckets/new", files=dict(bucket=bucket))
    print(resp.text)
    url = "http://100.25.117.202:5050"
    url_contents = urllib.request.urlopen(url).read()

    soup = bs4.BeautifulSoup(url_contents, "html.parser")
    div = soup.find("ul", {"id": "ull"})

    content = str(div)
    print(content[:50])

def removtask(bucket):
    data = {'bucket': bucket}
    print(data)
    resp = req.post("http://100.25.117.202:5050/buckets/{}/remove".format(bucket) , files=dict(bucket=bucket) )
    print(resp.text)

def main():
    nume= input('Digite el numero de lo que quiera hacer \n 1.) Añadir bucket \n 2.) Eliminar bucket\n')
    if nume == '1' :
        postTask(input("Ingrese el nombre del bucket \n"))
    elif nume == '2':
        removtask(input("Ingrese el nombre de la bucket a eliminar\n"))
    else:
        print("si\n")

if __name__ == '__main__':
    main()