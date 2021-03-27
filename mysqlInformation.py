import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="finalProject",
  port="3307"
)

cursor = mydb.cursor()