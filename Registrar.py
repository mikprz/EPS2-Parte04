import sqlite3


def Agregar(code,nomb,prize):

    miConexion=sqlite3.connect("Rakauskas_Quispe_Prado_almacen.db")
    miCursor = miConexion.cursor()


    nuevo_prod=[(code,nomb,prize)]

    consult_agregar="""INSERT INTO
                    Producto ('codigo','nombre','precio')
                    VALUES (?,?,?)
                """
    miCursor.executemany(consult_agregar,nuevo_prod)
    miConexion.commit()
    miConexion.close()


