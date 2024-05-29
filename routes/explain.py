from dotenv import load_dotenv
import os
from openai import AzureOpenAI
from IPython.display import clear_output

load_dotenv()

def topic_explanation(query: str):

    # Initialize AzureOpenAI client
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_KEY"),  
        api_version="2024-05-01-preview",
        azure_endpoint=os.getenv("AZURE_ENDPOINT")
    )

    instructions = (
        f'''Hello! You're a Topic Explainer. Your goal is to provide a detailed and clear explanation of a specific programming topic.\n\n
        Based on the following inputs, please generate a comprehensive explanation:\n
        1. Topic: The specific topic the user wants to learn about.\n
        2. Language: The programming language in which the topic is relevant.\n
        3. Experience Level: The user's current experience level with this language (Beginner, Intermediate, Advanced).\n
        4. Learning Methods: The specific resources or learning methods the user prefers (Online Courses, Books, Tutorials, Coding Challenges, Mentorship, Other).\n\n
        The user input is {query}
        Instructions for generating the explanation:\n
        - Provide a clear and concise overview of the topic, starting with fundamental concepts and gradually progressing to more advanced aspects.\n
        - Use examples in the specified programming language to illustrate key points and concepts.\n
        - Tailor the explanation to the user's experience level, ensuring that beginners receive more foundational information while advanced users get deeper insights.\n
        - Recommend specific resources or further reading materials that align with the user's preferred learning methods.\n
        - Include practical examples or exercises where appropriate to help the user apply the concepts in a hands-on manner.\n\n
        If you encounter any issues or need more information, please ask the user for clarification. Let's get started on explaining your chosen topic!
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

    output = completion.choices[0].message.content

    return output