import json
import os

ARCHIVO = "empanadas.json"


def cargar_datos():
    print("[LOG] Intentando cargar archivo JSON...")

    if not os.path.exists(ARCHIVO):
        print("[LOG] Archivo no encontrado. Creando nuevo archivo...")
        with open(ARCHIVO, "w") as f:
            json.dump([], f)

    with open(ARCHIVO, "r") as f:
        datos = json.load(f)

    print(f"[LOG] {len(datos)} empanadas cargadas.")
    return datos


def guardar_datos(datos):
    print("[LOG] Guardando cambios en empanadas.json...")

    with open(ARCHIVO, "w") as f:
        json.dump(datos, f, indent=4)

    print("[LOG] Cambios guardados correctamente.")