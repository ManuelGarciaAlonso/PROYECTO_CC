## Aprovechamiento del Contenedor de Docker en CI

Para configurar el sistema y aprovechar las herramientas ya usadas en hitos anteriores, debemos crear un Webhook dentro de nuestro proyecto de Github que se asocie a nuestro Jenkins de tal modo que cuando se ejecute algún cambio en el repositorio, nuestro Github se coordine con el sistema de IC. Para ello, debemos de usar un sistema auxiliar, ya que hemos configurado Jenkins para trabajar de forma local, por lo que Github no puede acceder al servicio, y para solucionar este problema hemos hecho uso de ngork. Ngork es un proxy inverso distribuido globalmente que nos proporciona recursos para alojar de forma remota nuestros servicios locales.

Para instalar Ngork usamos su página web, y una vez lo hemos instalado debemos iniciar sesión, donde podemos enlazar con nuestro perfil de Github.
![Instalación Ngork](/./img/4_ngork_1.png)

Utilizando los siguientes comandos nos autenticamos y creamos un servicio remoto accesible por github de nuestro servicio local de Jenkins:
´´´cmd  
ngrok config add-authtoken 2bK5SsBEiIu7POCmUmtSjQ2VpyI_rB2tN2882ksNYpSyApcs
ngrok http --domain=foxhound-quality-minnow.ngrok-free.app 8080
´´´
![Configuración Ngork](/./img/4_ngork_2.png)
![Conexión Ngork](/./img/4_ngork_3.png)

### 

Ahora podemos usar la url generada para crear nuestro Webhook:

![Webhook para conectar Github y Jenkins](/./img/4_webhook.png)

Podemos ver la correcta ejecución tanto del webhook como del pipeline de Jenkinks al hacer un push al repositorio:

![Webhook para conectar Github y Jenkins](/./img/4_webhookmade.png)
![Webhook para conectar Github y Jenkins](/./img/4_pipeline.png)