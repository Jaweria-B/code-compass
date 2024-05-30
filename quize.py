import streamlit as st
from openai import AzureOpenAI

# Set your Azure OpenAI credentials
azure_endpoint = " " 
AZURE_OPENAI_API_KEY = ''  # Replace with your actual API key

client = AzureOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=AZURE_OPENAI_API_KEY,
    api_version="2024-02-15-preview"
)

st.title("Azure OpenAI Chatbot")

user_input = st.text_input("Enter your question:")
if user_input:
    message_text = [
        {"role": "system", "content": "You are an AI assistant that helps people find information."},
        {"role": "user", "content": user_input},
    ]

    completion = client.chat.completions.create(
        model="kl",  # model = "deployment_name"
        messages=message_text,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
    )

    st.write("Response:")
    st.write(completion.choices[0].message.content)
