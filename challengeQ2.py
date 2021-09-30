import csv
import pandas as pd
import statistics

df = pd.read_csv(r'airbnb_listings.csv')

flatbookRatings, jasonRatings = [], []

for index, row in df.iterrows():
    if row['host_name'] == 'Flatbook':
        x = row['review_scores_value']
        flatbookRatings.append(x)

    elif row['host_name'] == 'Jason':
        y = row['review_scores_value']
        jasonRatings.append(y)

print(statistics.mean(flatbookRatings))
print(statistics.mean(jasonRatings))
        