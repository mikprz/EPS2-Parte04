import sqlite3



def Funcion1():

    conexion = sqlite3.connect("Rakauskas_Quispe_Prado_almacen.db")
    cursor = conexion.cursor()
    consulta_1 = "SELECT *FROM Producto"
    cursor= conexion.cursor()
    cursor.execute(str(consulta_1))
    libros=  cursor.fetchall()
    print('Codigo\t\tNombre\t\tPrecio')
    print('_______________________________________\n')

    m=1
    sd=''

    n=1  
    for libro in libros:

            sd=sd+nombre_l(n)+'\t'
            sd=sd+codigo_l(n)+'\t'
            sd=sd+'\t'+precio_l(n)
            n=n+1

       
    print(sd)
def nombre_l(n):
    conexion = sqlite3.connect("Rakauskas_Quispe_Prado_almacen.db")
    cursor = conexion.cursor()
    consulta = "SELECT codigo FROM Producto WHERE idproducto="
    consulta=consulta+str(n)
    cursor= conexion.cursor()
    cursor.execute(str(consulta))
    names=  cursor.fetchall()
    

    a=str(names).strip('[('')],')
    a=str(a).strip('\n')    

    return a

def codigo_l(n):
    conexion = sqlite3.connect("Rakauskas_Quispe_Prado_almacen.db")
    cursor = conexion.cursor()
    consulta = "SELECT nombre FROM Producto WHERE idproducto="
    consulta=consulta+str(n)
    cursor= conexion.cursor()
    cursor.execute(str(consulta))
    names=  cursor.fetchall()
    
    a=str(names).strip('[('')],')

    return a

def precio_l(n):
    conexion = sqlite3.connect("Rakauskas_Quispe_Prado_almacen.db")
    cursor = conexion.cursor()
    consulta = "SELECT precio FROM Producto WHERE idproducto="
    consulta=consulta+str(n)
    cursor= conexion.cursor()
    cursor.execute(str(consulta))
    names=  cursor.fetchall()
    
    a=str(names).strip('[('')],')

    return a + '\n'


print('Codigo\t\tNombre\t\tPrecio')
print('_______________________________________\n')



