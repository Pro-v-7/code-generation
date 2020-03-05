import pandas as pd
df=pd.read_csv('qna.csv')
df=df.drop_duplicates(keep='first')
df.to_csv('qna_all.csv',index=False,header=False)
