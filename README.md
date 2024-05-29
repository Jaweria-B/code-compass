# Code Compass 

## About Code Compass

Welcome to Code Compass, your ultimate companion for navigating the world of programming. Whether you're a beginner or an advanced developer, our tailored roadmap and resources will guide you through learning new languages, mastering concepts, and achieving your coding goals.

## Features

- **RoadMap Generator 🗺️**: Create personalized learning paths for your programming journey.
- **Topic Explainer 📚**: Get detailed explanations of specific programming topics and concepts.
- **Assignment Generator 📝**: Generate custom assignments to practice and reinforce your learning.
- **Quiz Time 🧠**: Test your knowledge with quizzes.
- **Learning Resources 📚**: Access a curated list of resources for further learning.
- **Code Checker ✔️**: Validate and improve your code with our code checking tool.
- **About 📖**: Learn more about Code Compass and our mission.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Streamlit
- OpenAI API Key (for Azure)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Jaweria-B/code-compass.git
   ```
2. Navigate to the project directory:
   ```sh
   cd code-compass
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   ```sh
   cp .env.example .env
   ```
   Edit the `.env` file to include your OpenAI API Key and Azure Endpoint.

### Running the Application

1. Run the Streamlit application:
   ```sh
   streamlit run app.py
   ```
2. Open your web browser and go to `http://localhost:8501` to access Code Compass.

## Screenshots

![Home Page](https://source.unsplash.com/featured/?

coding)
![RoadMap Generator](https://source.unsplash.com/featured/?roadmap)
![Topic Explainer](https://source.unsplash.com/featured/?explain)
![Assignment Generator](https://source.unsplash.com/featured/?assignment)
![Quiz Time](https://source.unsplash.com/featured/?quiz)
![Learning Resources](https://source.unsplash.com/featured/?resources)
![Code Checker](https://source.unsplash.com/featured/?code-checker)
![About Page](https://source.unsplash.com/featured/?about)

## Contributing

We welcome contributions! Please read our [Contributing Guide](CONTRIBUTING.md) for details on how to get started.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, feel free to reach out to us at support@codecompass.com.
```

### 4. **Enhance UI and Set Title & Icon**

Ensure the `st.set_page_config` call in your `app.py` is correctly setting the title and icon:
```python
st.set_page_config(page_title="Code Compass", page_icon=":compass:")
```

### Final Notes:

- **Dependencies:** Make sure your `requirements.txt` includes all necessary libraries.
- **Images in `README.md`:** Update the URLs to actual images or replace them with your own hosted images.
- **Styling:** You can add more CSS to improve the appearance of your app further.
- **Testing:** Thoroughly test each page to ensure it works as expected.