import streamlit as st
import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ.get("OPENAI_SECRET_KEY")


def generate_article(input):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Summarize the following article"+ input,
        temperature=0.5,
        max_tokens=530,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response


st.title("Generate your own Article under 2 Minutes")

input = st.text_area('Enter a short description of an idea for which you want to generate an article :')

generate = st.button('Generate',key='generate')
if generate:
    generated_text = generate_article(input)
    st.write(generated_text.choices[0].text)

