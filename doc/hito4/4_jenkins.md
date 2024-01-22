## Configuración de Jenkins como Sistema de Integración Continua Adicional

Creamos nuestra nueva tarea, que en nuestro caso se llamará ProyectoCC_IC. Una vez hemos creado la tarea accedemos a la configuración de la misma para establecer el enlace a nuestro repositorio en github

![](/./img/4_jenkins_task.png)

Por otro lado, vamos a configurar también los disparadores(Build Triggers: GitHub hook trigger for GITScm polling y Lanzar ejecuciones remotas (ej: desde 'scripts')) para autenticar las cambios de forma automática. Para ello, debemos realizar las siguientes configuraciones en la tarea que hemos creado

task2_3

En este proceso establecemos también la dirección de nuestro archivo de [configuración de Jenkins](/./Jenkinsfile).




Para configurar el sistema y aprovechar las herramientas ya usadas en hitos anteriores, debemos crear un Webhook dentro de nuestro proyecto de Github que se asocie a nuestro Jenkins de tal modo que cuando se ejecute algún cambio en el repositorio, nuestro Github se coordine con el sistema de IC. Para ello, debemos de usar un sistema auxiliar, ya que hemos configurado Jenkins para trabajar de forma local, por lo que Github no puede acceder al servicio, y para solucionar este problema hemos hecho uso de ngork. Ngork es un proxy inverso distribuido globalmente que nos proporciona recursos para alojar de forma remota nuestros servicios locales.

Para instalar Ngork usamos su página web, y una vez lo hemos instalado debemos iniciar sesión, donde podemos enlazar con nuestro perfil de Github.
![](/./img/4_jenkins_task.png)

Utilizando los siguientes comandos nos autenticamos y creamos un servicio remoto accesible por github de nuestro servicio local de Jenkins:
´´´
´´´
![](/./img/4_jenkins_task.png)
![](/./img/4_jenkins_task.png)

Ahora podemos usar la url generada para crear nuestro Webhook:


