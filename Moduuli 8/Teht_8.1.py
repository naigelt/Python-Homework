import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port= 3306,
    database= "flight_game",
    user="root",
    password="",
    autocommit=True
)

ICAO = input("Anna lentokentän ICAO-Koodi : ")
sql = "SELECT name, municipality FROM airport WHERE ident = '" +ICAO + "'"
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()
for line in result:
    print(f"{line[0]}, {line[1]}")
