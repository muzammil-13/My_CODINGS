import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM yourtable")
result = mycursor.fetchall()

for row in result:
    print(row)

# mycursor.close()
# mydb.close()
