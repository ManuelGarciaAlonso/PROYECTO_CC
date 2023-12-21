## Dockerfile correcto adaptado de forma correcta a las clases o módulos que se están testeando, incluyendo optimización del tamaño

### Buenas prácticas
Antes de mostrar la configuración concreta de nuestro Dockerfile, estas son las buenas prácticas usadas:
- Minimización de Capas: Se agrupan los comandos COPY y RUN para reducir el número de capas en la imagen.
- Uso de --no-cache-dir en pip: Evitamos guardar la caché innecesaria de las instalaciones para reducir el tamaño de la imagen, optimizando su tamaño.
- Establecimiento de un WORKDIR: Facilita la referencia a archivos y directorios dentro del contenedor.

### Estructura del Dockerfile

```docker
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["pytest", "tests/tests.py"]
```

### Uso
Como ya ha sido mencionado en el apartado anterior, una vez hemos instalado Docker y configurado nuestras dependencias así como el Dockerfile, ejecutamos los siguientes comandos para cargar nuestra imagen:

```
docker build -t imagen_proyectocc .
docker run imagen_proyectocc
```

![Carga de imagen en Docker](././img/3_cmd_stats.png)

Podemos comprobar las imágenes existentes mediante los siguientes comandos:
```
docker ps -a
docker images
```

![Información de docker](././img/3_cmd_stats.png)