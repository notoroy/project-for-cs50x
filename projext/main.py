from bs4 import BeautifulSoup
import requests
import re
import pandas as pd



url = 'https://en.wikipedia.org/wiki/List_of_companies_of_Kenya'
response = requests.get(url).text
soup = BeautifulSoup(response , 'lxml')

table = soup.find('table')

rows = table.find_all('tr')

columns = [v.text.replace('\n' , '') for v in rows[0].find_all('th')]

df = pd.DataFrame(columns=columns)

for i in range(1 , len(rows)):
    tds = rows[i].find_all('td')

    value = [td.text.replace('\n','') for td in tds]

    df = df.append(pd.Series(value, index=columns) , ignore_index=True)
    
    df.to_csv('companies.csv')

































