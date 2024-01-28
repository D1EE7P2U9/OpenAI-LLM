# #Integrate our code with OpenAI API
# import os 
# from constants import openai_key
# # from langchain.llms import openai
# from langchain_openai import OpenAI

# import streamlit as st

# os.environ['OPENAI_API_KEY'] = openai_key

# #Initialize streamlit framework

# st.title('Langchain Demo with OPENAI API')

# input_text = st.text_input('Search the topic you want')

# #openai LLMS
# llm = OpenAI(temperature=0.8)

# if input_text:
#     st.write(llm(input_text))




#################################################


# #Integrate our code with OpenAI API
# import os 
# from constants import openai_key
# # from langchain.llms import openai
# from langchain_openai import OpenAI
# from langchain import PromptTemplate
# from langchain.chains import LLMChain

# import streamlit as st

# os.environ['OPENAI_API_KEY'] = openai_key

# #Initialize streamlit framework

# st.title('Celebrity Search Results')
# input_text = st.text_input('Search the topic you want')

# #prompt_template
# first_input_prompt = PromptTemplate(
#     input_variables = ['Name'],
#     template = 'tell me about {Name}'
#     )


# #openai LLMS
# llm = OpenAI(temperature=0.8)
# chain = LLMChain(llm=llm,prompt = first_input_prompt,verbose=True)

# if input_text:
#     st.write(chain.run(input_text))