import streamlit as st
from dotenv import load_dotenv
import os
from openai import AzureOpenAI
import random

# Load environment variables
load_dotenv()

def get_quiz_data(text):
    template = f"""
    You are a helpful assistant programmed to generate questions based on any text provided. For every chunk of text you receive, you're tasked with designing 5 distinct questions. Each of these questions will be accompanied by 3 possible answers: one correct answer and two incorrect ones. 
    For clarity and ease of processing, structure your response in a way that emulates a Python list of lists. 
    Your output should be shaped as follows:
    1. An outer list that contains 5 inner lists.
    2. Each inner list represents a set of question and answers, and contains exactly 4 strings in this order:
    - The generated question.
    - The correct answer.
    - The first incorrect answer.
    - The second incorrect answer.
    Your output should mirror this structure:
    [
        ["Generated Question 1", "Correct Answer 1", "Incorrect Answer 1.1", "Incorrect Answer 1.2"],
        ["Generated Question 2", "Correct Answer 2", "Incorrect Answer 2.1", "Incorrect Answer 2.2"],
        ...
    ]
    It is crucial that you adhere to this format as it's optimized for further Python processing.
    Provided text: {text}
    """

    try:
        # Initialize AzureOpenAI client
        client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_KEY"),  
            api_version="2024-05-01-preview",
            azure_endpoint=os.getenv("AZURE_ENDPOINT")
        )

        message_text = [{"role":"system","content":template}]

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

        quiz_data = eval(completion.choices[0].message.content)

        # Shuffle options once and store them in session state
        for question_set in quiz_data:
            options = question_set[1:]
            random.shuffle(options)
            question_set[1:] = options

        return quiz_data

    except Exception as e:
        if "AuthenticationError" in str(e):
            st.error("Incorrect API key provided. Please check and update your API key.")
            st.stop()
        else:
            st.error(f"An error occurred: {str(e)}")
            st.stop()

def display_quiz(quiz_data):
    st.title("Quiz Time!")
    st.write("Please select the correct answers:")

    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = [None] * len(quiz_data)

    for idx, question_set in enumerate(quiz_data):
        question = question_set[0]
        options = question_set[1:]

        st.write(f"**{idx + 1}. {question}**")
        user_answer = st.radio(
            label="",
            options=options,
            key=f"question_{idx}",
            index=options.index(st.session_state.user_answers[idx]) if st.session_state.user_answers[idx] else 0
        )
        st.session_state.user_answers[idx] = user_answer

    if st.button("Submit"):
        calculate_score(quiz_data, st.session_state.user_answers)

def calculate_score(quiz_data, user_answers):
    score = 0
    for idx, question_set in enumerate(quiz_data):
        correct_answer = question_set[1]
        if user_answers[idx] == correct_answer:
            score += 1

    st.success(f"Your score is: {score} out of {len(quiz_data)}")

def quiz_page():
    st.title("Quiz Generator 🧠")

    text = st.text_area("Enter the text to generate quiz questions:", height=200)
    if st.button("Generate Quiz"):
        if text:
            with st.spinner("Generating quiz questions..."):
                quiz_data = get_quiz_data(text)
                if quiz_data:
                    st.session_state.quiz_data = quiz_data
                    display_quiz(quiz_data)
                else:
                    st.error("Failed to generate quiz questions.")
        else:
            st.error("Please provide the text.")

    if 'quiz_data' in st.session_state:
        display_quiz(st.session_state.quiz_data)