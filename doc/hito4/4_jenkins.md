## Configuración de Jenkins como Sistema de Integración Continua

Primero, creamos nuestra nueva tarea, que en nuestro caso será una pipeline se llamará ProyectoCC_IC. Una vez hemos creado la tarea accedemos a la configuración de la misma para establecer el enlace a nuestro repositorio en github:

![Configuración tarea 1](/./img/4_jenkins_task.png)

Por otro lado, vamos a configurar también los disparadores(Build Triggers: GitHub hook trigger for GITScm polling y Lanzar ejecuciones remotas (ej: desde 'scripts')) para autenticar las cambios de forma automática. Para ello, debemos realizar las siguientes configuraciones en la tarea que hemos creado:

![Configuración tarea 2](/./img/4_jenkins_task2.png)
![Configuración tarea 3](/./img/4_jenkins_task3.png)

En este proceso establecemos también la dirección de nuestro archivo de [configuración de Jenkins](/./Jenkinsfile).