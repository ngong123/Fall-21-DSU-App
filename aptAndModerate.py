import csv
import pandas as pd

# Read csv file with pandas
df = pd.read_csv(r'airbnb_listings.csv')
# print(df)
numEntries = len(df)


# Count occurences of conditions:
# property_type == Apartment and cancellation_policy == 2 (moderate)

count = 0
for index, row in df.iterrows():
    if row['property_type'] == 'Apartment' and row['cancellation_policy'] == 2:
        count+=1
ans = round(count/numEntries, 3)
print(ans)

# 0.201


