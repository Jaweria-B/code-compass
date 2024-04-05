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
