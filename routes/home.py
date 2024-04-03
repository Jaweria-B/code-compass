# home_page.py

import streamlit as st

def home_page():
    # Custom HTML/CSS for the animation
    animation_html = """
    <style>
        body {
            background-color: lightblue;
            margin: 0;
            overflow: hidden;
        }

        .animation-container {
            width: 100%;
            height: 100vh;
            position: relative;
            overflow: hidden;
        }

        .animation {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 200px;
            height: 200px;
            background-color: rgba(255, 255, 255, 0.5);
            border-radius: 50%;
            animation: spin 3s linear infinite;
        }

        @keyframes spin {
            0% {
                transform: translate(-50%, -50%) rotate(0deg);
            }
            100% {
                transform: translate(-50%, -50%) rotate(360deg);
            }
        }
    </style>
    <div class="animation-container">
        <div class="animation"></div>
    </div>
    """

    st.title("Welcome to Your Educational Platform")
    st.markdown(animation_html, unsafe_allow_html=True)
    st.write("Explore personalized learning paths, quizzes, real-world projects, and more!")
