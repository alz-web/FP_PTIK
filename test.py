import streamlit as st

# Set page title and layout
st.set_page_config(page_title="SQL Course", layout="wide")

# Custom CSS for full styling
st.markdown(
    """
    <style>
        [data-testid="stAppViewContainer"] {
            background-color: rgb(248, 249, 255);
            font-family: Arial, sans-serif;
        }
        [data-testid="stSidebar"] {
            background-color: rgb(84, 78, 51);
            border-radius: 2px;
            color: white;
        }
        [data-testid="stSidebar"] h1 {
            font-size: 35px;
            font-weight: bold;
            color: white;
            text-align: center;
        }
        [data-testid="stSidebar"] button {
            background-color: rgb(106, 99, 109);
            color: white;
            border: none;
            border-radius: 5px;
            width: 160px;
            margin-bottom: 5px;
            transition: all 0.3s ease;
        }
        [data-testid="stSidebar"] button:hover {
            background-color: rgb(255, 255, 255);
            color: rgb(0, 0, 0);
        }
        .main-title {
            font-size: 50px;
            font-weight: bold;
            color: rgb(255, 255, 255);
            text-align: center;
            padding: 20px;
            margin-bottom: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(222, 83, 83, 0.1);
            background-color: rgb(155, 148, 155);
        }
        .video-container, .quiz-container {
            text-align: center;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .quiz-container button {
            background-color: rgb(100, 149, 237);
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .quiz-container button:hover {
            background-color: rgb(34, 61, 108);
        }
        [data-testid="stExpander"] {
            background-color: rgba(39, 36, 36, 0.54);
            border-radius: 5px;
            padding: 10px;
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
            color: rgb(253, 253, 253);

        }
        [data-testid="stExpander"] button:hover {
            background-color: rgb(255, 255, 255);
            color: rgb(122, 65, 65);
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
st.sidebar.markdown("<h1>SQL Course</h1>", unsafe_allow_html=True)
st.sidebar.markdown("Select a chapter:")

chapters = {
    "Chapter 1: Introduction": {
        "Roadmap to Learning SQL": "https://youtu.be/a-hFbr-4VQQ?feature=shared",
        "What is Database": "https://youtu.be/j09EQ-xlh88?feature=shared",
        "SQL Installation": "https://youtu.be/1aybOgni7lI?feature=shared",
        "Quiz": None
    },
    "Chapter 2: Basic Concepts": {
        "Introduction to Query": "https://youtu.be/Hl4NZB1XR9c?feature=shared",
        "Basic Join": "https://youtu.be/0OQJDd3QqQM?feature=shared",
        "SubQuery": "https://youtu.be/nJIEIzF7tDw?feature=shared",
        "Quiz": None
    },
    "Final Test": {
        "Final Test": None
    }
}

if "selected_chapter" not in st.session_state:
    st.session_state["selected_chapter"] = list(chapters.keys())[0]
if "selected_subchapter" not in st.session_state:
    st.session_state["selected_subchapter"] = list(chapters[st.session_state["selected_chapter"]].keys())[0]

def set_subchapter(chapter, subchapter):
    st.session_state["selected_chapter"] = chapter
    st.session_state["selected_subchapter"] = subchapter

# Display chapters in sidebar with toggles
for chapter, subchapters in chapters.items():
    with st.sidebar.expander(chapter, expanded=(chapter == st.session_state["selected_chapter"])):
        for subchapter in subchapters:
            if st.button(f"▫ {subchapter}", key=f"{chapter}_{subchapter}", use_container_width=True):
                set_subchapter(chapter, subchapter)

selected_chapter = st.session_state["selected_chapter"]
selected_subchapter = st.session_state["selected_subchapter"]

st.markdown(f"<div class='main-title'>{selected_chapter} - {selected_subchapter}</div>", unsafe_allow_html=True)

if chapters[selected_chapter][selected_subchapter]:
    st.markdown("<div class='video-container'>", unsafe_allow_html=True)
    st.video(chapters[selected_chapter][selected_subchapter])
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("### Watch the video and proceed to the quiz below.")
    st.text_area("Write your note and  Python code here:", 
                    "print('Hello, Streamlit!')", height=200)


if selected_subchapter == "Quiz":
    st.markdown("<div class='quiz-container'>", unsafe_allow_html=True)
    st.title(f"{selected_chapter} Quiz")
    st.write("Test your knowledge with these multiple-choice questions.")
    
    questions = [
        ("What does SQL stand for?", ["Structured Question Language", "Structured Query Language", "Simple Query Language"], "Structured Query Language"),
        ("Which SQL command is used to retrieve data?", ["SELECT", "INSERT", "DELETE"], "SELECT"),
        ("Which clause is used to filter results in SQL?", ["WHERE", "ORDER BY", "HAVING"], "WHERE")
    ]
    
    score = 0
    for question, options, correct in questions:
        answer = st.radio(question, options)
        if answer == correct:
            score += 1
    
    if st.button("Submit Answers"):
        st.success(f"You scored {score} out of {len(questions)}!")
    st.markdown("</div>", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.info("This course provides structured SQL learning with video lectures and quizzes.")
