## Contenedor subido correctamente a Docker Hub y documentación de la actualización automática

Antes de subir contenedores e imagenes a Docker Hub debemos crear una cuenta del mismo. Podemos utilizar la misma de Docker Desktop, e incluso podemos enlazar estas mismas con nuestro Github:
![Conexión de Docker con Github](/./img/3_docker_github_connect.png)

## Subida Manual
Para subir de forma manual nuestra imagen y contenedor, debemos etiquetar de forma local nuestra imagen y después subirla usando los siguientes comandos:
```
docker tag gaalm/imagen_proyecto_cc:latest gaalm/imagen_proyecto_cc:latest
docker push gaalm/imagen_proyecto_cc:latest
```
Podemos ver el resultado de la ejecución de estos comandos en Docker Hub, donde podemos encontrar el contenedor de nuestra imagen correctamente cargado
![Imagen cargada en Docker Hub](/./img/3_hub_createdrepo.png)

## Automatización
Por otro lado, tenemos la opción de configurar un archivo *.yml* para crear una acción en nuestro repositorio de Github. Esta acción es tal que para cada modificación del repositorio, se vuelve a cargar un nuevo contenedor a Docker Hub para actualizar de forma automática esta imagen en línea de nuestra ejecución.
Para ello, creamos el archivo [docker_publish.yml](/./.github/workflows/docker_publish.yml) con el siguiente código:
```yml
name: Publish Docker image

on:
  release:
    types: [published]
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]  

jobs:
  push_to_registry:
    name: Push Docker image to Docker Hub
    runs-on: ubuntu-latest
    steps:
      - name: Check out the repo
        uses: actions/checkout@v4
      
      - name: Log in to Docker Hub
        uses: docker/login-action@f4ef78c080cd8ba55a85445d5b36e214a81df20a
        with:
          username: ${{ secrets.DOCKER_NAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}
      
      - name: Extract metadata (tags, labels) for Docker
        id: meta
        uses: docker/metadata-action@9ec57ed1fcdbf14dcef7dfbe97b2010124a938b7
        with:
          images: gaalm/imagen_proyectocc
      
      - name: Build and push Docker image
        uses: docker/build-push-action@3b5e8027fcad23fda98b2e3ac259d8d67585f671
        with:
          context: .
          file: ./Dockerfile
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
```
Nótese que para poder ejecutar correctamente este archivo, es necesario configurar una sección en Github llamada *Secrets*. En esta sección se establecen una serie de variables a las que daremos valor y un nombre con el que se podrá usar el valor sin acceder a él, con el objetivo de mantener privacidad de cara a la publicación de estos archivos donde necesitamos usar las credenciales de Docker (y otros posibles usos). En la siguiente imagne podemos ver cómo se establecen estas variables:

![Github Secrets](/./img/3_github_secrets.png)

Una vez este archivo ha sido incluido en el proyecto debidamente y probamos la ejecución del mismo, podemos ver el resultado de su correcta ejecución así como la imagen satisfactoriamente cargada:

![Acción ejecutada](/./img/3_action_working.png)
![Imagen cargada en Docker Hub mediante una acción](/./img/3_docker_action.png)