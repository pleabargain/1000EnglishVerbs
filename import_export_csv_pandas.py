#using pandas
# pandas 1.2.2

import pandas as pd

#df = pd.read_csv(r'1000verbs.csv')

#this prints all of the file
# print(df)

data = pd.read_csv(r'1000verbs.csv')
data.dropna(inplace = True) 

df = pd.DataFrame(data,columns=['Past_Participle'])
#print(df)

some_text = "Here is a past participle verb: "
# df1 = 'str  ' + df['Past_Participle'].map(str) 

# df1.to_csv("past_part.csv")

df1 = some_text + df['Past_Participle'].map(str) + '\nTry to use it in a sentence.'
# print(df1)
df1.to_csv("past_part.csv")




#this didn't work
# print(f"{some_text}", df1)

#output="Here is a verb "+ df1
#print(output)



