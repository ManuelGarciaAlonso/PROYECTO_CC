## Creación del fichero de composición y testeo del clúster

### Configuración del fichero

El archivo [docker-compose.yml](/./docker-compose.yml) define varios servicios para el proyecto, incluyendo pruebas, una base de datos, pruebas específicas en Docker, y la API, utilizando la versión 3.8 de Docker Compose. A continuación, se muestra el código:

```yaml
version: '3.8'
services:
  test:
    build:
      context: .
    volumes:
      - .:/app
    command: invoke test
    networks:
      - app-network

  db:
    build: 
      context: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    networks:
      - app-network

  docker_test:
    build:
      context: .
    volumes:
      - .:/app
    command: ["pytest", "tests/docker.py"]
    networks:
      - app-network

  api:
    build:
      context: .
    volumes:
      - .:/app
    command: ["pytest", "tests/tests.py"]
    networks:
      - app-network

networks:
  app-network: {}
```

### Creación de Tests para Docker Compose:

Por otro lado, se ha creado un script [docker.py](/./tests/docker.py) que contiene las pruebas para validar el funcionamiento de los servicios desplegados con Docker Compose. Este script esa las dependencias especificadas para realizar peticiones a los servicios y verificar respuestas esperadas, asegurando así la correcta interacción entre los contenedores. Se ha creado también una función de *timeout* para controlar la recepción de la respuesta del servidor:
```python
import requests
import time
def wait_for_service(url, timeout=30):
    start_time = time.time()
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Service is up!")
                break
        except requests.ConnectionError:
            pass
        if time.time() - start_time > timeout:
            raise Exception("Timeout waiting for service")
        time.sleep(1)


def test_app_response():

    wait_for_service("http://localhost:8000/services/")
    response = requests.get("http://localhost:8000/services/")
    assert response.status_code == 200

    wait_for_service("http://localhost:8000/services/Diseño Web")
    response = requests.get("http://localhost:8000/services/Diseño Web")
    assert response.status_code == 200
```

### Ejecución de los tests del clúster

Una vez hemos hecho toda la configuración, nuestro entorno está preparado para usar los contenedores que hemos definido para la ejecución de nuestra aplicación. Al hacer algún cambio, podemos visualizar los resultados de nuestra composición de servicios en la ejecución de la acción donde hemos incluido Docker-Compose:
![Resultado de la acción](/./img/6_action_result.png)


Vemos cómo se ejecutan los diferentes servicios y cuál es su resultado.

Por otro lado, si accedemos a Docker Hub se puede ver cómo la imágen ha sido actualizada:


![Docker Hub](/./img/6_docker_push.png)