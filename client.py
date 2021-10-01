import requests as req
import urllib,bs4


def postTask(bucket):
    req.certs.where()
    req.post("http://100.25.117.202:5050/buckets/new", files=dict(bucket=bucket))
    print("Se ha agregado el bucket " + bucket + " \n\n")

def removtask(bucket):
    data = {'bucket': bucket}
    
    resp = req.post("http://100.25.117.202:5050/buckets/{}/remove".format(bucket) , files=dict(bucket=bucket) )
    print("Se ha eliminado el bucket " + data + " \n\n ")

def main():
    res =""
    while res != 3:
        url = "http://100.25.117.202:5050"
        url_contents = urllib.request.urlopen(url).read()
        soup = bs4.BeautifulSoup(url_contents, "html.parser")
        div = soup.find_all('li', id="ull")
        print("Lista de buckets: \n")
        for d in div:
            print(d.string+ " \n")

        res= input('Digite el numero de lo que quiera hacer \n 1.) Añadir bucket \n 2.) Eliminar bucket\n 3.) Cerrar\n')
        if res == '1' :
            postTask(input("Ingrese el nombre del bucket \n"))
        elif res == '2':
            removtask(input("Ingrese el nombre de la bucket a eliminar\n"))
        elif res == '3':
            break

if __name__ == '__main__':
    main()