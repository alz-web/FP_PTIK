import streamlit as st

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'Home'
if 'progress' not in st.session_state:
    st.session_state.progress = {}

def home():
    st.title("Welcome to EduStream!")
    st.write("An interactive learning platform built with Streamlit.")
    
    st.subheader("Available Courses")
    if st.button("Python Basics"):
        st.session_state.page = 'Python Basics'
    if st.button("Data Science 101"):
        st.session_state.page = 'Data Science 101'

def course_lecture_page(course_name, video_url, pdf_url):
    st.title(f"{course_name} - Lecture")
    st.video(video_url)
    st.subheader("Download Lecture Notes")
    st.markdown(f"[Download PDF]({pdf_url})")
    
    if st.button("Go to Quiz"):
        st.session_state.page = f'Quiz: {course_name}'
    if st.button("Back to Home"):
        st.session_state.page = 'Home'

def quiz_page(course_name, quiz):
    st.title(f"{course_name} - Quiz")
    score = 0
    for question, options in quiz.items():
        answer = st.radio(question, options['choices'])
        if answer == options['correct']:
            score += 1
    
    if st.button("Submit Quiz"):
        st.session_state.progress[course_name] = score
        st.write(f"You scored {score}/{len(quiz)}!")
    
    if st.button("Back to Home"):
        st.session_state.page = 'Home'

def main():
    if st.session_state.page == 'Home':
        home()
    elif st.session_state.page == 'Python Basics':
        course_lecture_page("Python Basics", "https://example.com/python_basics.mp4", "https://example.com/python_basics.pdf")
    elif st.session_state.page == 'Quiz: Python Basics':
        quiz_page("Python Basics", 
                  {"What is Python?": {"choices": ["A Snake", "A Programming Language", "A Fruit"], "correct": "A Programming Language"},
                   "Which keyword is used to define a function?": {"choices": ["def", "func", "define"], "correct": "def"}})
    elif st.session_state.page == 'Data Science 101':
        course_lecture_page("Data Science 101", "https://example.com/data_science_101.mp4", "https://example.com/data_science_101.pdf")
    elif st.session_state.page == 'Quiz: Data Science 101':
        quiz_page("Data Science 101", 
                  {"What is Data Science?": {"choices": ["A way to store data", "A field of study", "A coding language"], "correct": "A field of study"},
                   "Which library is used for data visualization?": {"choices": ["pandas", "matplotlib", "numpy"], "correct": "matplotlib"}})

if __name__ == "__main__":
    main()
