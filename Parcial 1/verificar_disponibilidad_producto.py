
# verificar_disponibilidad_producto.py

from almacen import almacen  # Importamos la estructura del almacén

def verificar_disponibilidad():
    print("Verificación de Disponibilidad de Productos en el Almacén")
    
    # Solicitar el nombre del producto al usuario
    nombre = input("Ingrese el nombre del producto a verificar: ")
    encontrado = False  # Variable para saber si el producto se encontró
    
    # Recorrer cada estantería en el almacén
    for estanteria, productos in almacen.items():
        # Buscar el producto en la estantería actual
        for producto in productos:
            if producto['nombre'] == nombre:
                # Si se encuentra el producto, mostrar la cantidad y la estantería
                print(f"Producto '{nombre}' encontrado en {estanteria}. Cantidad disponible: {producto['cantidad']}.")
                encontrado = True  # Marcar que el producto fue encontrado
    
    # Si el producto no se encuentra en ninguna estantería, informar al usuario
    if not encontrado:
        print(f"El producto '{nombre}' no se encuentra disponible en ninguna estantería.")

# Llamada a la función principal si ejecutamos este archivo directamente
if __name__ == "__main__":
    verificar_disponibilidad()
