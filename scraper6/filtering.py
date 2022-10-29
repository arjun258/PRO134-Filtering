import pandas as pd
import matplotlib.pyplot as plt
import csv
# df['Distance']=df['Distance'].astype('float')
df = pd.read_csv('./gravityAdded.csv')

gravity = df['Gravity'].tolist()
support_distance = []

df['Distance']=df['Distance'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
distance = df['Distance'].tolist()
for i in distance:
  if(i<100):  
    support_distance.append(i)

gravity = df['Gravity'].tolist()
support_gravity=[]
for i in gravity:
    if(i>149):
        support_gravity.append(i)

# df[support_distance]=df[support_distance].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')



