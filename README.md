# Proyecto de protocolo http para topicos especiales en telematica:
    
 ### Uso de la aplicacion ###
 
 Webserver:
 `python3 webserver.py`
 Este iniciara una pagina HTML en la direccion publica de la maquina `Servidor` de AWS, que desplegara la ruta con los Buckets creados, donde se podra agregar, eliminar y ver los Buckets actuales.
 
 Client:
 `python3 client.py`
 Este iniciara un menu como cliente, que permitira lo mismo que se puede hacer en la pagina para cualquier otro usuario, pero este sera desplegado desde la terminal.


Librerias necesarias para la ejecucion:
- requests
- urllib
- bs4
- http
- cgi
- os
- shutil
