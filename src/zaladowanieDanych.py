#import mysql.connector
import os
from pathlib import Path

#mydb = mysql.connector.connect(
#  host="localhost",
#  user="yourusername",
#  password="yourpassword"
#)

for filename in os.listdir(Path('.\dane')):
    if filename.endswith(".csv"): 
        print(filename)
        continue
    else:
        continue

#print(mydb)