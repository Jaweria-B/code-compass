import os
import streamlit as st
from openai import AzureOpenAI

# Initialize Azure OpenAI client with API key
client = AzureOpenAI(
    azure_endpoint="https://demo-openai-1.openai.azure.com/",
    api_key="7391afe05b9d4207819f652624a59447",  # Provide your API key directly here
    api_version="2024-02-15-preview"
)

# Function to generate quiz questions based on a prompt
def generate_quiz_questions(prompt, question_type):
    message_text = [{"role": "system", "content": prompt}]

    completion = client.chat.completions.create(
        model="ds",  # Specify your model name or deployment name
        messages=message_text,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    # Extract questions from the completion
    quiz_questions = []
    for choice in completion.choices:
        for message in choice.logprobs.text:
            if message.role == "assistant":
                quiz_questions.append(message.content.strip())

    return quiz_questions

# Main function
def main():
    st.title("Quiz Generator")

    prompt = st.text_area("Enter prompt:", "Generate multiple-choice questions about geography.")

    question_types = ["multiple_choice", "fill_in_the_blank"]
    selected_question_type = st.selectbox("Select the type of questions:", question_types)

    if st.button("Generate Questions"):
        questions = generate_quiz_questions(prompt, selected_question_type)
        st.subheader("Quiz Questions:")
        for i, question in enumerate(questions):
            st.write(f"{i + 1}. {question}")

if __name__ == "__main__":
    main()


// open ai ---
import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

def generate_mcq(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.5,
        n=1,
        stop="\n"
    )

    # Extract the generated MCQ from the response
    mcq = response.choices[0].text.strip()

    # Split the MCQ into question and choices
    question, choices = mcq.split("\n")[0], mcq.split("\n")[1:]

    return question, choices

def main():
    st.title("MCQ (Multiple Choice Questions) Generator")

    # Input prompt from the user
    prompt = st.text_area("Enter your prompt here:", height=150)

    # Generate MCQs button
    if st.button("Generate MCQs"):
        if prompt:
            question, choices = generate_mcq(prompt)
            st.write("Generated MCQ:")
            st.write("Question:", question)
            st.write("Choices:")
            for idx, choice in enumerate(choices):
                st.write(f"{idx+1}. {choice}")
        else:
            st.error("Please enter a prompt.")

if __name__ == "__main__":
    main()
