# --------------
import pandas as pd 
import numpy as np

# Read the data using pandas module.
data=pd.read_csv(path)

# Find the list of unique cities where matches were played
print("The unique cities where matches were played are ", data.city.unique())
print('*'*80)
# Find the columns which contains null values if any ?
print("The columns which contain null values are ", data.columns[data.isnull().any()])
print('*'*80)
# List down top 5 most played venues
print("The top 5 most played venues are", data.venue.value_counts().head(5))
print('*'*80)
# Make a runs count frequency table
print("The frequency table for runs is", data.runs.value_counts())
print('*'*80)
# How many seasons were played and in which year they were played 
data['year']=data.date.apply(lambda x : x[:4])
seasons=data.year.unique()
print('The total seasons and years are', seasons)
print('*'*80)
# No. of matches played per season
ss1=data.groupby(['year'])['match_code'].nunique()
print('The total matches played per season are', ss1)
print("*"*80)
# Total runs across the seasons
ss2=data.groupby(['year']).agg({'total':'sum'})
print("Total runs are",ss2)
print("*"*80)
# Teams who have scored more than 200+ runs. Show the top 10 results
w1=data.groupby(['match_code','batting_team']).agg({'total':'sum'}).sort_values(by='total', ascending=False)
w1[w1.total>200].reset_index().head(10)
print("The top 10 results are",w1[w1.total>200].reset_index().head(10))
print("*"*80)
# What are the chances of chasing 200+ target
dt1=data.groupby(['match_code','batting_team','inning'])['total'].sum().reset_index()
dt1.head()
dt1.loc[((dt1.total>200) & (dt1.inning==2)),:].reset_index()
data.match_code.unique().shape[0]
probability=(dt1.loc[((dt1.total>200) & (dt1.inning==2)),:].shape[0])/(data.match_code.unique().shape[0])*100
print("Chances are", probability)
print("*"*80)
# Which team has the highest win count in their respective seasons ?
dt2=data.groupby(['year','winner'])['match_code'].nunique()
dt3=dt2.groupby(level=0,group_keys=False)
dt4=dt3.apply(lambda x: x.sort_values(ascending=False).head(1))
print("The team with the highes win count is", dt4)


