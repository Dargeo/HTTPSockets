import requests as req



def postTask(task):

    resp = req.post("http://localhost:8000/tasklist/new", files=dict(task=task))
    print(resp.text)

def removtask(task):
    data = {'task': task}
    print(data)
    resp = req.post("http://localhost:8000/tasklist/{}/remove".format(task) , files=dict(task=task) )
    print(resp.text)

def main():
    nume= input('Digite el numero de lo que quiera hacer \n 1.) Añadir task \n 2.) Eliminar Task\n')
    if nume == '1' :
        postTask(input("Ingrese el nombre del task \n"))
    elif nume == '2':
        removtask(input("Ingrese el nombre de la task a eliminar\n"))
    else:
        print("si\n")

if __name__ == '__main__':
    main()