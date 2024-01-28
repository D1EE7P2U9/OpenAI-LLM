#Integrate our code with OpenAI API
import os 
from constants import openai_key
# from langchain.llms import openai
from langchain_openai import OpenAI

import streamlit as st

os.environ['OPENAI_API_KEY'] = openai_key

#Initialize streamlit framework

st.title('Langchain Demo with OPENAI API')

input_text = st.text_input('Search the topic you want')

#openai LLMS
llm = OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))