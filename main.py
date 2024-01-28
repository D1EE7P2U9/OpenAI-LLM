#Integrate our code with OpenAI API
import os 
from constants import openai_key
# from langchain.llms import openai
from langchain_openai import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory

import streamlit as st

os.environ['OPENAI_API_KEY'] = openai_key

#Initialize streamlit framework

st.title('Celebrity Search Results')
input_text = st.text_input('Search the topic you want')

#prompt_template
first_input_prompt = PromptTemplate(
    input_variables = ['Name'],
    template = 'tell me about {Name}'
    )

#memory
person_memory = ConversationBufferMemory(input_key='Name',memory_key='chat_history')
dob_memory = ConversationBufferMemory(input_key='Person',memory_key='chat_history')
descr_memory = ConversationBufferMemory(input_key='dob',memory_key='description_history')


#openai LLMS
llm = OpenAI(temperature=0.8)
chain = LLMChain(llm=llm,prompt = first_input_prompt,verbose=True,output_key='Person',memory=person_memory)

#2nd template
second_input_prompt = PromptTemplate(
    input_variables = ['Person'],
    template = 'When was {Person} born'
    )

chain2 = LLMChain(llm=llm,prompt = first_input_prompt,verbose=True,output_key='dob',memory=dob_memory)


#3rd template
third_input_prompt = PromptTemplate(
    input_variables = ['dob'],
    template = 'Mention 5 major events happened around {dob} in the world'
    )

chain3 = LLMChain(llm=llm,prompt = first_input_prompt,verbose=True,output_key='description',memory=descr_memory)

parent_chain = SequentialChain(chains=[chain,chain2],input_variables = ['name'],out_put_variables=['person','dob','description'],verbose=True)

if input_text:
    st.write(parent_chain({'Name':input_text}))

    with st.expander('Person Name'):
        st.info(person_memory.buffer)

    with st.expander('Major Events'):
        st.info(descr_memory.buffer)