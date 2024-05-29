import streamlit as st
import markdown
from routes.question import asking_questions
from routes import LearningPath
from routes.explain import topic_explanation
from routes import assignment
from routes import code_checker
from routes.quiz import quiz_page
from routes.resources import resources_page
from routes.about import about_page 

# Initialize session states if they don't exist
if 'answers' not in st.session_state:
    st.session_state.answers = None
if 'content' not in st.session_state:
    st.session_state.content = None

def show(title, response):
    st.markdown(f"<h1 style='color: white;'>{title}</h1>", unsafe_allow_html=True)
    page_element = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://wallpaperboat.com/wp-content/uploads/2019/10/coding-16.jpg");
        background-size: cover;
    }
    </style>
    """
    st.markdown(page_element, unsafe_allow_html=True)
    st.markdown(
        """
    <style>
    .text-box {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 15px 15px 15px 20px;
        border-radius: 20px;
        box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.4);
        color: black !important;
        margin: 5px auto;
        width: 120%;
        height: auto;
    }
    .text-box h1, h2, h3, h4, h5, h6 {
        color: black !important;
    }
    </style>
    """, unsafe_allow_html=True
    )

    html_markdown = markdown.markdown(response)
    html_content = f'<div class="text-box"><h4>{html_markdown}</h4></div>'
    st.markdown(html_content, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Code Compass", page_icon=":compass:")

    st.sidebar.title("Code Compass Options")

    page_options = {
        "Home 🏠": "Home",
        "RoadMap Generator 🗺️": "RoadMap",
        "Topic Explainer 📚": "Topic",
        "Assignment Generator 📝": "Assignment",
        "Quiz Time 🧠": "Quiz",
        "Learning Resources 📚": "Resources",
        "Code Checker ✔️": "Code Checker",
        "About Us 📖": "About"
    }

    page = st.sidebar.radio("Go to", list(page_options.keys()))

    if page == "Home 🏠":
        st.title("Welcome to Code Compass :compass:")
        st.session_state.answers = None
        st.session_state.content = None

    if st.session_state.answers is None:
        st.session_state.answers = asking_questions()
    
    Topic_query = f'Topic: {st.session_state.answers["topic_today"]}, Language: {st.session_state.answers["language"]}, Experience Level: {st.session_state.answers["experience_level"]}, Learning method: {st.session_state.answers["learning_methods"]}'
    assignment_query = f'Language: {st.session_state.answers["language"]}, Concept: {st.session_state.answers["topic_today"]}, Learning Goal: {st.session_state.answers["learning_goal"]}, Experience Level: {st.session_state.answers["experience_level"]}'
    roadmap_query = f'Language: {st.session_state.answers["language"]}, Experience Level: {st.session_state.answers["experience_level"]}, prior Experience: {st.session_state.answers["prior_experience"]}, Learning method: {st.session_state.answers["learning_methods"]}, time commitment: {st.session_state.answers["time_commitment"]}'

    if st.session_state.answers is None:
        st.write("Please fill in the inputs to proceed.")
        return

    if page == "RoadMap Generator 🗺️":
        if st.session_state.content is None or "RoadMap" not in st.session_state.content:
            response = LearningPath.roadmap(roadmap_query)
            show("RoadMap Generator 🗺️", response)
            st.session_state.content = {"RoadMap": response}
        else:
            show("RoadMap Generator 🗺️", st.session_state.content["RoadMap"])

    elif page == "Topic Explainer 📚":
        if st.session_state.content is None or "Explain" not in st.session_state.content:
            response = topic_explanation(Topic_query)
            show("Topic Explainer 📚", response)
            st.session_state.content = {"Explain": response}
        else:
            show("Topic Explainer 📚", st.session_state.content["Explain"])

    elif page == "Assignment Generator 📝":
        if st.session_state.content is None or "assignment" not in st.session_state.content:
            response = assignment.create_assignment(assignment_query)
            show("Assignment Generator 📝", response)
            st.session_state.content = {"assignment": response}
        else:
            show("Assignment Generator 📝", st.session_state.content["assignment"])

    elif page == "Code Checker ✔️":
        code_checker.show()
    
    elif page == "Quiz Time 🧠":
        quiz_page()

    elif page == "Learning Resources 📚":
        resources_page()
    
    elif page == "About Us 📖":
        about_page()

if __name__ == "__main__":
    main()
