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
        st.session_state.page = 'Course: Python Basics'
    if st.button("Data Science 101"):
        st.session_state.page = 'Course: Data Science 101'

def course_page(course_name, content, quiz):
    st.title(course_name)
    st.write(content)
    
    st.subheader("Quiz")
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
    elif st.session_state.page == 'Course: Python Basics':
        course_page("Python Basics", 
                    "Learn the fundamentals of Python programming!", 
                    {"What is Python?": {"choices": ["A Snake", "A Programming Language", "A Fruit"], "correct": "A Programming Language"},
                     "Which keyword is used to define a function?": {"choices": ["def", "func", "define"], "correct": "def"}})
    elif st.session_state.page == 'Course: Data Science 101':
        course_page("Data Science 101", 
                    "Introduction to data science and machine learning.", 
                    {"What is Data Science?": {"choices": ["A way to store data", "A field of study", "A coding language"], "correct": "A field of study"},
                     "Which library is used for data visualization?": {"choices": ["pandas", "matplotlib", "numpy"], "correct": "matplotlib"}})

if __name__ == "__main__":
    main()
