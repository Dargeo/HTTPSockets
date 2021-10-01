import requests as req



def postTask(bucket):
    cert = req.certs.where()
    
    resp = req.post("http://54.83.172.18:5050/tasklist/new", files=dict(bucket=bucket))
    print(resp.text)

def removtask(bucket):
    data = {'bucket': bucket}
    print(data)
    resp = req.post("http://54.83.172.18:5050/tasklist/{}/remove".format(bucket) , files=dict(bucket=bucket) )
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