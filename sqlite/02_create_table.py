import sqlite3

con = sqlite3.connect("sqlite/app.db")
cursor = con.cursor()   # creamos un cursos a partir de la conexion
# en el cursor llamamos al metodo execute para hacer una consulta
cursor.execute(
    """
    CREATE TABLE if not exists usuarios
    (id_user INTEGER primary key, nombre VARCHAR(50));
    """
)
# debemos comprometer los cambios con el metodo commit para hacer la consulta
con.commit()    # <-metodo commit
con.close()
