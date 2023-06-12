#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Description: This is a stock market dashboard to show some charts and data on some stock


# In[14]:


#import libraries
import streamlit as st
import pandas as pd
from PIL import Image
import datetime
import numpy as np
import pkgutil


# In[15]:


#Add a title and an Image
st.write("""
#Stock Market Web application
#Visually show data on a stock! Data range from Jan 2, 2020 - Aug 4, 2020""")


# In[16]:


image = Image.open(r"C:\Users\acer\Desktop\python practice\stock-market-design-of-bull-and-bear-vector-22540385.jpg")
st.image(image, use_column_width=True)


# In[17]:


#Create a sidebar header
st.sidebar.header('User Input')


# In[18]:


#Create a function to get the users input
def get_input():
    start = st.sidebar.text_input("Start Date", "2020-01-02")
    end = st.sidebar.text_input("End Date", "2020-08-04")
    symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    return start, end, symbol


# In[19]:


#Create a function to get the company name
def get_company_name(symbol):
    if symbol == 'AMZN':
      return 'Amazon'
    elif symbol == 'TSLA':
      return 'Tesla'
    elif symbol == 'GOOG':
      return 'Alphabet'
    else:
        'None'
        


# In[20]:


#Create a function to get the proper company data and the proper timeframe from the user start date to the user end date

def get_date(symbol, start, end):
    
    #load the data
    if symbol.upper() == 'AMZN':
        df = pd.read_csv(r"C:\Users\acer\Downloads\AMZN.csv")
    elif symbol.upper() == 'TSLA':
        df = pd.read_csv(r"C:\Users\acer\Downloads\TSLA.csv")
    elif symbol.upper() == 'GOOG':
        df = pd.read_csv(r"C:\Users\acer\Downloads\GOOG.csv")
    else:
        df = pd.DataFrame(columns = ['Date', 'Close', 'Open', 'Volume', 'Adj Close', 'High', 'Low'])


# In[21]:


#Get the date range
import datetime
 
start = datetime.datetime.strptime("2020-01-02", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-08-04", "%Y-%m-%d")


# In[22]:


#set the start and ebd index rows both to 0
start_row = 0
end_row = 0


# In[23]:


files = ('C:/Users/acer/Downloads/AMZN.csv', 'C:/Users/acer/Downloads/TSLA.csv', 'C:/Users/acer/Downloads/GOOG.csv')
dfs = []
for file in  files:
    dfs.append( pd.read_csv(file))
    print(dfs[len(dfs)-1].shape)
    print(dfs[len(dfs)-1].dtypes)
print (dfs[2])


# In[24]:


import yfinance as yf
tickerSymbol = 'AMZN'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='Date', start='2020-02-01', end='2020-08-04')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
#Get some statistics on the data
st.header('Data Statistics')
st.write(tickerDf.describe())


# In[ ]:





# In[ ]:




