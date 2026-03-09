import pandas as pd 

header_list = ['name', 'host_name', 'neighbourhood', 'room_type', 'price', 'number_of_reviews']

df = pd.read_csv('listings.csv', usecols=header_list)

# print(df)

html = df.to_html()

with open('listings.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Printing completed now view the HTML file to see a clear table")


# Seeing if I can print based on separate variables


