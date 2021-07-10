import mysql.connector


con=mysql.connector.connect(
    host="localhost",
    user="saurav",
    password="1906057",
    database="my_db1",
    port=3306
)

print("hey i think i am connected")


con.close()
