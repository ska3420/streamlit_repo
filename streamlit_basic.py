#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[2]:


st.code("st.text()", language='python')
st.text('Apurva blog')
st.code("st.markdown()", language='python')
st.markdown('# This is Heading 1 in Markdown')
st.code("st.title()", language='python')
st.title('This is a title')
st.code("st.header()", language='python')
st.header('Header')
st.code("st.subheader()", language='python')
st.subheader('Sub Header')
st.code("st.latex()", language='python')
st.latex(r'''
...      ''')
st.code("st.write()", language='python')
st.write('Can display many things')

