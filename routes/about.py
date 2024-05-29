import streamlit as st

def about_page():
    st.markdown("<h1 style='color: black;'>About Code Compass 📖</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="background-color: rgba(255, 255, 255, 0.9); padding: 20px; border-radius: 15px; box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.4);">
            <h2>Welcome to Code Compass</h2>
            <p>
                Code Compass is your ultimate companion for navigating the world of programming. Whether you're a beginner or an advanced developer, our tailored roadmap and resources will guide you through learning new languages, mastering concepts, and achieving your coding goals.
            </p>
            <h3>Features</h3>
            <ul>
                <li><strong>RoadMap Generator:</strong> Create personalized learning paths for your programming journey.</li>
                <li><strong>Topic Explainer:</strong> Get detailed explanations of specific programming topics and concepts.</li>
                <li><strong>Assignment Generator:</strong> Generate custom assignments to practice and reinforce your learning.</li>
                <li><strong>Quiz Time:</strong> Test your knowledge with quizzes.</li>
                <li><strong>Learning Resources:</strong> Access a curated list of resources for further learning.</li>
                <li><strong>Code Checker:</strong> Validate and improve your code with our code checking tool.</li>
            </ul>
            <h3>Our Mission</h3>
            <p>
                Our mission is to make learning programming accessible and enjoyable for everyone. We believe in the power of personalized education and strive to provide the best tools and resources to help you succeed.
            </p>
        </div>
        """, unsafe_allow_html=True
    )