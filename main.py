from storage import cargar_datos
from menu import mostrar_menu


def main():
    print("[LOG] Iniciando sistema de empanadas...")

    datos = cargar_datos()

    mostrar_menu(datos)


if __name__ == "__main__":
    main()