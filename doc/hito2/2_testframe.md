## Elección y Uso del Marco de Pruebas

### Justificación

De nuevo, se usará pytest como nuestro marco de pruebas, debido a su versatilidad y, como ya ha sido mencionado, fácil integración con Python. Pytest nos permite ejecutar pruebas con complejidad variable, pero en en este caso será usado para las pruebas unitarias creadas.


### Uso:

1. Creación y activación de un entorno virtual

Primero, usando Invoke debemos crear un entorno virtual. Esto se hace para aislar la ejecución y evitar probelmas de dependencias:

```text
python -m venv entorno1
```
Para activar el entorno usamos:

```text
.\entorno1\Scripts\activate
```

2. Ejecución de los tests

Una vez hemos configurado el entorno virtual, ejecutamos los test desde la termina usando:

```text
.\venv\Scripts\invoke test
```

Otra opción es ejecutarlos directamente con Pytest:

```text
pytest test/test_profile.py
```

En la siguiente imagen se muestra la secuencia de comandos de la ejecución de los test, que en este caso es satisfactoria:
![Ejecución de tests de Pytest usando Invoke en un entorno virtual](/././img/2_tests_executed.png)