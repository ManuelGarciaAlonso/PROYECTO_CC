## Elección y Configuración del Gestor de Tareas

En este proyecto se busca realizar una gestión "secuencial" del desarrollo, es decir, confirmar la validez de lo desarrollado para poder seguir desarrollando. Esto, sumado un enfoque para los test modular y con definiciones claras, lleva la eleccióndel modelo de test a TDD, y en este sentido se han elegido las herramientas para la ejecución de los mismos.

### Justificación
Para la gestión de tareas se ha escogido Invoke. Invoke es una herramienta que de forma fácil y simple pero potente, nos permite especificar y ejecutar tareas de forma automática en Python, lenguaje en el que se desarrolla el proyecto. Además, facilita la ejecución de tareas como el manejo de dependencias o la limpieza del entorno existente, por lo que no sólo podemos dedicar la gestión de tareas a los propios test, haciendo más eficiente el desarollo

### Uso

Para la instalación de Invoke, ejecutamos el siguiente comando en la terminal:
```
pip install invoke
```

Una vez hemos instalado el gestor de tareas, podemos hacer tareas como:

- Preparación de dependencias
```
@task
def install_deps(c):
    c.run("pip install -r requirements.txt")
```
Con esta tarea podríamos definir en un archivo de texto las dependencias necesarias para la ejecución, pudiendo así exportar la ejecución de estos test a otros entornos no configurados

- Ejecución de los test
```
@task
def test(c):
    c.run("pytest tests/test1.py")
```

- Limpieza del entorno
```
@task
def clean(c):
    c.run("find . -name '*.pyc' -exec rm -f {} +")
```

La configuración del gestor de tareas para el proyecto se encuentra [aquí](/././tasks.py)