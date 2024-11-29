# integrate the Gemini AI
from constants import GOOGLE_API_KEY
import getpass
import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",google_api_key=GOOGLE_API_KEY)



st.title('Langchain Demo with Gemini AI')
input_text = st.text_input("Search the topic u want here")
output = llm.invoke(input_text)
st.write(output.content)

