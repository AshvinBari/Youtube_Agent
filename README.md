# 🎥 AI Agent For YouTube

## 📖 Overview
**AI Agent For YouTube** is a smart tool designed to help you find the best YouTube tutorials for any topic. Whether you are a beginner, intermediate, or advanced learner, this agent uses the **Tavily API** to search for high-quality video content and recommends the most popular and relevant tutorials based on your needs.

## ✨ Features
- **Smart Search**: Finds YouTube videos based on your specific topic (e.g., "Python Basics", "Machine Learning").
- **Difficulty Levels**: Tailors results to your skill level:
  - 🟢 **Basic**: Beginner-friendly, step-by-step tutorials.
  - 🟡 **Intermediate**: Practical project-based tutorials.
  - 🔴 **Advanced**: Expert-level deep dives.
- **Best Pick Recommendation**: Automatically highlights the "Highest-View" or most relevant video.
- **Visual Interface**: Displays video thumbnails, titles, and direct links.
- **Additional Recommendations**: Provides a list of other top-rated videos for more options.

## 🛠️ Tech Stack
- **Python**: Core programming language.
- **Streamlit**: For the interactive web user interface.
- **Tavily API**: For powerful search and content extraction.

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher installed.
- A Tavily API Key (currently configured in the code).

### Installation

1. **Clone the Repository** (if applicable) or download the source code.
   ```bash
   git clone <repository-url>
   cd YouTube
   ```

2. **Install Dependencies**
   Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. The application will open in your default web browser (usually at `http://localhost:8501`).

## 💡 How to Use
1. **Enter a Topic**: Type the subject you want to learn about (e.g., "React JS", "Data Science").
2. **Select Level**: Choose your difficulty level (Basic, Intermediate, or Advanced).
3. **Find Best Video**: Click the button to let the AI agent search.
4. **View Results**:
   - The **top recommendation** will appear with a large thumbnail and description.
   - Scroll down to see **other recommended videos**.
   - Click **"Watch Video"** to open the video on YouTube.

## 📂 Project Structure
```
YouTube/
├── app.py              # Main application logic and UI
├── requirements.txt    # List of Python dependencies
└── README.md           # Project documentation
```

## ⚠️ Note on API Key
The `app.py` file currently contains a placeholder or hardcoded API key for Tavily. For production or personal use, it is recommended to use environment variables to secure your credentials.

---
*Built with ❤️ using Streamlit and Tavily AI.*
