#Import required libraries

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

with st.sidebar:
    st.write('''
             ''')