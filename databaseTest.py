import mysql.connector

conn=mysql.connector.connect(host="localhost",username="root",password="W@2915djkq#",database="face_recognition")
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()