
from openai import OpenAI
import time


def check_code(problem_statement, code):
    pass

import streamlit as st


def show():
    st.markdown("<h1 style='color: white;'>Code Checker ✔️</h1>", unsafe_allow_html=True)
    
    # Add background image
    st.markdown("""
        <style>
        [data-testid="stAppViewContainer"]{
        background-image: url("https://wallpapercave.com/wp/wp6763962.png");
        background-size: cover;
        }
        </style>
    """, unsafe_allow_html=True)

    # Add transparent white overlay and text box
    st.markdown("""
        <style>
        .text-box {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 5px;
            border-radius: 20px;
            box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.4);
            margin: 5px auto;
            width: 120%;
            height: 1000px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Get user input
    problem_statement = st.text_area("Enter Problem Statement:")
    code = st.text_area("Enter Code:")

    # Run code explanation
    if st.button("Run and Debug"):
        explanation= check_code(problem_statement, code)

        # Display response
        html_content = f'<div class="text-box"><h4 style="color:black;">{explanation}</h4></div>'
        st.markdown(html_content, unsafe_allow_html=True)
