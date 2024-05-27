import streamlit as st

from pages.question import asking_questions

from pages import LearningPath
from pages.explain import topic_explanation
from pages import assignment
from pages import code_checker

if 'answers' not in st.session_state:
    st.session_state.answers = None
if 'content' not in st.session_state:
    st.session_state.content = None

def show(title,response):
    import streamlit as st
    st.markdown(f"<h1 style='color: white;'>{title}</h1>", unsafe_allow_html=True)
    # Add background image
    #https://wallpapercave.com/wp/wp6763962.png

    page_element="""
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://plus.unsplash.com/premium_vector-1711987875549-d0ba34191e70?bg=FFFFFF&w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjl8fGNvZGluZ3xlbnwwfHwwfHx8MA%3D%3D");
    background-size: cover;
    }
    </style>
    """

    st.markdown(page_element, unsafe_allow_html=True)

    # Add transparent white overlay and text box
    st.markdown(
        """
    <style>
    .text-box {
        background-color: rgba(255, 255, 255, 0.9); /* Adjust opacity here */
        padding: 15px 15px 15px 20px;
        border-radius: 20px;
        box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.4);
        color: black !important;
        margin: 5px auto;
        width: 120%; /* Adjust width as needed */
        height: auto; /* Adjust height as needed */
    }
    .text-box h1, h2, h3, h4, h5, h6 {
        color: black !important; /* Ensure text color is black */
    }
    </style>
    """, unsafe_allow_html=True)

    import markdown
    html_markdown = markdown.markdown(response)
    # Add text box
    html_content = f'<div class="text-box"><h4>{html_markdown}</h4></div>'
   
    # Adding the HTML content to Streamlit using st.markdown
    st.markdown(html_content, unsafe_allow_html=True)


import streamlit as st

page_options = {
    "Home 🏠": "Home",
    "RoadMap Generator 🗺️": "RoadMap",
    "Topic Explainer 📚": "Topic",
    "Assignment Generator 📝": "Assignment",
    "Code Checker ✔️": "Code Checker"
}

def main():
    st.sidebar.title("Code Compass Options")

    page = st.sidebar.radio("Go to", list(page_options.keys()))

    if page == "Home 🏠":
        st.title("Welcome to Code Compass")
        st.session_state.answers = None  
        st.session_state.content = None     

    if st.session_state.answers is None:
        st.session_state.answers = asking_questions()
    

    Topic_query = f'Topic:{st.session_state.answers["topic_today"]} Language: {st.session_state.answers["language"]}, Experience Level: {st.session_state.answers["experience_level"]}, Learning_method: {st.session_state.answers["learning_methods"]}'
    assignment_query = f'Language: {st.session_state.answers["language"]}, Concept: {st.session_state.answers["topic_today"]}, Learning Goal: {st.session_state.answers["learning_goal"]}, Experience Level: {st.session_state.answers["experience_level"]}'
    roadmap_query = f'Language: {st.session_state.answers["language"]}, Experience Level: {st.session_state.answers["experience_level"]}, prior Experience: {st.session_state.answers["prior_experience"]}, Learning_method: {st.session_state.answers["learning_methods"]}, time_commitment: {st.session_state.answers["time_commitment"]}'

    if st.session_state.answers is None:
        st.write("Please fill in the inputs to proceed.")
        return

    if page == "RoadMap Generator 🗺️":
        if st.session_state.content is None or st.session_state.content.get("RoadMap") is None:
            response = LearningPath.roadmap(roadmap_query)
            show("RoadMap Generator 🗺️", response)
            st.session_state.content = {"RoadMap": response}
        else:
            show("RoadMap Generator 🗺️", st.session_state.content["RoadMap"])

    elif page == "Topic Explainer 📚":
        if st.session_state.content is None or st.session_state.content.get("Explain") is None:
            response = topic_explanation(Topic_query)
            show("Topic Explainer 📚", response)
            st.session_state.content = {"Explain": response}
        else:
            show("Topic Explainer 📚", st.session_state.content["Explain"])

    elif page == "Assignment Generator 📝":
        if st.session_state.content is None or st.session_state.content.get("assignment") is None:
            response = assignment.create_assignment(assignment_query)
            show("Assignment Generator 📝", response)
            st.session_state.content = {"assignment": response}
        else:
            show("Assignment Generator 📝", st.session_state.content["assignment"])

    elif page == "Code Checker ✔️":
        code_checker.show()
if __name__ == "__main__":
    main()

