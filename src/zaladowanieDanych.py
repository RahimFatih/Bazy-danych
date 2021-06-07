import mysql.connector
import os
from pathlib import Path

mydb = mysql.connector.connect(
    host="localhost", user="root", password="ptc"
)
mycursor = mydb.cursor()


for filename in os.listdir(
    os.path.join(os.path.realpath("."), os.path.realpath("dane"))
):
    if filename.endswith(".csv"):
        with open(os.path.join(os.path.realpath("./dane/" + filename))) as file:
            sql = ""
            val = []
            for i, line in enumerate(file):
                if i == 0:
                    sql = "INSERT INTO BD." + filename[:-4] + " (" + line + ") VALUES (%s"
                    for columns in range(len(line.split(",")) - 1):
                        sql = sql + ", %s"
                    sql = sql + ")"
                else:
                    val.append(line.rstrip().split(","))
                    fin = (*val, )
            mycursor.executemany(sql, fin)
    else:
        continue
mydb.commit()
print(mycursor.rowcount, "record inserted.")
# print(mydb)
