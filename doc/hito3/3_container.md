## Elección Correcta y Justificada del Contenedor Base

Para el proyecto se ha decidido hacer uso del python:3.9-slim ya que para el uso que se le va a dar es una de las mejores opciones por varias razones que se comentan a continuación.

### Justificación:

1. Compatibilidad: Esta imagen es compatible con las diferentes tecnologías usadas en nuestro proyecto en Python, como se evidencia por la presencia de archivos Python en el directorio src.
2. Eficiencia en Tamaño: La versión 'slim' ofrece un tamaño de imagen reducido, lo cual es crucial para la construcción y despliegue rápidos del contenedor, sin sacrificar a pesare de la ligereza, las funcionalidades necesarias para la ejecución de la aplicación y las pruebas.
3. Amplio Soporte: Al ser una imagen oficial de Python, cuenta con un amplio soporte y una comunidad activa, asegurando actualizaciones regulares y seguridad.

### Uso
Para hacer uso de Docker, debemos realizar una serie de tareas previas a la creación del DockerFile:
1. Instalar docker desktop: 
Para instalar Docker Desktop debemos acceder a su página web e instalar el programa. Posterior a ello debemos introducir nuestras credenciales e iniciar sesión.
![Inicio de sesión](/././img/2_tests_executed.png)
2. Establecer fichero de requisitos: 
Este proyecto tiene una serie de dependencias que debemos indidcar para evitar errores en la ejecución. Nuestro [requirements.txt](/./requirements.txt) en concreto debe incluir invoke y pytest
3. Ejecutamos los comandos necesarios para contruir y cargar la imagen:
```cmd
docker build -t imagen .
docker run imagen
```