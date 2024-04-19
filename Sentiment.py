# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:55:11 2024

@author: Ajay
"""

 
from transformers import pipeline
import streamlit as st

pipe = pipeline('text-classification')

st.title('Sentiment Analysis')

user_input = st.text_input('Enter Your text: ')

if st.button("Get Sentiment"):
    if user_input:
        result = pipe(user_input)
        
        st.write("Sentiment: ", result[0]['label'])