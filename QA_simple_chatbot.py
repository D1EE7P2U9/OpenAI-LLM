# Q&A chatbot
from langchain.llms import openai
from dotenv import load_dotenv
import os

load_dotenv()

import streamlit as st



##Function to load OpenAI model and get response

def get_oepnai_response(question):
    llm = openai(openai_api_key = os.getenv('OPEN_API_KEY'),model_name='text-davinci-003',temperature=0.5)
    response = llm(question)
    return response

##initialise streamlit app
    
st.set_page_config(page_title='Q&A Demo')
st.header("Langchain application")

input = st.text_input("Input:",key='input')

response = get_oepnai_response(input)

submit = st.button('Ask the Question')

#If ask button is clicked

if submit:
    st.subheader('the Response is')
    st.write(response)
