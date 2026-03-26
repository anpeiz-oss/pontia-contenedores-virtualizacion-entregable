from fastapi import requests
from urllib3 import response
from pydantic.deprecated import json
from datetime import datetime, date, timedelta
import requests

BASE_URL = "http://localhost:8000"

def test_crear_tarea_ok():
    response = requests.post(f"{BASE_URL}/tasks/", json={
        "titulo": "Test OK",
        "contenido": "Contenido de tarea correcto, sin palabras malsonantes y con fecha de deadline posterior a la fecha actual.",
        "deadline": "2027-01-01"
    })
    assert response.status_code == 201
    print(f"Se ha creado la siguiente tarea: \n{response.json()}")

    print("Test crear tarea OK completado con EXITO !!!\n")

def test_crear_tarea_ko():
    response = requests.post(f"{BASE_URL}/tasks/", json={
        "titulo": "Test KO",
        "contenido": "Contenido de tarea de test que no se debería crear debido a incumplimiento de la fecha de deadline anterior a la fecha actual.",
        "deadline": "2026-01-01"
    })
    assert response.status_code == 422
    print("""NO se ha podido crear la tarea: \n{
        "titulo": "Test KO",
        "contenido": "Contenido de tarea de test que no se debería crear debido a incumplimiento de la fecha de deadline anterior a la fecha actual.",
        "deadline": "2026-01-01"
    }""")

    print("Test crear tarea KO completado con EXITO !!!\n")


def test_obtener_tarea_1_ok():
    response = requests.get(f"{BASE_URL}/tasks/1")
    print(response.json())
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["titulo"] == "Test OK"
    assert response.json()["contenido"] == "Contenido de tarea correcto, sin palabras malsonantes y con fecha de deadline posterior a la fecha actual."
    assert response.json()["deadline"] == "2027-01-01"
    assert response.json()["completada"] == False
    print("El detalle de la tarea con id 1 coincide con el esperado.")

    print("Test obtener tarea 1 OK completado con EXITO !!!\n")
    
def test_obtener_task2_ko():
    response = requests.get(f"{BASE_URL}/tasks/2")
    assert response.status_code == 404
    print(f"El código de respuesta esperado (404) coincide con el obtenido ({response.status_code}).")

    print("Test obtener task2 KO completado con EXITO !!!\n")

def test_marcar_task1_completada_ok():
    antes = requests.get(f"{BASE_URL}/tasks/1")
    print(f"El atributo completada e la tarea con id 1 antes de ejecutar la llamada a marcar como completado es : {antes.json()['completada']}")
    despues = requests.put(f"{BASE_URL}/tasks/1/completar")
    assert despues.status_code == 200
    assert despues.json()["completada"] == True
    print(f"El atributo completada e la tarea con id 1 despues de ejecutar la llamada a marcar como completado es : {despues.json()['completada']}")

    print("Test marcar completada OK completado con EXITO !!!\n")

