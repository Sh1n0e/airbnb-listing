# This file's purpose is to take the csv file and populate the database

import pandas as pd
import sqlite3

conn = sqlite3.connect('airbnb.db')

header_list = ['id', 'name', 'host_name', 'neighbourhood', 'room_type', 'price', 'number_of_reviews']

df = pd.read_csv('listings.csv', usecols=header_list)

df['url'] = 'https://www.airbnb.com/rooms/' + df['id'].astype(str)

# Going to work with sqlite for now to ensure how database works serverlessly then will transition into using postgreSQL

df.to_sql('listings', conn, if_exists='replace', index=False)
conn.close()

"""
Test case writing data into html, this is just for testing purposes
html = df.to_html()

with open('listings.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Printing completed now view the HTML file to see a clear table")
"""





