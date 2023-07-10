#!/usr/bin/env python
# coding: utf-8

# In[17]:


import requests
import pandas as pd

url = "https://edamam-food-and-grocery-database.p.rapidapi.com/parser"

querystring = {"ingr":"champagne"}

headers = {
    "X-RapidAPI-Key": "bd8c2f188cmshf5d0f1a1c8718c6p1c7f46jsn370366720478",
    "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
}

# Appel à l'API
response = requests.request("GET", url, headers=headers, params=querystring)

# Extraction des 10 premiers produits et création d'un dataframe
products = response.json()["hints"][:10]

# Extract required data from each product
data = []
for product in products:
    food = product['food']
    data.append({
        'foodId': food['foodId'],
        'label': food['label'],
        'category': food['category'],
        'foodContentsLabel': food.get('foodContentsLabel', ''),
        'image': food.get('image', '')
    })

# Create a pandas dataframe from the extracted data
df = pd.DataFrame(data, columns=['foodId', 'label', 'category', 'foodContentsLabel', 'image'])

# Save the dataframe to a CSV file
df.to_csv('products.csv', index=False)


# In[18]:

data = pd.read_csv('products.csv')
data.head()

# In[19]:

data.info()