def test_obtener_todas_tareas():
    response = requests.get(f"{BASE_URL}/tasks/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    print(f"Se espera un lista de longitud 1 como resultado de la obtención de todas las tareas existentes y la longitud de la lista de tareas obtenidas es {len(response.json())}")

    print("Test obtener todas las tareas completado con EXITO !!!\n")

def test_obtener_tareas_caducadas():
    response = requests.get(f"{BASE_URL}/tasks/caducadas/")
    assert response.status_code == 200
    assert len(response.json()) == 0
    print(f"Se espera un lista vacía (longitud 0) como resultado de la obtención de las tareas caducadas y la longitud de la lista de tareas obtenidas es {len(response.json())}")

    print("Test obtener tareas caducadas completado con EXITO !!!\n")

def test_obtener_tareas_completadas():
    response = requests.get(f"{BASE_URL}/tasks/completadas/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    print(f"Se espera un lista de longitud 1 como resultado de la obtención de las tareas completadas y la longitud de la lista de tareas obtenidas es {len(response.json())}")

    print("Test obtener tareas completadas completado con EXITO !!!\n")

def test_obtener_tareas_activas():
    response = requests.get(f"{BASE_URL}/tasks/activas/")
    assert response.status_code == 200
    assert len(response.json()) == 0
    print(f"Se espera un lista vacía (longitud 0) como resultado de la obtención de las tareas activas y la longitud de la lista de tareas obtenidas es {len(response.json())}")

    print("Test obtener tareas activas completado con EXITO !!!\n")

def test_borrar_tarea_inexistente():
    response = requests.delete(f"{BASE_URL}/tasks/2")
    assert response.status_code == 404
    print(f"Se espera un código de respuesta 404 como resultado de la eliminación de una tarea inexistente y el código de respuesta obtenido es {response.status_code}")

    print("Test borrar tarea inexistente completado con EXITO !!!\n")

def test_borrar_task1_ok():
    antes = requests.get(f"{BASE_URL}/tasks/")
    print(f"La longitud de la lista de tareas obtenidas antes de borrar la task1 es {len(antes.json())}")
    
    response = requests.delete(f"{BASE_URL}/tasks/1")
    assert response.status_code == 204
    print(f"Se espera un código de respuesta 204 como resultado de la eliminación de una tarea existente y el código de respuesta obtenido es {response.status_code}")

    despues = requests.get(f"{BASE_URL}/tasks/")
    assert len(despues.json()) == len(antes.json()) - 1
    print(f"La longitud de la lista de tareas obtenidas tras el borrado es {len(despues.json())} que coincide con lo esperado ({len(antes.json()) - 1})")
    
    print("Test borrar task1 OK completado con EXITO !!!\n")

def test_obtener_todas_tareas_tras_borrado_task1():
    response = requests.get(f"{BASE_URL}/tasks/")
    assert response.status_code == 200
    assert len(response.json()) == 0
    print("Test obtener todas las tareas tras borrado task1 completado con EXITO !!!\n")

def test_eliminacion_palabras_malsonantes_ok():
    response = requests.post(f"{BASE_URL}/tasks/", json={
        "titulo": "Test Palabras Malsonantes en el contenido.",
        "contenido": "Este es un ejemplo de contenido que contiene palabras malsonantes como puto, coño, joder, mierda, hostia, carajo, cabron, gilipollas, pene, vagina, culo, tetas, zorra, maricon.",
        "deadline": "2027-01-01"
    })
    print(f"La respuesta tras el intento de creación de la taks2 cuyo 'contenido': 'Este es un ejemplo de contenido que contiene palabras malsonantes como puto, coño, joder, mierda, hostia, carajo, cabron, gilipollas, pene, vagina, culo, tetas, zorra, maricon.'")
    assert response.status_code == 201
    assert response.json()["contenido"] == "Este es un ejemplo de contenido que contiene palabras malsonantes como *, *, *, *, *, *, *, *, *, *, *, *, *, *."
    print(f"Se ha creado la siguiente tarea: \n{response.json()}")

    print("Test eliminacion palabras malsonantes OK completado con EXITO !!!\n")

if __name__ == "__main__":
    print("\nPara que esta batería de tests funcione como se ha diseñado:")
    print("Debe partirse de una base de datos limpia y para garantizar este punto hay que borrar el fichero tasks.db de la raiz del repositorio antes de levantar la app a testear con el servidor fastapi.")
    print("\nEjecutando tests...\n")
    
    test_crear_tarea_ok()
    test_crear_tarea_ko()
    test_obtener_tarea_1_ok()
    test_obtener_task2_ko()
    test_marcar_task1_completada_ok()
    test_obtener_todas_tareas()
    test_obtener_tareas_caducadas()
    test_obtener_tareas_completadas()
    test_obtener_tareas_activas()
    test_borrar_tarea_inexistente()
    test_borrar_task1_ok()
    test_obtener_todas_tareas_tras_borrado_task1()
    test_eliminacion_palabras_malsonantes_ok()
    
    print("\nTests completados\n")
