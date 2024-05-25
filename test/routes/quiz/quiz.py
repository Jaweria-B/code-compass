import streamlit as st
from openai import AzureOpenAI
import os

def generate_quiz(prompt):
    client = AzureOpenAI(
        azure_endpoint=os.getenv("AZURE_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_KEY"),
        api_version="2024-02-15-preview"
    )
    
    message_text = [{"role": "system", "content": prompt}]
    
    completion = client.chat.completions.create(
        model="code-compass-gpt-4",
        messages=message_text,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    
    return completion.choices[0].message.content

def quiz():
    st.title("Quiz Generator")

    st.write("Generate a customized quiz based on a specific technology or provided text.")

    quiz_type = st.radio(
        "Select the type of quiz content:",
        ("Technology", "Custom Text")
    )

    if quiz_type == "Technology":
        topic = st.text_input("Enter the technology you want a quiz for:", "")
    else:
        topic = st.text_area("Enter the text you want a quiz for:", "")

    difficulty = st.selectbox("Select difficulty level:", ["Easy", "Medium", "Hard"])

    quiz_format = st.selectbox("Select quiz format:", ["Short Questions", "MCQs", "Fill In the Blanks"])

    if st.button("Generate Quiz"):
        if topic:
            prompt = f"""
            You are an AI assistant that helps people generate quizzes.
            The user wants to generate a quiz for the topic: {topic}.
            The difficulty level is: {difficulty}.
            The format of the quiz is: {quiz_format}.
            Please generate a comprehensive quiz based on the given topic, difficulty level, and format.

            For MCQs, provide options for each question.
            For Fill In the Blanks, provide sentences with blanks.
            For Short Questions, provide open-ended questions.
            """

            quiz = generate_quiz(prompt)

            st.subheader("Generated Quiz")
            st.write(quiz)

            # Here, further parsing and displaying of quiz in specific format can be done.

