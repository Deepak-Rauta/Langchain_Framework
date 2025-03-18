import os
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

# call the environment variables
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
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
st.title("Langchian Demo with Gemini AI API")
input_text = st.text_input("Search the topic you want")

# Gemini AI LLM Call
llm = GoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=os.getenv("GEMINI_API_KEY"))
output_parser = StrOutputParser()

# chain
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))