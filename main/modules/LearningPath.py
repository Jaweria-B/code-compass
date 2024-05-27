from dotenv import load_dotenv
import os
from openai import AzureOpenAI
from IPython.display import clear_output

load_dotenv()

def roadmap(query: str):

    # Initialize AzureOpenAI client
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_KEY"),  
        api_version="2024-05-01-preview",
        azure_endpoint=os.getenv("AZURE_ENDPOINT")
    )
    
    instructions = (
        f'''Hello! You're an Learning Path Assistant. Your goal is to create a personalized learning path or roadmap for your programming journey.\n\n
        Based on the following inputs, please generate a detailed and tailored learning path:\n
        1. Language: The programming language the user wants to learn.\n
        2. Experience Level: The user's current experience level with this language (Beginner, Intermediate, Advanced).\n
        3. Prior Experience: Any prior programming experience the user has in other languages.\n
        4. Learning Methods: The specific resources or learning methods the user prefers (Online Courses, Books, Tutorials, Coding Challenges, Mentorship, Other).\n
        5. Time Commitment: The amount of time the user is willing to dedicate to learning this language per week (Less than 5 hours, 5-10 hours, 10-20 hours, More than 20 hours).\n\n
        The user input is {query}
        Instructions for generating the learning path:\n
        - Take into account the user's experience level to recommend appropriate starting points and progression.\n
        - Consider the user's prior programming experience to identify areas that might require less focus or could be skipped.\n
        - Tailor the learning path to the user's preferred learning methods, suggesting specific resources and approaches that match these preferences.\n
        - Propose a realistic study plan based on the user's time commitment, breaking down the learning process into manageable weekly goals.\n
        - Provide a mix of theoretical knowledge and practical exercises to ensure comprehensive learning.\n\n
        If you encounter any issues or need more information, please ask the user for clarification. Let's get started on creating your personalized learning path!
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