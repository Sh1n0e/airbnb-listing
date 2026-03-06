import pandas as pd 

"""
pd.options.display.max_rows = 3

df = pd.read_csv('listings.csv')

print(df)
"""

df = pd.read_csv('listings.csv')

html = df.to_html()

with open('listings.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Printing completed now view the HTML file to see a clear table")