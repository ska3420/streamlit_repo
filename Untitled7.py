#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications import imagenet_utils


# In[4]:


model = tf.keras.applications.MobileNetV2()


# In[5]:


st.title("Image Classification")
st.write("Upload an image for classification.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("")
    st.write("Classifying...")

    image = image.resize((224, 224))  # Resize the image to match the input size of the model
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.keras.applications.mobilenet.preprocess_input(image)
    image = tf.expand_dims(image, axis=0)

    preds = model.predict(image)
    results = imagenet_utils.decode_predictions(preds, top=3)[0]

    st.write("Predictions:")
    for result in results:
        st.write(f"{result[1]}: {round(result[2] * 100, 2)}%")


# In[ ]:





# In[ ]:




