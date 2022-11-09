import sqlite3

def Funcion2(nombre,id):

    conexion = sqlite3.connect("Rakauskas_Quispe_Prado_almacen.db")
    cursor = conexion.cursor()
    consulta_1 = "UPDATE Producto SET '"
    consulta_1 = consulta_1 + str(nombre)

    consulta_1 = consulta_1 + "' WHERE idproducto="

    consulta_1 = consulta_1 + str(id)
    cursor= conexion.cursor()
    
    cursor.execute(str(consulta_1))

    conexion.commit()
    conexion.close()