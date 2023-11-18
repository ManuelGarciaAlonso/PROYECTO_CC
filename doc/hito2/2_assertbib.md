## Elección y Uso de la Biblioteca de Aserciones


### Justificación
Como biblioteca de aserciones, la herramienta escogida ha sido Pytest. Pytest es la herramienta para creación de tests más usada por su simplicidad y facilidad de uso, ya que el desarrollo tiene un formato muy legible y entendible.
Con Pytest podemos realizar test unitarios definiendo aserciones precisas del comportamiento de cada componente del sistema. Por otro lado, al ser una herramienta extendida y específica para Python, se convierte en una herramienta indicada para este proyecto.

### Uso

Para la instalación de Pytest, ejecutamos el siguiente comando en la terminal:
```
pip install pytest
```

Una vez hemos instalado la biblioteca de aserciones, se diseñan los test necesarios para las [US](/././doc/hito1/1_US.md). Estos son algunos posibles tests:

1. US-01 - Crear un perfil en la plataforma

   ```python
   def test_creacion_perfil_usuario():
    usuario = UserProfile("usuario1", "Python, Desarrollo Web", "5 años")
    assert usuario.username == "usuario1"
    assert usuario.skills == "Python, Desarrollo Web"
   ```

2. US-02 - Publicar servicios o habilidades

   ```python
   def test_publicar_servicio():
    proveedor = UserProfile("proveedor_servicio", "Enseñanza", "3 años")
    servicio = Service("Curso de Python", "Curso Intermedio de Python", 100, proveedor, "Educación")
    proveedor.add_service(servicio)
    assert servicio in proveedor.services_offered
   ```

3. US-03 - Calificar a las personas que proporcionan los recursos

   ```python
   def test_agregar_calificacion_a_servicio():
    proveedor_servicio = UserProfile("instructor", "Enseñanza", "3 años")
    servicio = Service("Taller de Ciencia de Datos", "Aprende Ciencia de Datos", 150, proveedor_servicio, "Educación")
    calificacion = Rating("estudiante", 5, "¡Excelente curso!", servicio)
    assert calificacion in servicio.ratings
    assert calificacion.score == 5
   ```

4. US-04 - Realizar transacciones desde la aplicación

   ```python
   def test_creacion_transaccion():
    comprador = UserProfile("comprador", "Estudiante", "1 año")
    vendedor = UserProfile("vendedor", "Instructor", "5 años")
    servicio = Service("Curso de Desarrollo Web", "Aprende Desarrollo Web", 200, vendedor, "Tecnología")
    transaccion = Transaction(comprador, vendedor, servicio, 200)
    assert transaccion.status == "Pending"
   ```

5. US-05 - Hablar y establecer detalles de un servicio a través de un chat

   ```python
   def test_funcionalidad_chat():
    usuario1 = UserProfile("usuario1", "Python", "2 años")
    usuario2 = UserProfile("usuario2", "JavaScript", "3 años")
    chat = Chat(usuario1, usuario2)
    chat.send_message(usuario1, "Hola, ¿tienes conocimientos sobre despliegues?")
    assert chat.get_latest_message() == (usuario1, "Hola, ¿tienes conocimientos sobre despliegues?")
   ```

6. US-06 - Usar filtros específicos al buscar servicios

   ```python
   def test_filtrado_servicios():
    mercado = ServiceMarketplace()
    servicio1 = Service("Tutoría de Python", "Tutoría individual de Python", 50, UserProfile("tutor1", "Enseñanza", "5 años"), "Educación")
    servicio2 = Service("Taller de JavaScript", "Taller para principiantes de JS", 75, UserProfile("instructor1", "Desarrollo", "7 años"), "Tecnología")
    mercado.add_service(servicio1)
    mercado.add_service(servicio2)
    servicios_filtrados = mercado.search_services({"price": "<=75"})
    assert servicio1 in servicios_filtrados
    assert servicio2 in servicios_filtrados
   ```

Todos estos test han sido desarrollados e incluidos en el [archivo de tests](/././tests/tests.py)