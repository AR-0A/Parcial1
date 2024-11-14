
# entrada_productos.py

from almacen import almacen  # Importamos la estructura del almacén

def agregar_producto():
    print("Gestión de Entrada de Productos al Almacén")
    
    # Solicitar datos al usuario
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    estanteria = input("Ingrese la estantería de destino (e.g., Estantería A): ")
    
    # Verificar si la estantería existe
    if estanteria in almacen:
        # Buscar si el producto ya existe en la estantería
        for producto in almacen[estanteria]:
            if producto['nombre'] == nombre:
                # Si el producto ya existe, actualizar la cantidad y el precio
                producto['cantidad'] += cantidad
                producto['precio'] = precio  # Actualizamos el precio
                print(f"Producto '{nombre}' actualizado correctamente en {estanteria}.")
                return
        
        # Si el producto no existe, lo agregamos como nuevo
        nuevo_producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
        almacen[estanteria].append(nuevo_producto)
        print(f"Producto '{nombre}' agregado correctamente a {estanteria}.")
    else:
        # Si la estantería no existe, mostramos un mensaje de error
        print(f"Error: La estantería '{estanteria}' no existe en el almacén.")

# Llamada a la función principal si ejecutamos este archivo directamente
if __name__ == "__main__":
    agregar_producto()
