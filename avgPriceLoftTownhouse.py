# Q4
import csv
import pandas as pd
from scipy import stats as st
# Read csv file with pandas
df = pd.read_csv(r'airbnb_listings.csv')

# print(df['property_type'].value_counts())
# Townhouse           17
# Loft                13

loftPrices, townhousePrices = [], []
# Get average daily price of all townhouses/lofts.
for index, row in df.iterrows():
    if row['property_type'] == 'Loft':
        x = row['price']
        loftPrices.append(x)
    
    elif row['property_type'] == 'Townhouse':
        y = row['price']
        townhousePrices.append(y)


dfLoftPrices = pd.DataFrame(loftPrices)
loft = dfLoftPrices.to_numpy()

dfTownhousePrices = pd.DataFrame(townhousePrices)
th = dfTownhousePrices.to_numpy()

ttest = st.ttest_ind(a=loft, b=th, equal_var=True)
print("fuck u")
# statistic=array([0.69836398]), pvalue=array([0.49070955

# manual check using Ti84
print(dfLoftPrices.describe())
print(dfTownhousePrices.describe())
# t statistic value = 0.732, p = 0.469
