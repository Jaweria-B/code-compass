from dotenv import load_dotenv
import os
import json
from openai import AzureOpenAI
import time
from IPython.display import clear_output

load_dotenv()

def roadmap(query: str):

    # Initialize AzureOpenAI client
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_KEY"),  
        api_version="2024-05-01-preview",
        azure_endpoint=os.getenv("AZURE_ENDPOINT")
    )
    

    
    # Create a new assistant
    assistant = client.beta.assistants.create(
        name="Learning Path Assistant",
        instructions = (
            '''Hello! You're an Learning Path Assistant. Your goal is to create a personalized learning path or roadmap for your programming journey.\n\n
            Based on the following inputs, please generate a detailed and tailored learning path:\n
            1. Language: The programming language the user wants to learn.\n
            2. Experience Level: The user's current experience level with this language (Beginner, Intermediate, Advanced).\n
            3. Prior Experience: Any prior programming experience the user has in other languages.\n
            4. Learning Methods: The specific resources or learning methods the user prefers (Online Courses, Books, Tutorials, Coding Challenges, Mentorship, Other).\n
            5. Time Commitment: The amount of time the user is willing to dedicate to learning this language per week (Less than 5 hours, 5-10 hours, 10-20 hours, More than 20 hours).\n\n
            Instructions for generating the learning path:\n
            - Take into account the user's experience level to recommend appropriate starting points and progression.\n
            - Consider the user's prior programming experience to identify areas that might require less focus or could be skipped.\n
            - Tailor the learning path to the user's preferred learning methods, suggesting specific resources and approaches that match these preferences.\n
            - Propose a realistic study plan based on the user's time commitment, breaking down the learning process into manageable weekly goals.\n
            - Provide a mix of theoretical knowledge and practical exercises to ensure comprehensive learning.\n\n
            If you encounter any issues or need more information, please ask the user for clarification. Let's get started on creating your personalized learning path!
            '''
        )
        ,
        tools=[{"type": "code_interpreter"}],
        model="code-compass-gpt-4" # Replace this with the deployment name for your model
    )

    print(assistant.model_dump_json(indent=2))

    # Create a thread
    thread = client.beta.threads.create()
    print(thread)

    # Add a user question to the thread
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=query
    )

    # Run the thread
    run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
    )

    print("create status: ", run.status)

    # Retrieve the status of the run
    run = client.beta.threads.runs.retrieve(
    thread_id=thread.id,
    run_id=run.id
    )

    status = run.status
    print(status)

    # start_time = time.time()

    # while status not in ["completed", "cancelled", "expired", "failed"]:
    #     time.sleep(5)
    #     run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    #     elapsed_time = time.time() - start_time
    #     print("Elapsed time: {} minutes {} seconds".format(int(elapsed_time // 60), int(elapsed_time % 60)))
    #     status = run.status
    #     print(f'Status: {status}')
    #     clear_output(wait=True)

    messages = client.beta.threads.messages.list(thread_id=thread.id) 

    # print(f'Status: {status}')
    # elapsed_time = time.time() - start_time
    # print("Elapsed time: {} minutes {} seconds".format(int(elapsed_time // 60), int(elapsed_time % 60)))
    print(messages.model_dump_json(indent=2))
    print("the messages are: ", messages)

    return messages.model_dump_json(indent=2)

    
# if __name__ == '__main__':
#     show()