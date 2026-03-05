# 🥟 Sistema de Gestión de Empanadas

Programa de consola desarrollado en **Python** que permite administrar un **catálogo de empanadas** mediante operaciones básicas de gestión (CRUD).
La información se almacena de forma persistente en un archivo **JSON**, permitiendo que los datos se mantengan entre ejecuciones del programa.

---

# 📌 Características

* Ejecución desde **consola**
* **Menú interactivo**
* Persistencia de datos en archivo **JSON**
* Operaciones CRUD completas:

  * Listar empanadas
  * Agregar empanadas
  * Editar empanadas
  * Eliminar empanadas
* **Trazabilidad del proceso** mediante mensajes de log en consola
* **Arquitectura modular**

---

# 📂 Estructura del Proyecto

```
empanadas_app/
│
├── main.py              # Punto de entrada del programa
├── menu.py              # Manejo del menú de consola
├── crud_empanadas.py    # Lógica de negocio (CRUD)
├── archivo_json.py      # Lectura y escritura del archivo JSON
└── empanadas.json       # Base de datos del catálogo
```

---

# ⚙️ Funcionamiento del Sistema

El sistema sigue el siguiente flujo:

```
main.py
   │
   ▼
menu.py
   │
   ▼
crud_empanadas.py
   │
   ▼
archivo_json.py
   │
   ▼
empanadas.json
```

Cada módulo cumple una **responsabilidad específica**, permitiendo un código más limpio, mantenible y escalable.

---

# 🧩 Descripción de los Módulos

## main.py

Archivo principal que inicia la aplicación.

Responsabilidades:

* Cargar los datos desde el archivo JSON
* Iniciar el menú principal

---

## menu.py

Controla la interacción con el usuario mediante un **menú de opciones**.

Opciones disponibles:

1. Listar empanadas
2. Agregar empanada
3. Editar empanada
4. Eliminar empanada
5. Salir

---

## crud_empanadas.py

Contiene la lógica del negocio para manipular el catálogo.

Funciones principales:

* `listar_empanadas()`
* `agregar_empanada()`
* `editar_empanada()`
* `eliminar_empanada()`

---

## archivo_json.py

Encargado de la **persistencia de datos**.

Funciones:

* `cargar_datos()`
* `guardar_datos()`

Este módulo permite:

* Leer el archivo JSON al iniciar el sistema
* Guardar cambios después de cada modificación

---

## empanadas.json

Archivo donde se almacenan los registros del catálogo.

Ejemplo de estructura:

```json
[
  {
    "nombre": "Empanada de carne",
    "precio": 3000,
    "ingredientes": "carne, papa",
    "disponible": "si"
  }
]
```

---

# ▶️ Cómo ejecutar el programa

1. Clonar o descargar el proyecto.

2. Ubicarse en la carpeta del proyecto:

```
cd empanadas_app
```

3. Ejecutar el programa:

```
python main.py
```

---

# 💻 Requisitos

* Python 3.8 o superior
* Librerías utilizadas:

  * `json`
  * `os`

(No se requieren dependencias externas)

---

# 📊 Ejemplo del menú en consola

```
===== MENU EMPANADAS =====

1. Listar empanadas
2. Agregar empanada
3. Editar empanada
4. Eliminar empanada
5. Salir
```

---

# 🧠 Buenas prácticas aplicadas

* Separación de responsabilidades
* Arquitectura modular
* Persistencia de datos
* Código reutilizable
* Trazabilidad mediante logs

---

# 👨‍💻 Autor

Proyecto desarrollado como ejercicio de práctica en **Python** para implementar un sistema CRUD modular con persistencia en JSON.
