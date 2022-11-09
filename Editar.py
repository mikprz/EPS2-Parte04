import sqlite3

def Funcion2():
    conexion=sqlite3.connect("Rakauskas_Quispe_Prado_almacen.db")
    cursor=conexion.cursor()

    edit_nom=input("Ingrese el nombre del producto a modificar: ")
    cod=input("Ingrese el nuevo código del producto: ")
    nom=input("Ingrese el nuevo nombre del producto: ")
    precio=float(input("Ingrese el nuevo precio del producto: "))
    consulta="UPDATE Producto SET codigo=?, nombre=?, precio=? WHERE nombre=?"

    cursor.execute(consulta,(cod,nom,precio,edit_nom))

    conexion.commit()
    
    conexion.close()