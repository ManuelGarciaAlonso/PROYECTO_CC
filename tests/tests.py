import pytest
from src.SvcMkp import *

def test_creacion_perfil_usuario():
    usuario = UserProfile("usuario1", "Python, Desarrollo Web", "5 años")
    assert usuario.username == "usuario1"
    assert usuario.skills == "Python, Desarrollo Web"

def test_publicar_servicio():
    proveedor = UserProfile("proveedor_servicio", "Enseñanza", "3 años")
    servicio = Service("Curso de Python", "Curso Intermedio de Python", 100, proveedor, "Educación")
    proveedor.add_service(servicio)
    assert servicio in proveedor.services_offered

def test_agregar_calificacion_a_servicio():
    proveedor_servicio = UserProfile("instructor", "Enseñanza", "3 años")
    servicio = Service("Taller de Ciencia de Datos", "Aprende Ciencia de Datos", 150, proveedor_servicio, "Educación")
    calificacion = Rating("estudiante", 5, "¡Excelente curso!", servicio)
    assert calificacion in servicio.ratings
    assert calificacion.score == 5

def test_creacion_transaccion():
    comprador = UserProfile("comprador", "Estudiante", "1 año")
    vendedor = UserProfile("vendedor", "Instructor", "5 años")
    servicio = Service("Curso de Desarrollo Web", "Aprende Desarrollo Web", 200, vendedor, "Tecnología")
    transaccion = Transaction(comprador, vendedor, servicio, 200)
    assert transaccion.status == "Pending"

def test_funcionalidad_chat():
    usuario1 = UserProfile("usuario1", "Python", "2 años")
    usuario2 = UserProfile("usuario2", "JavaScript", "3 años")
    chat = Chat(usuario1, usuario2)
    chat.send_message(usuario1, "Hola, ¿tienes conocimientos sobre despliegues?")
    assert chat.get_latest_message() == (usuario1, "Hola, ¿tienes conocimientos sobre despliegues?")

def test_filtrado_servicios():
    mercado = ServiceMarketplace()
    servicio1 = Service("Tutoría de Python", "Tutoría individual de Python", 50, UserProfile("tutor1", "Enseñanza", "5 años"), "Educación")
    servicio2 = Service("Taller de JavaScript", "Taller para principiantes de JS", 75, UserProfile("instructor1", "Desarrollo", "7 años"), "Tecnología")
    mercado.add_service(servicio1)
    mercado.add_service(servicio2)
    servicios_filtrados = mercado.search_services({"price": "<=75"})
    assert servicio1 in servicios_filtrados
    assert servicio2 in servicios_filtrados
