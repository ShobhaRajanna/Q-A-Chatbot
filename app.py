import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import os

openai_api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(question):
    try:
        llm = ChatOpenAI(openai_api_key=openai_api_key, model_name = "gpt-3.5-turbo",temperature=0.7)
        response = llm.predict(question)    
        return response
    except Exception as e:
        return f"Error: {str(e)}"


st.set_page_config(page_title="Q&A Demo", page_icon="🧠", layout="wide")

st.header("Q&A Demo")

input_text = st.text_input("Input: ", key="input_text")
response = get_openai_response(input_text)

submit = st.button("Ask a question")

if submit:
    st.subheader("The Response:")
    st.write(response)