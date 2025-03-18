import os
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from dotenv import load_dotenv
load_dotenv()
# Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# creating chatbot
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. please provide response to the user quries"),
        ("user", "Question: {question}")
    ]
)

# Streamlit framework
st.title("Langchian Demo with llama2 API")
input_text = st.text_input("Search the topic you want")

# Gemini AI LLM Call
llm = Ollama(model="llama2")
output_parser = StrOutputParser()

# chain
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))