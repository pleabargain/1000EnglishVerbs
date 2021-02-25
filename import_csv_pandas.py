#using pandas
# 
import pandas as pd

#df = pd.read_csv(r'1000verbs.csv')

#this prints all of the file
# print(df)

data = pd.read_csv(r'1000verbs.csv')
df = pd.DataFrame(data,columns=['Past_Participle'])
#print(df)

some_text = "Here is a verb"
df1 = df [  'Past_Participle'].map(str) 
#this didn't work
# print(f"{some_text}", df1)

print("Here is a verb "+ df1)
