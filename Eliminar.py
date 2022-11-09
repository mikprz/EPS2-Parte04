import sqlite3

def Funcion2(nombre):

    conexion = sqlite3.connect("Rakauskas_Quispe_Prado_almacen.db")
    cursor = conexion.cursor()
    consulta_1 = "DELETE FROM Producto WHERE idproducto="
    cursor= conexion.cursor()

    consulta_1 = consulta_1 + str(nombre)
    cursor.execute(str(consulta_1))

    conexion.commit()
    conexion.close()