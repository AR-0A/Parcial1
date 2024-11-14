
# gestionar_salida_producto.py

from almacen import almacen  # Importamos la estructura del almacén

def retirar_producto():
    print("Gestión de Salida de Productos del Almacén")
    
    # Solicitar detalles del producto a retirar
    nombre = input("Ingrese el nombre del producto a retirar: ")
    cantidad = int(input("Ingrese la cantidad a retirar: "))
    estanteria = input("Ingrese la estantería de origen (e.g., Estantería A): ")
    
    # Verificar si la estantería existe
    if estanteria in almacen:
        # Buscar si el producto existe en la estantería
        for producto in almacen[estanteria]:
            if producto['nombre'] == nombre:
                # Verificar si la cantidad a retirar es posible
                if producto['cantidad'] >= cantidad:
                    producto['cantidad'] -= cantidad  # Restamos la cantidad
                    print(f"Producto '{nombre}' retirado correctamente de {estanteria}. Cantidad restante: {producto['cantidad']}.")
                else:
                    # Mensaje de error si la cantidad es insuficiente
                    print(f"Error: No hay suficiente cantidad de '{nombre}' en {estanteria}. Cantidad disponible: {producto['cantidad']}.")
                return
        
        # Si el producto no se encuentra en la estantería
        print(f"Error: El producto '{nombre}' no se encuentra en la estantería {estanteria}.")
    else:
        # Si la estantería no existe, mostramos un mensaje de error
        print(f"Error: La estantería '{estanteria}' no existe en el almacén.")

# Llamada a la función principal si ejecutamos este archivo directamente
if __name__ == "__main__":
    retirar_producto()
