import mysql.connector

# yhdeyden avaus
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password= '',
         autocommit=True
         )
#   määritellään kysely
areacode = input("Kirjoita maakoodi")
sql = "SELECT type, COUNT(*) FROM airport WHERE iso_country = '" + areacode + "' GROUP BY TYPE"

# suoritetaan kysely
cursor = connection.cursor()
cursor.execute(sql)

result = cursor.fetchall()
for rivi in result:
    print(f"{rivi[0]}, {rivi[1]}")