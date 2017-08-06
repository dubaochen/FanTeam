# -*- coding:utf-8 -*-
import pandas as pd
import datetime
df = pd.read_csv('15/15_data.csv', encoding='utf-8')
df['time'] = pd.to_datetime(df['time'])
df['tag'] = ''

#打1标签
timedf = pd.read_csv('15/15_normalInfo.csv',encoding="utf-8")
timedf['startTime'] = pd.to_datetime(timedf['startTime'])
timedf['endTime'] = pd.to_datetime(timedf['endTime'])
startlist = pd.Series(timedf['startTime'])
endlist = pd.Series(timedf['endTime'])

for i in range(0,len(startlist)):
    print(startlist[i])
    print(endlist[i])
    df.loc[((df['time']<=endlist[i]) & (df['time']>=startlist[i])),'tag']=1

#打0标签
timedf = pd.read_csv('15/15_failureInfo.csv',encoding="utf-8")
timedf['startTime'] = pd.to_datetime(timedf['startTime'])
timedf['endTime'] = pd.to_datetime(timedf['endTime'])
startlist = pd.Series(timedf['startTime'])
endlist = pd.Series(timedf['endTime'])

for i in range(0,len(startlist)):
    print(startlist[i])
    print(endlist[i])
    df.loc[((df['time']<=endlist[i]) & (df['time']>=startlist[i])),'tag']=0

df.to_csv("15/15_addTag.csv",encoding="utf-8")


