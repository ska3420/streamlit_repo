#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
from streamlit import set_page_config
import os
import numpy as np
import pandas as pd
from PIL import Image


# In[6]:


# Custom function to set the page style
def set_custom_style():
    # Page layout
    st.markdown(
        """
        <style>
        .reportview-container {
            background: linear-gradient(to bottom, #f2f2f2, #e6e6e6);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # Custom CSS
    st.markdown(
        """
        <style>
        /* Add your custom CSS here */
        body {
            color: #333;
            font-family: Arial, sans-serif;
        }
        .stButton>button {
            background-color: #008CBA;
        }
        .stTextInput>div>div>input {
            background-color: #f2f2f2;
            color: #333;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# In[15]:


def main():
    set_page_config(page_title="Project App", page_icon="🚀")

    # Set custom style
    set_custom_style()

    st.title("My Projects Showcase 📚")

    # Dictionary containing project names as keys and their corresponding GitHub URLs and image URLs as values
    projects_data = {
        "E-commerce Analysis: Customer Behavior and Delivery performance": {
            "github_url": "https://github.com/ska3420/Analysis_of_customer_behavior_on_Ecommerce-data",
            "image_url": Image.open("C:/Users/HP/Desktop/Python_practice/streamlit/ecommerce - photo.PNG")
        },
        "Outlet- sales- analysis": {
            "github_url": "https://github.com/ska3420/BigMart-Outlet-Sales-Analysis-and-Predictions",
            "image_url": Image.open("C:/Users/HP/Desktop/Python_practice/streamlit/bigmart.PNG")
        },
        "streamlit small repositry": {
            "github_url": "https://github.com/ska3420/streamlit_repo",
            "image_url": Image.open("C:/Users/HP/Desktop/Python_practice/streamlit/streamlit.PNG")
        },
        "SQL Project 1": {
            "github_url": "https://github.com/ska3420/Music_store_analysis",
            "image_url": Image.open("C:/Users/HP/Desktop/Python_practice/streamlit/music.PNG")
        }
        # Add more projects as needed
    }

    # Project selection using selectbox
    selected_project = st.selectbox("Select a project:", list(projects_data.keys()))

    # Display GitHub link 
    st.header("GitHub Repository")
    github_url = projects_data[selected_project]["github_url"]
    st.markdown(f"Check out the GitHub repository: [{github_url}]({github_url})")

    st.image(projects_data[selected_project]["image_url"], caption=selected_project, use_column_width=True)

    # Data visualization dashboards
    st.header("Data Visualization Dashboards 🎨🎨")
    
    st.title("Dashboard 1")
    plot1 = Image.open("F:/apurva documents/dashboard/sales.PNG")
    st.image(plot1, use_column_width=True)
    
    st.title("Dashboard 2")
    plot2 = Image.open("F:/apurva documents/dashboard/stock analysis.PNG")
    st.image(plot2, use_column_width=True)
    
    st.title("Dashboard 3")
    plot3 = Image.open("F:/apurva documents/dashboard/H&M trend.PNG")
    st.image(plot3, use_column_width=True)
    
    st.title("Dashboard 4")
    plot4 = Image.open("F:/apurva documents/dashboard/earthquake.PNG")
    st.image(plot4, use_column_width=True)
    
    st.title("Dashboard 5")
    plot5 = Image.open("F:/apurva documents/dashboard/Ad_detail_Dashboard.PNG")
    st.image(plot5, use_column_width=True)
    
if __name__ == "__main__":
    main()


# In[ ]:




