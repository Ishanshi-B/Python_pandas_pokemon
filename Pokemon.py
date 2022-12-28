#Ishanshi Bhardwaj
#Resource Used: https://www.youtube.com/watch?v=vmEHCJofslg

#Loading Data into Pandas
import pandas as pd
df = pd.read_csv('pokemon_data.csv')
print(df.head(3))
print(df.tail(3))

#Reading Data in Pandas
#Read Headers
# df.columns
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 13)

#Read each column
print(df['Name'])
print(df[['Name', 'Type 1']]) #list of column names
print(df.Name)
print(df['Name'][0:5]) #gets the top 5 names

#Reach Each Row
print(df.iloc[1]) #integer location gives everything in the first row
for index, row in df.iterrows():
    print(index,row['Name'])
print(df.loc[df['Type 1'] == "Fire"])#finds specific data that isn't just integer based

#Read a specific location(R,C)
print(df.iloc[2,1])

#Sorting/Describing Data
print(df.describe())
print(df.sort_values(['Type 1','HP'],ascending=[1,0])) # ascending values where type 1 is going a to be and hp is highto low


#Making Changes to the data
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] +df['Sp. Def']+ df['Speed']
df['Total'] = df.iloc[:, 4:10].sum(axis=1) #axis = 1 adds horizontally and axis = 0 adds vertically
cols = list(df.columns.values)
df = df[cols[0:4]+[cols[-1]]+cols[4:12]]
#df = df[['Total','HP','Defense']] #reorders the placement of total
print(df.head(5))

#Saving our data
df.to_csv('modified.csv', index = False) #no index

#to excel
df.to_excel('modified.xlsx', index=False)
df.to_csv('modified.txt', index=False, sep='\t')

#Filtering Data
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)] # | this is OR
new_df = new_df.reset_index()
new_df.reset_index(drop=True, inplace=True) #this resets the index
print(new_df)

print(df.loc[df['Name'].str.contains('Mega')])
print(df.loc[~df['Name'].str.contains('Mega')])

import re #regular expression

print(df.loc[df['Type 1'].str.contains('fire|grass',flags=re.I, regex= True)])
print(df.loc[df['Name'].str.contains('^pi[a-z]*',flags=re.I, regex= True)])

#Conditional Changes
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer' #change the fire to flamer in type 1
#print(df)
df = pd.read_csv('modified.csv')
df.loc[df['Total'] > 500, ['Generation','Legendary']] = ['TEST 1', 'Test 2']
print(df)

#Aggregate Stastics (Groupby)
print(df.groupby(['Type 1']).mean().sort_values('HP', ascending=False))
print(df.groupby(['Type 1']).count())
df['count'] = 1
print(df.groupby(['Type 1']).count()['count'])
print(df)

#Working with large amounts of data
new_df = pd.DataFrame(columns=df.columns)

#loads in chunks
for df in pd.read_csv('modified.csv',chunksize=5):
   print("Chunk df")
   print(df)
for df in pd.read_csv('modified.csv',chunksize=5):
    results = df.groupby(['Type 1']).count()
    new_df = pd.concat([new_df,results])
