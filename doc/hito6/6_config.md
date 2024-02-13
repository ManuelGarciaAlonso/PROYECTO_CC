## Documentación y justificación de la estructura del clúster y la configuración de contenedores

### Estructura del Clúster
El clúster está diseñado para soportar un entorno de desarrollo y pruebas compuesto por varios servicios esenciales que conforman la aplicación. La elección de Docker Compose para la orquestación de estos servicios se debe a su simplicidad y eficacia en la creación de entornos de desarrollo reproducibles y aislados. La estructura del clúster incluye los siguientes servicios:

- Servicio de Pruebas (test): Ejecuta pruebas generales de la aplicación, utilizando invoke como herramienta de ejecución. Este servicio es crucial para validar la lógica de negocio y asegurar que el código cumple con los requisitos antes de avanzar a etapas de despliegue.

- Base de Datos (db): Simula el servicio de almacenamiento persistente de la aplicación.

- Pruebas Docker (docker_test): Se centra en la ejecución de pruebas específicas de Docker, usando pytest para validar la correcta configuración y funcionamiento de los contenedores. Este servicio es fundamental para asegurar que la aplicación se comporta correctamente en un entorno contenerizado.

- API (api): Contiene la lógica de la aplicación accesible a través de interfaces HTTP. Este servicio es esencial para probar la interacción con la aplicación mediante llamadas a la API, verificando su funcionalidad y rendimiento.

- La red app-network facilita la comunicación interna entre los servicios, permitiendo que interactúen como si estuvieran en el mismo entorno de red sin exponer puertos innecesariamente al exterior.

### Configuración de Contenedores
La configuración de cada contenedor se ha diseñado con el objetivo de maximizar la eficiencia y la seguridad del entorno de desarrollo y pruebas. A continuación, se justifican las decisiones más importantes:

1. Contexto de Construcción Compartido: Todos los servicios utilizan el mismo contexto de construcción (.), lo que simplifica la gestión de las imágenes y hace que todos los contenedores se actualizan simultáneamente con el código más reciente.
2. Volúmenes: Se monta el directorio actual (.) dentro de los contenedores (/app), permitiendo que los cambios en el código fuente se reflejen inmediatamente en los servicios sin necesidad de reconstruir las imágenes. Esta configuración es ideal para nuestro desarrollo.
3. Redes: La inclusión de todos los servicios en app-network asegura que puedan comunicarse entre sí de manera eficiente, simulando un entorno de microservicios. Esta coniguración es determinante para probar la interacción entre losdiferentes componentes de la aplicación.
4. Puertos: Solo el servicio db expone un puerto (8000) hacia el exterior, facilitando el acceso a la base de datos durante el desarrollo. Esta decisión minimiza la exposición de servicios internos, limitando el acceso a aquellos lo necesario para el desarrollo y las pruebas.


### Añadir Dependencias

Para el correcto funcionamiento de las pruebas, especialmente las realizadas en el servicio *docker_test* que crearemos, es esencial incluir las dependencias necesarias en [requirements.txt](/./requirements.txt):

```
requests==2.28.1
requests-oauthlib==1.3.1
```

Estas dependencias permiten realizar peticiones HTTP y manejar la autenticación OAuth, respectivamente, lo cual es crucial para testear la interacción con la API y otros servicios web.

### Configuración de GitHub Actions y cc.yaml

Para integrar la construcción y prueba de los servicios con GitHub Actions, se debe añadir el siguiente paso en alugno de los flujos de trabajo CI de la [carpeta de workflows](/./.github/workflows/):

```yaml
- name: Docker Compose Build
    run: docker-compose up
```

Por otro lado, para asegurar que las pruebas específicas de Docker Compose se ejecuten como parte de la evaluación continua, se debe incluir la siguiente línea en el archivo [cc.yaml](/./cc.yaml):

```yaml
test-docker-compose:
  - docker-compose -f docker-compose.yml up --abort-on-container-exit --build
```

Esto garantiza la ejecución y evaluación automáticas de los servicios definidos en [docker-compose.yml](/./docker-compose.yml), incluyendo el entorno de pruebas, la base de datos, y los servicios API.