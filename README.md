# SEPOMEX-API
API para consultar los CP de México.


## Despliegue de la aplicación

Depende de donde se vaya a desplegar el proyecto. Ya sea un servidor vps como _Digital Ocean_, _AWS_, entre otros. U otros servidores que ya esten preconfigurados como _Heroku_

### Para el caso de **Heroku**

Se tiene que tener instalado el CLI de heroku y desde ahi se manipula todo el servidor(es importante tener Git tambien). Es necesario usar una base de datos PostgreSQL que en este caso Heroku facilida la integración de la base de datos proporcionando así los datos de configuración. Aquí se tiene la facilidad de pasarle los datos confidentiales por medio de variables de entorno.
Se tiene que organizar un archivo llamado _Procfile_ con los comandos que el servidor va a correr. Aqui se integra _unicorn_ para servir los archivos.

Al hacer push al repositorio de Heroku, este automaticamente detecta el lenguaje de programación y lo instala en el servidor, posteriormente, por medio de pip instala lo que encuentre en la archivo _requirements.txt_ y al final ejecuta el archivo procfile donde el servidor se activa(es importante que para este punto, se haya cambiado la condiguración de modo de producción)

### Para el caso de un **VPS** 

Aqui se tiene que considerar que se tiene una maquina (generalmente _Unix_) desde cero. Por lo que hay que configurar cada servicio por separado; como instalar las bases de datos que se vayan a utilizar, los lenguages de programación que se vayan a usar, _Git_, instalación de dependencias, etc. Para poder usar este servidor se tiene que establecer una comunicación por **SSH** a la ip (maquina) que nos proporcionan, por este medio es que podremos interactuar con el sistema mediante el uso de la consola. 

Aqui se tiene que hacer un pull de los archivos que esten en el proyecto y para estos servidores, ademas de incluir _Unicorn_, se debe instalar un servidor web (en mi caso, yo conozco nginx), al cual se le agrega un archivo de comandos y servicios que tendrá este. Se configuran tanto los puertos internos como los externo de donde se haran las consultas de los clientes por medio del navegador y se cambia el proyecto con las configuraciones de producción.



## CI/CD

Este es un archivo que facilita toda la construcción del contenedor de _Docker_, testing(he usado pytest) y la subida a producción. En este se debe incluir cada _job_. Estas instrucciones se llevarán a cabo cada vez que se haga un push al repositorio, por lo que aquí se automatizan estos procesos. Es un archivo _.yml_ que como en docker-compose se tiene que indicar que servicios se realizarán y si dependen de otros para ejecutarse. En este caso yo lo he hecho con GitHub y aquí se introduce claves secretas o incluso entornos donde se almacena toda una serie de configuraciónes. Todas estas se utilizan para no dejar a la vista información sensible que pueda vulnerar la seguridad del proyecto. 

Entonces, cada vez que se hace un push al repositorio, enseguida reconstruye el contenedor de la aplicación en _Docker_ y la actualiza en el repositorio de _DockerHub_, después hace los testeos de funciones, esperando que todos los endpoints funcionen correctamente. Ya que pasaron estas dos instrucciones toma todos los datos necesarios del entorno para procesar la subida a producción y si todo esta bien, hace el despligue.
