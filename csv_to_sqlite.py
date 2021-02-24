# open a csv file
# import csv into python
# create a dbase in sqlite
# open the database
# write the csv data to sqlite
# close the data base
# for dbase processing remember that headers with spaces is unwelcome!

import  sqlite3
import csv

conn = sqlite3.connect('enverbs.sqlite')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS enverbs')
c.execute('''
        CREATE TABLE "enverbs"(
            "Word" TEXT,
            "third_singular" TEXT,
            "Present_Participle" TEXT,
            "Simple_Past" TEXT,
            "Past_Participle" TEXT
        )
        ''')

fname=input("enter csv name: ")
if len(fname) <1 : fname="1000verbs.csv"

with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
        print(row)
        Word=row[0]
        third_singular=row[1]
        Present_Participle=row[2]
        Simple_Past=row[3]
        Past_Participle=row[4]
        c.execute('''INSERT INTO enverbs(Word,
        third_singular,
        Present_Participle,
        Simple_Past,
        Past_Participle)
        VALUES(?,?,?,?,?)''',(Word,third_singular,Present_Participle,Simple_Past,Past_Participle))
        conn.commit()

