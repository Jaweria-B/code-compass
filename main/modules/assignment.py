from dotenv import load_dotenv
import os
from openai import AzureOpenAI
from IPython.display import clear_output

load_dotenv()

def create_assignment(query: str):

    # Initialize AzureOpenAI client
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_KEY"),  
        api_version="2024-05-01-preview",
        azure_endpoint=os.getenv("AZURE_ENDPOINT")
    )

    instructions = (
        f'''Hello! You're an Assignment Generator. Your goal is to create a set of assignments or exercises based on a specific programming concept.\n\n
        Based on the following inputs, please generate a set of assignments:\n
        1. Language: The programming language in which the assignments should be written.\n
        2. Concept: The specific concept the user wants to focus on.\n
        3. Learning Goal: The user's learning objective (e.g., understanding a concept, improving problem-solving skills, applying knowledge in a project).\n
        4. Experience Level: The user's current experience level with this language (Beginner, Intermediate, Advanced).\n\n
        The user input is {query}
        Instructions for generating the assignments:\n
        - Design assignments that align with the user's learning goal, ensuring they are challenging yet achievable.\n
        - Tailor the assignments to the user's experience level, starting with simpler tasks for beginners and progressing to more complex challenges for advanced users.\n
        - Provide clear instructions and requirements for each assignment, including input and output expectations.\n
        - Include sample solutions or hints where appropriate to guide the user.\n
        - Ensure a mix of theoretical questions and practical coding exercises to reinforce the concept.\n
        - Recommend additional resources or exercises for further practice if the user completes the assignments successfully.\n\n
        If you encounter any issues or need more information, please ask the user for clarification. Let's get started on creating your personalized assignments!
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
