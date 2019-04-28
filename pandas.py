import pandas as pd
df=pd.read_csv('/home/ganaparti/Downloads/heart.csv')
print (df)
df1=pd.DataFrame(data=df)
print (df1)
df1.to_excel("/home/ganaparti/Downloads/heartt.xlsx")
df2=pd.read_excel('/home/ganaparti/Downloads/heartt.xlsx')
print (df2)
