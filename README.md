📌 Project 1: LangChain with Gemini AI

This project builds a chatbot using Google's Gemini AI with LangChain and Streamlit for a simple UI.

🔹 Steps Involved

Load Environment Variables:

Using dotenv to load API keys (GEMINI_API_KEY, LANGCHAIN_API_KEY).

Define a Prompt:

Uses ChatPromptTemplate to structure user queries.

Defines the chatbot as a "helpful assistant."

Set Up LangChain with Gemini AI:

Initializes GoogleGenerativeAI(model="gemini-1.5-pro").

Create a Processing Chain:

Combines Prompt → Gemini AI → Output Parsing.

Uses StrOutputParser() to extract responses from Gemini.

Build a UI with Streamlit:

Displays a text box (st.text_input()) for user input.


📌 Project 2: LangChain with Llama 2 (via Ollama)

This project replaces Gemini with Llama 2, running locally via Ollama.

🔹 Steps Involved

Set Up Ollama:

Install Ollama on your system.

then run:

ollama run llama2

Define a Prompt:

Same as Gemini, using ChatPromptTemplate.

Set Up LangChain with Llama 2:

Uses Ollama(model="llama2") instead of Google Gemini.

Create a Processing Chain:

Links Prompt → Llama 2 → Output Parsing.

Build UI with Streamlit:

Takes user input and runs it through Llama 2.

Calls the LangChain pipeline (chain.invoke()) when the user enters a query.
