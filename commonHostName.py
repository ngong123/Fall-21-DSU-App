import csv
import pandas as pd

# Read csv file with pandas
df = pd.read_csv(r'airbnb_listings.csv')

# Q2 Get 2nd most common host_name and numListings
print(df['host_name'].value_counts())
# Jason, 25 listings

# Q3 Get number of unique host_id given host_name == Jason


jasonIDs = []
for index, row in df.iterrows():
    if row['host_name'] == 'Jason' and row['host_id'] not in jasonIDs:
        jasonIDs.append(row['host_id'])
print(len(jasonIDs))
# 7 unique Jasons
