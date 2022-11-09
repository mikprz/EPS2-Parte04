import sqlite3

conexion = sqlite3.connect("Rakauskas_Quispe_Prado_almacen.db")
tabla_producto =""" CREATE TABLE Producto(
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