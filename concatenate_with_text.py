#concatenate with text

import  sqlite3
import csv

conn_dB = sqlite3.connect('enverbs')
cursor = conn_dB.cursor()
cursor.execute("SELECT Past_Participle || ' some text ' as Past_Participle from enverbs")

items = cursor.fetchall()


for item in items:
    print("verbs:\t "+ item[0])

conn_dB.commit()
cursor.close()