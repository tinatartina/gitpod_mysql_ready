#es1

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost";
  user="root";
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

#es2

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost";
  user="root",
  password="";
  database="mydatabase"
)