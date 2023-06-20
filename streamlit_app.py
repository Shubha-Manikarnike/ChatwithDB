import os
from langchain.agents import *
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
from langchain.chat_models import ChatOpenAI
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
import streamlit as st

db_user = "postgres"
db_password = "Pass1234"
db_host = "database-1.cojmud51692g.us-east-1.rds.amazonaws.com"
db_name = "postgres"
db = SQLDatabase.from_uri(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}/{db_name}")
#db = SQLDatabase.from_uri(f"postgresql+psycopg2://postgres:{env('DBPASS')}@localhost:5432/{env('DATABASE')}",)
os.environ['OPENAI_API_KEY'] = "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"

QUERY = """
Given an input question, first create a syntactically correct postgresql query to run, then look at the results of the query and return the answer.
Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here

{question}
"""

# Setup the database chain
def get_prompt(prompt):
    print("Type 'exit' to quit")

    try:
        question = QUERY.format(question=prompt)
        print(db_chain.run(question))
        return db_chain.run(question)
    except Exception as e:
        print(e)
        return e

def generate_response(txt):
    # Instantiate the LLM model
    llm = OpenAI(temperature=0, openai_api_key=os.environ['OPENAI_API_KEY'])
    #db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)
    # Split text
    #get_prompt()
    #return get_prompt(txt)
    return "Hello World"

# Page title
st.set_page_config(page_title='🦜🔗 Chat with your DB')
st.title('🦜🔗 Chat with your DB')
# Text input
txt_input = st.text_area('Enter your text', '', height=200)
# Form to accept user's text input for summarization
result = []
with st.form('chatwithDB_form', clear_on_submit=True):
    #openai_api_key = st.text_input('OpenAI API Key', type = 'password', disabled=not txt_input)
    submitted = st.form_submit_button('Submit')
    if submitted:
        with st.spinner('Calculating...'):
            response = generate_response(txt_input)
            result.append(response)
if len(result):
    st.info(response)    