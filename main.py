import streamlit as st
import os
import openai
from dotenv import load_dotenv


load_dotenv() 
col1, col2 = st.columns(2,gap='large')
token = os.environ.get("OPENAI_SECRET_KEY")
openai.api_key = token
natural_languages = ["English","Hindi", "Spanish", "French", "German", "Italian", "Dutch", "Portuguese", "Japanese", "Korean", "Chinese (Simplified)", "Chinese (Traditional)"]
def grammar_check(input):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Correct this to standard English:\n\n"+input,
        temperature=0,
        max_tokens=530,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response

def generate_summary(input):
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

def translate(input, target_language):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Translate the exact input into "+ target_language+":"+input,
        temperature=0.5,
        max_tokens=530,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response

with col1:
    st.header("Scribble Spot: ")
    input = st.text_area("Enter your article here",key='input')
    submitted = st.button('Submit',key='submit')
    if submitted:
        st.success("Article Submitted Successfully")

with col2:
    grammar_checked = st.button('Grammar Check',key='grammar_check')
    if grammar_checked:
        clear_input = grammar_check(input)
        st.write(clear_input.choices[0].text)

    target_language = st.selectbox(
        'What Language would you like to translate to ?',options = natural_languages)
    if target_language:
        translation_requested = st.button('Translate',key='translate')
        if translation_requested:
            translated_text = translate(input, target_language)
            st.write(translated_text.choices[0].text)

    summary_requested = st.button('Provide Summary',key='provide_summary')
    if summary_requested:
        summary = generate_summary(input)
        st.write(summary.choices[0].text)
