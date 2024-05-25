from openai import OpenAI
import time



def create_assignment(query):
    pass

def show(response):
    
    import streamlit as st
    st.markdown("<h1 style='color: white;'>Assignment</h1>", unsafe_allow_html=True)
    # Add background image
    #https://wallpapercave.com/wp/wp6763962.png
    page_element="""
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://wallpaperboat.com/wp-content/uploads/2019/10/coding-16.jpg");
    background-size: cover;
    }
    </style>
    """

    st.markdown(page_element, unsafe_allow_html=True)

    # Add transparent white overlay and text box
    st.markdown(
        """
    <style>
    .text-box {
        background-color: rgba(255, 255, 255, 0.9); /* Adjust opacity here */
        padding: 5px;
        border-radius: 20px;
        box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.4);
        margin: 5px auto;
        width: 120%; /* Adjust width as needed */
        height: 1500px; /* Adjust height as needed */
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    # Add text box
    html_content = f'<div class="text-box"><h4 style="color:black;">{response}</h4></div>'

    # Adding the HTML content to Streamlit using st.markdown
    st.markdown(html_content, unsafe_allow_html=True)

