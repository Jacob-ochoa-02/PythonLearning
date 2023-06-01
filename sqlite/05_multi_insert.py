import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    # Tiene que ser una tupla necesariamente
    usuarios = [
        (2, "Leonsito feliz"),
        (3, "Chanchito triste"),
    ]
    cursor.executemany(
        "insert into usuarios values(?, ?)",
        usuarios,
    )   # Para prevenir una SQL injection
