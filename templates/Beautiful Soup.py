import requests
from bs4 import BeautifulSoup

url = 'https://codewithharry.com'
# Step 1 Get the HTML file
# Step 3 HTML Tree traversal
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2 Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)
title = soup.title
print(title)
