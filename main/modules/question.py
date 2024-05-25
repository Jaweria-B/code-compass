import streamlit as st

def asking_questions():
    answers = {}

    st.title("Programming Roadmap Generator")
    st.write("Let's create a tailored roadmap for you to learn a programming language.")

    answers["language"] = st.text_input("1. Which programming language do you want to learn?")

    answers["experience_level"] = st.selectbox("2. What is your current experience level with this language?",
                                               ("Beginner", "Intermediate", "Advanced"))

    answers["learning_goal"] = st.selectbox("3. What is your primary goal in learning this language?",
                                            ("Web Development", "Data Science", "Mobile App Development", "Game Development", "Other"))

    answers["time_commitment"] = st.selectbox("4. How much time are you willing to dedicate to learning this language per week?",
                                              ("Less than 5 hours", "5-10 hours", "10-20 hours", "More than 20 hours"))

    answers["learning_methods"] = st.multiselect("5. Are there any specific resources or learning methods you prefer?",
                                                 ("Online Courses", "Books", "Tutorials", "Coding Challenges", "Mentorship", "Other"))

    answers["prior_experience"] = st.text_area("6. Do you have any prior programming experience in other languages? If yes, please specify.")
    answers["topic_today"] = st.text_input("7. Which topic do you want to learn today?")

    if st.button("Submit"):
        st.success("Answers submitted successfully!")
    return answers
