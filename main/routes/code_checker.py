import streamlit as st
from dotenv import load_dotenv
import os
from openai import AzureOpenAI
from IPython.display import clear_output

load_dotenv()


def check_code(problem_statement, code, experience_level, learning_goal):

    # Initialize AzureOpenAI client
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_KEY"),  
        api_version="2024-05-01-preview",
        azure_endpoint=os.getenv("AZURE_ENDPOINT")
    )
    
    instructions = (
        f'''Hello! You're a Code Checker and Programming Assistant. Your goal is to provide detailed and comprehensive feedback on the code provided by the user.\n\n
        Based on the following inputs, please assist the user with their code:\n
        1. Code: {code} The piece of code the user wants to check.\n
        2. Problem Statement: {problem_statement} The problem statement user has enetered.\n
        3. Experience Level: {experience_level}The user's current experience level with this language (Beginner, Intermediate, Advanced).\n
        4. Learning Goal: {learning_goal} The user's learning objective (e.g., understanding a concept, improving problem-solving skills, debugging an error, optimizing code).\n\n
        The user inputs have been given to you.
        Instructions for providing assistance:\n
        - Start by analyzing the provided code for any syntax or runtime errors. Point out the specific errors and explain why they occur, including which lines are affected.\n
        - If there are logical errors, help the user understand the problem and suggest possible fixes. Explain the underlying concepts that might be causing the issue.\n
        - Offer suggestions for improving the code, including best practices, optimizations, and alternative approaches that might be more efficient or readable.\n
        - Provide relevant examples or snippets to illustrate your suggestions and explanations.\n
        - If the user's learning goal is to understand a particular concept, offer a detailed explanation of how this concept is applied in their code. Provide additional resources or examples if needed.\n
        - Encourage the user to experiment with their code and guide them on how to test and validate their changes.\n
        - Tailor your feedback to the user's experience level, ensuring that beginners receive more foundational guidance while advanced users get deeper insights and advanced tips.\n\n
        If you encounter any issues or need more information, please ask the user for clarification. Let's get started on helping you with your code!
        '''
    )


    message_text = [{"role":"system","content":instructions}]


    # Create a completion request to generate text using the GPT-4 Turbo model
    completion = client.chat.completions.create(
        model="code-compass-gpt-4", # model = "deployment_name"
        messages = message_text,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    learning_path = completion.choices[0].message.content

    return learning_path




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
            padding: 5px 15px;
            border-radius: 20px;
            box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.4);
            color: black !important;
            margin: 5px auto;
            width: 120%;
            height: auto;
        }
        .text-box h1, h2, h3, h4, h5, h6 {
            color: black !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Get user input
    problem_statement = st.text_area("Enter Problem Statement:")
    code = st.text_area("Enter Code:", height=300)
    experience_level = st.selectbox("Experience Level:", ["Beginner", "Intermediate", "Advanced"])
    learning_goal = st.multiselect("Learning Goal:", ("Understanding a concept", "Improving problem-solving skills", "Debugging an error", "Optimizing code"))

    # Run code explanation
    if st.button("Run and Debug"):
        explanation= check_code(problem_statement, code, experience_level, learning_goal)

        # Display response
        html_content = f'<div class="text-box"><h4 style="color:black;">{explanation}</h4></div>'
        st.markdown(html_content, unsafe_allow_html=True)
