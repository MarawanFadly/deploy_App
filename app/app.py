import streamlit as st    # streamlit run app/app.py
from google import genai  # pip install google-genai
import os

#client = genai.Client( api_key= os.getenv('GEMINI_API_KEY') )

client = genai.Client(api_key="AIzaSyDQMpwtvPZThspLKJ5KOEvC36vtC7avZWk")
st.header( 'Our First Chatbot' )

user_input = st.text_area( 'Enter your text' )

# create a simple button to handle requests
if st.button( 'Send' ) :
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=user_input,
    )

    st.write( response.text )