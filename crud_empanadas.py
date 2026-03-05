from storage import guardar_datos


def listar_empanadas(datos):
    print("\n=== CATALOGO DE EMPANADAS ===")

    if not datos:
        print("No hay empanadas registradas.")
        return

    for emp in datos:
        print(f"""
Nombre: {emp['nombre']}
Precio: {emp['precio']}
Ingredientes: {emp['ingredientes']}
Disponible: {emp['disponible']}
---------------------------
""")


def agregar_empanada(datos):
    print("\n=== AGREGAR EMPANADA ===")

    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    ingredientes = input("Ingredientes principales: ")
    disponible = input("Disponible (si/no): ")

    nueva = {
        "nombre": nombre,
        "precio": precio,
        "ingredientes": ingredientes,
        "disponible": disponible
    }

    datos.append(nueva)

    print("[LOG] Empanada agregada.")
    guardar_datos(datos)


def editar_empanada(datos):
    print("\n=== EDITAR EMPANADA ===")

    nombre = input("Ingrese el nombre de la empanada a editar: ")

    for emp in datos:
        if emp["nombre"].lower() == nombre.lower():

            print("[LOG] Empanada encontrada. Editando...")

            emp["precio"] = float(input("Nuevo precio: "))
            emp["ingredientes"] = input("Nuevos ingredientes: ")
            emp["disponible"] = input("Disponible (si/no): ")

            guardar_datos(datos)

            print("[LOG] Empanada actualizada.")
            return

    print("Empanada no encontrada.")


def eliminar_empanada(datos):
    print("\n=== ELIMINAR EMPANADA ===")

    nombre = input("Nombre de la empanada a eliminar: ")

    for emp in datos:
        if emp["nombre"].lower() == nombre.lower():

            datos.remove(emp)

            guardar_datos(datos)

            print("[LOG] Empanada eliminada.")
            return

    print("Empanada no encontrada.")