
import sqlite3 as sql
#crear base de datos
def createDB():
    conn = sql.connect("hiscores.db")
    conn.commit()
    conn.close()
    
#crear tablas 
def createTable():
    conn = sql.connect("hiscores.db")    
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE hiscores(
            nombre text,
            puntaje integer
            )"""
    )
    conn.commit()
    conn.close()

#grabar el hiscore en la base de datos
def insertarColumna(nombre_jugador,score):
    conn = sql.connect("hiscores.db")    
    cursor = conn.cursor()
    instruccion = f"INSERT INTO hiscores VALUES ('{nombre_jugador}',{score})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

#traer los datos a la lista hi scores para mostrar en el menu 
def leerDatos():
    conn = sql.connect("hiscores.db")    
    cursor = conn.cursor()
    instruccion = f"select * from hiscores ORDER BY {'puntaje'} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    lista_hiscores = list(datos)
    return lista_hiscores
           
                      
if __name__ == "__main__":
    #createDB() ok
    #createTable() ok
    #insertarColumna("kako",1000) #test para ver si funciona
    leerDatos()

