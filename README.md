# SEPOMEX-API
API para consultar los CP de México.


## Despliegue de la aplicación

Aquí depende de donde se vaya a desplegar el proyecto. Ya sea un servidor vps como _Digital Ocean_, _AWS_, entre otros. U otros servidore que ya esten preconfigurados como _Heroku_

Para el caso de **Heroku**

Se tiene que tener instalado el CLI de heroku y desde ahi se manipula todo el servidor(es importante tener Git tambien). Es necesario usar una base de datos PostgreSQL que en este caso Heroku facilida la integración de la base de datos proporcionando así los datos de configuración. Aquí se tiene la facilidad de pasarle los datos confidentiales por medio de variables de entorno.
Se tiene que organizar un archivo llamado _Procfile_ con los comandos que el servidor va a correr. Aqui se integra _unicorn_ para servir los archivos.

Al hacer push al repositorio de Heroku, este automaticamente detecta el lenguaje de programación y lo instala en el servidor, posteriormente, por medio de pip instala lo que encuentre en la archivo _requirements.txt_ y al final ejecuta el archivo procfile donde el servidor se activa(es importante que para este punto, se haya cambiado la condiguración de modo de producción)


