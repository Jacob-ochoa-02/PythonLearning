# import time

# print(time.time())  # Respecto a UTC
# timestamp, cuenta los segundos que han pasado desde el
# 1ro de enero de 1970
# import datetime

# fecha = datetime.datetime(2023,5,27)  #-> forma "tediosa"
# print(datetime)

from datetime import datetime

fecha = datetime(2023, 5, 27)
fecha2 = datetime(2023, 6, 27)
ahora = datetime.now()
# print(fecha)
# print(ahora)
fechaStr = datetime.strptime("2023-01-03", "%Y-%m-%d")
# el segundo argumento se llaman directives, se usan para indicar cómo
# queremos crear este objeto de fecha
print(ahora.strftime("%Y-%m-%d"))
print(fecha > fecha2)
print(
    ahora.year,
    ahora.month,
    ahora.day,
    ahora.hour,
    ahora.minute,
    ahora.second
)
