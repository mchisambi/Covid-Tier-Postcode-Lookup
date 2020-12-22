import bs4 as bs
import urllib.request
import pandas as pd
import numpy as np
import csv
import xlrd
import lxml
import re

# Reads input file
df = pd.read_csv('Postcodes.csv')
postcodes = df['Postcode'].tolist()

# Creates urls for lookup
x = 0
for i in range(len(postcodes)):
    postcodes[x] = postcodes[x].replace(' ','+')
    x = x + 1

url_root = 'https://www.gov.uk/find-coronavirus-local-restrictions?postcode='
urls = []
print(urls)
x = 0
for i in range(len(postcodes)):
    urls.append(url_root + postcodes[x])
    x = x +1

# Finds tiers and cleans tier text
tiers = []
x = 0
for i in range(len(urls)):
    sauce = urllib.request.urlopen(urls[x]).read()
    soup = bs.BeautifulSoup(sauce)
    tiers.append(soup.find_all('title', limit=1))
    tiers[x] = str(tiers[x])
    tiers[x] = re.search('\n   .(.*?)\n  \n', tiers[x]).group(1)
    x = x + 1

# Adds tier results to dataframe and exports csv
# !!! TO DO: Update path by replacing XXX
df['Tiers'] = tiers
df.to_csv(r'C:\XXX\PostcodeTiersResults.csv', index=False)