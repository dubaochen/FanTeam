# -*- coding:utf-8 -*-
import pandas as pd
uplist = []
lowlist = []

df = pd.read_csv("predicted.csv")
for i in range(1,1983):
    print("++++++++group:%s+++++++"%i)
    dt = df.loc[df.group==i]
    mean = dt.describe()['tag'][1]
    uplimit = dt['time'].iloc[0]
    lowlimit = dt['time'].iloc[-1]
    if mean<0.2:
        uplist.append(uplimit)
        lowlist.append(lowlimit)

up = []
low = []
low_num = 0.0
up_num = uplist[0]
for i in range(1,len(uplist)):
    if uplist[i]-lowlist[i-1]==1:
        low_num = lowlist[i]
    else :
        up.append(up_num)
        low.append(low_num)

pS1 = pd.Series(up,name="startTime")
pS2 = pd.Series(low,name="endTime")
df = pd.concat([pS1,pS2],axis=1)
print(df)
df.to_csv("test_1_results.csv",index=None)

