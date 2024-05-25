# streamlit_app.py

import streamlit as st
from modules.question import asking_questions
from modules import LearningPath
# from modules import assignment
# from modules.explain import topic_explanation
from modules import code_checker

def show(title,response):
    import streamlit as st
    st.markdown(f"<h1 style='color: white;'>{title}</h1>", unsafe_allow_html=True)
    # Add background image
    #https://wallpapercave.com/wp/wp6763962.png
    page_element="""
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://wallpaperboat.com/wp-content/uploads/2019/10/coding-16.jpg");
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
        padding: 5px;
        border-radius: 20px;
        box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.4);
        margin: 5px auto;
        width: 120%; /* Adjust width as needed */
        height: 5000px; /* Adjust height as needed */
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
    import markdown
    html_markdown = markdown.markdown(response)
    # Add text box
    html_content = f'<div class="text-box"><h4 style="color:black;">{html_markdown}</h4></div>'

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
    st.title("Welcome to Code Compass")

    content_dict = {
        "RoadMap": None,
        "Explain": None,
        "assignment": None,
    }

    answers = None
    
    answers = asking_questions() 
    Topic_query = f'Topic:{answers["topic_today"]} Language: {answers["language"]}, Experience Level: {answers["experience_level"]}, Learning_method: {answers["learning_methods"]}'
    assignment_query = f'Language: {answers["language"]},Concept: {answers["topic_today"]}, Learning Goal: {answers["learning_goal"]}, Experience Level: {answers["experience_level"]}'
    roadmap_query = f'Language: {answers["language"]},Experience Level: {answers["experience_level"]}, prior Experience: {answers["prior_experience"]}, Learning_method: {answers["learning_methods"]}, time_committment: {answers["time_commitment"]}'


    st.sidebar.title("Code Compass Options")

   
    page = st.sidebar.radio("Go to", list(page_options.keys()))

    if page == "Home 🏠":
        pass    

    elif page == "RoadMap Generator 🗺️":
        if content_dict["RoadMap"] is None:
            response = LearningPath.roadmap(roadmap_query)
            show("RoadMap Generator 🗺️",response)
            content_dict["RoadMap"]=response
            
        else:
            show("RoadMap Generator 🗺️",content_dict["RoadMap"])

    # elif page == "Topic Explainer 📚":
    #     if content_dict["Explain"] is None:
    #         content_dict["Explain"] = topic_explanation(Topic_query) 
    #     show("Topic Explainer 📚",content_dict["Explain"])

    # elif page == "Assignment Generator 📝":
    #     if content_dict["assignment"] is None:
    #         content_dict["assignzment"] = assignment.create_assignment(assignment_query)
    #     show("Assignment Generator 📝",content_dict["assignment"])

    elif page == "Code Checker ✔️":
        code_checker.show()

if __name__ == "__main__":
    main()

