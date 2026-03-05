from crud_empanadas import (
    listar_empanadas,
    agregar_empanada,
    editar_empanada,
    eliminar_empanada
)


def mostrar_menu(datos):

    while True:

        print("""
===== MENU EMPANADAS =====

1. Listar empanadas
2. Agregar empanada
3. Editar empanada
4. Eliminar empanada
5. Salir
""")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            listar_empanadas(datos)

        elif opcion == "2":
            agregar_empanada(datos)

        elif opcion == "3":
            editar_empanada(datos)

        elif opcion == "4":
            eliminar_empanada(datos)

        elif opcion == "5":
            print("[LOG] Cerrando programa...")
            break

        else:
            print("Opción inválida.")