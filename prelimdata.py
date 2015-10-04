__author__ = 'Xun'

import json
import pandas as pd

data = []
#Read in multiple objects in a single JSON file
with open('yelp_raw.json') as f:
    for line in f:
        data.append(json.loads(line))
f.close()

#Print out key point for check-up
print data[130872] #Last entry of customers
print data[130873] #First entry of reviews

print data[460943] #Last entry of reviews
print data[460944] #First entry of businesses

#Subset different datasets
customers = data[0:130873]
reviews = data[130873:460944]
business = data[460944:]

#Construct DataFrame for Compilation
customersDF = pd.DataFrame(customers)
reviewsDF = pd.DataFrame(reviews)
businessDF = pd.DataFrame(business)

#Subset Reviews Text Data and sort by Business_id and Date
outputDF = reviewsDF[['business_id', 'date', 'stars', 'text']].sort(['business_id', 'date'], ascending=[1, 1])

#Output Data in CSV file
with open('customersInfo.csv', 'wb') as f:
    customersDF.to_csv(f,header=False, encoding='utf-8', index=False)
f.close()
print 'Customer Info file created'

with open('reviewText.csv', 'wb') as f:
    reviewsDF.to_csv(f,header=False, encoding='utf-8', index=False)
f.close()
print 'Review Text file created'

with open('businessInfo.csv', 'wb') as f:
    businessDF.to_csv(f,header=False, encoding='utf-8', index=False)
f.close()
print 'Business Info file created'

with open('ReviewsForAnalysis.csv', 'wb') as f:
    outputDF.to_csv(f,header=False, encoding='utf-8', index=False)
f.close()
print 'Output Data file created'


