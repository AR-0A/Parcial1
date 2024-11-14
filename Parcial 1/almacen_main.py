
# almacen_main.py

from gestionar_entrada_producto import agregar_producto
from gestionar_salida_producto import retirar_producto
from verificar_disponibilidad_producto import verificar_disponibilidad
from verificar_estado_almacen import verificar_estado_almacen
from transferencia_producto import transferir_producto
from optimización_inventario import optimizar_inventario

def mostrar_menu():
    print("\nBienvenido al sistema de gestión del almacén. Seleccione una opción:")
    print("1. Gestionar Entrada de Productos")
    print("2. Gestionar Salida de Productos")
    print("3. Verificar Disponibilidad de Productos")
    print("4. Verificar Estado del Almacén")
    print("5. Transferir Productos entre Estanterías")
    print("6. Optimizar Inventario")
    print("0. Salir")

def ejecutar_opcion(opcion):
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        retirar_producto()
    elif opcion == "3":
        verificar_disponibilidad()
    elif opcion == "4":
        verificar_estado_almacen()
    elif opcion == "5":
        transferir_producto()
    elif opcion == "6":
        optimizar_inventario()
    elif opcion == "0":
        print("Saliendo del sistema de gestión del almacén.")
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la acción que desea realizar: ")
        if opcion == "0":
            ejecutar_opcion(opcion)
            break
        ejecutar_opcion(opcion)

# Llamada a la función principal si ejecutamos este archivo directamente
if __name__ == "__main__":
    main()
