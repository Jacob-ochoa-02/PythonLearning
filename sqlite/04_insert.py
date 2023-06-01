import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    # Tiene que ser una tupla necesariamente
    cursor.execute(
        "insert into usuarios values(?, ?)",
        (1, "Hola Mundo"),
    )   # Para prevenir una SQL injection
