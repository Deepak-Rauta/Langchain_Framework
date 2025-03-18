📌 Project 1: LangChain with Gemini AI

This project builds a chatbot using Google's Gemini AI with LangChain and Streamlit for a simple UI.

🔹 Steps Involved
Load Environment Variables:

Using dotenv to load API keys (GEMINI_API_KEY, LANGCHAIN_API_KEY).
Define a Prompt:

Uses ChatPromptTemplate to structure user queries.
Defines the chatbot as a "helpful assistant."
Set Up LangChain with Gemini AI:

Initializes GoogleGenerativeAI(model="gemini-pro").
Create a Processing Chain:

Combines Prompt → Gemini AI → Output Parsing.
Uses StrOutputParser() to extract responses from Gemini.
Build a UI with Streamlit:

Displays a text box (st.text_input()) for user input.
Calls the LangChain pipeline (chain.invoke()) when the user enters a query.
