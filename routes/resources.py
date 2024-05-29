import streamlit as st
from dotenv import load_dotenv
import os
from openai import AzureOpenAI
import json

# Load environment variables
load_dotenv()

def get_learning_resources(topic, experience_level, learning_method):
    api_key = os.getenv("AZURE_OPENAI_KEY")
    endpoint = os.getenv("AZURE_ENDPOINT")
    
    prompt = (
        f"Hello! You're a resource finder assistant. Your goal is to find learning resources based on the user's topic.\n\n"
        f"Based on the following inputs, please provide a list of resources:\n"
        f"1. Topic: {topic}\n"
        f"2. Experience Level: {experience_level}\n"
        f"3. Learning Method: {learning_method}\n\n"
        f"Instructions:\n"
        f"- Search the internet for relevant YouTube videos, Coursera courses, and websites.\n"
        f"- Provide a list of links with brief descriptions for each resource.\n"
        f"- Ensure the resources are up-to-date and highly rated.\n"
        f"- Format the response in a JSON structure with keys: 'youtube', 'coursera', 'websites'.\n\n"
        f"I know that you are an AI developed by OpenAI, you can't perform live searches on the internet or access real-time data, including checking for the latest resources, their ratings, or up-to-date links. Just provide me the json response.\n\n"
        ''' Use this format:
        {
            "youtube": [
                {
                    "title": "the title",
                    "description": "the description",     
                    "link": "the_link"
                },
                ...
            ],
            "coursera": [
                {
                    "title": "the title",
                    "description": "the description",     
                    "link": "the_link"
                },
                ...
            ],
            "websites": [
                {
                    "title": "the title",
                    "description": "the description",     
                    "link": "the_link"
                },
                ...
            ]
        }'''
    )

    try:
        # Initialize AzureOpenAI client
        client = AzureOpenAI(
            api_key=api_key,  
            api_version="2024-05-01-preview",
            azure_endpoint=endpoint
        )
        
        message_text = [{"role": "system", "content": prompt}]

        # Create a completion request to generate text using the GPT-4 Turbo model
        completion = client.chat.completions.create(
            model="code-compass-gpt-4",  # model = "deployment_name"
            messages=message_text,
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )

        response = completion.choices[0].message.content.strip()
        return response

    except Exception as e:
        st.error(f"An error occurred while fetching learning resources: {str(e)}")
        return None

def fetch_learning_resources(topic, experience_level, learning_method):
    response = get_learning_resources(topic, experience_level, learning_method)
    if response:
        st.write("Raw response from API:")
        st.write(response)  # Display the raw response for debugging purposes
        try:
            response_json = json.loads(response)
            return response_json
        except json.JSONDecodeError as e:
            st.error("Failed to parse the response as JSON.")
            st.write("Response received:")
            st.write(response)
            return None
    else:
        st.error("No response received from the API.")
        return None


def resources_page():
    st.title("Learning Resource Finder 📚")

    topic = st.session_state.answers["topic_today"]
    experience_level = st.session_state.answers["experience_level"]
    learning_method = st.session_state.answers["learning_methods"]

    if st.button("Find Resources"):
        with st.spinner("Fetching learning resources..."):
            resources = fetch_learning_resources(topic, experience_level, learning_method)

            if resources:
                st.header("YouTube Videos")
                for video in resources.get("youtube", []):
                    st.write(f"[{video['title']}]({video['link']})")
                    st.write(video['description'])

                st.header("Coursera Courses")
                for course in resources.get("coursera", []):
                    st.write(f"[{course['title']}]({course['link']})")
                    st.write(course['description'])

                st.header("Web Resources")
                for website in resources.get("websites", []):
                    st.write(f"[{website['title']}]({website['link']})")
                    st.write(website['description'])
            else:
                st.write("No resources found.")