# routes/home.py

import streamlit as st

def home_page():
    st.title("Welcome to Your Educational Platform")

    # Embed HTML animation
    html_animation = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Background Animation</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color: lightblue;
            }

            .animation-container {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: -1;
            }

            .animated-bg {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-image: linear-gradient(to bottom, rgba(255, 255, 255, 0), rgba(255, 255, 255, 1));
                animation: animateBackground 10s linear infinite;
            }

            @keyframes animateBackground {
                0% { transform: translateY(-50%); }
                50% { transform: translateY(50%); }
                100% { transform: translateY(-50%); }
            }
        </style>
    </head>
    <body>
        <div class="animation-container">
            <div class="animated-bg"></div>
        </div>
    </body>
    </html>
    """

    # Embed HTML animation in Streamlit
    st.components.v1.html(html_animation)
    
    st.write("Explore personalized learning paths, quizzes, real-world projects, and more!")
