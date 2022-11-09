import sqlite3
import Listar
import Registrar

conexion = sqlite3.connect("Rakauskas_Quispe_Prado_almacen.db")
tabla_producto =""" CREATE TABLE IF NOT EXISTS Producto(
            idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE,
            nombre TEXT,
            precio FLOAT
            )
       """

cursor = conexion.cursor()
cursor.execute(tabla_producto)

conexion.close()

print("\tMenu de opciones\n")
print("1. Registrar\n")
print("2. Eliminar\n")
print("3. Editar\n")
print("4. Listar\n")
print("5. Salir\n")

opcion=input("\nSeleccione una opcion: ")

if opcion=='1':
    nombre=input("nombre: ")
    codigo=input("codigo: ")
    precio=input("precio: ")
    Registrar.Agregar(codigo,nombre,precio)
elif opcion=='2':
     n=1
elif opcion=='3':
    n=2
elif opcion=='4':
     Listar.Funcion1()
else:
     
    n=6

