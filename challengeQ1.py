import csv
import pandas as pd
from pandas.core.frame import DataFrame

df = pd.read_csv(r'airbnb_listings.csv')

'''Assuming all the Airbnbs are at the same location, I would use a series of filters to recommend the best room depending on the customer's wants/needs (customer-end):
- How many nights are you staying? (minimum_nights <= # <= maximum nights)
- How many people are staying? (accomodation)
- What daily price range are you looking for (price)
- High user review (review_scores_value) and high number of reviewers (number_of_reviews)

Then, after applying these filters, I would then try to find the best hosts with the following traits (host-end):
- Flexible cancellation policy
- The host has served as an Airbnb host for a high number of days
- Low response time
- High response rate

Like so, using a series of data filters on both customer- and host-end, I would recommend the best listings for the customer
'''

# Client end

numNights = int(input("How many nights are you staying: "))
numPeople = int(input("How many people are staying: "))
maxPrice = int(input("What is the maximum daily price you can accept? "))
# assume 9+ is high review

# for index, row in df.iterrows():
#     if numNights < row['minimum_nights'] | numNights > row['maximum_nights']:
#         df2 = df.drop(index, inplace=True)

df2 = df[df['minimum_nights'] <= numNights]
df3 = df2[df2['maximum_nights'] >= numNights]
df4 = df3[df3['accommodates'] >= numPeople]
df5 = df4[df4['price'] <= maxPrice]
df6 = df5[df5['review_scores_value'] >= 9]   


# Host end - sort rows in dataframe

df6.sort_values(['review_scores_value','cancellation_policy', 'host_for_x_days','host_response_time', 'host_response_rate'], ascending=[True, False, True, False, True])

print(df6)
df6.to_excel('best airbnb selections for you.xlsx')






