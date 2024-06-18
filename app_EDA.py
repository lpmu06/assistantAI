# Import required libraries

import os
from apikey import apikey

import streamlit as st
import pandas as pd

#from langchain.llms import OpenAI
#from langchain.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv, find_dotenv

#Main

st.title('AI Assistant for Data Science')
st.header('Exploratory Data Analysis Part')
st.subheader('Solution')
st.write('Hello, I am your AI assistant and I am here to help you with your data science projects.')

#Explanation sidebar
with st.sidebar:
    st.write('*Your Data Science Adventure Begins with an CSV File.*')
    st.caption('''**You may already know that every exciting data science journey starts with a dataset.
    That's why I'd love for you to upload a CSV file.
    Once we have your data in hand, we'll dive into understanding it and have some fun exploring it.
    Then, we'll work together to shape your business challenge into a data science framework.
    I'll introduce you to the coolest machine learning models, and we'll use them to tackle your problem. Sounds fun right?**
    ''')