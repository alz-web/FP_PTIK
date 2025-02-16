# Code by KEL 4 PTIK
# ALDO, MOZA, BIHAN, NESYA, SAVANNA
import streamlit as st
import pandas as pd

# JUDUL
st.set_page_config(page_title="SQL Course", layout="wide")

# CSS
st.markdown(
    """
    <style>
        [data-testid="stAppViewContainer"] {
            background-color: #f9f9f9;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        [data-testid="stSidebar"] {
            background-color: #1f2937;
            color: white;
            border-radius: 8px;
        }
        [data-testid="stSidebar"] h1 {
            font-size: 48px;
            font-weight: 700;
            color: #e5e7eb;
            text-align: center;
        }
        [data-testid="stSidebar"] button {
            background-color: #374151 !important;
            color: #e5e7eb !important;
            border: 1px solid #4b5563;
            border-radius: 6px;
            transition: background 0.3s ease, color 0.3s ease;
        }
        [data-testid="stSidebar"] button:hover {
            background-color: #111827 !important;
            color: #f9fafb !important;
        }
        .main-title {
            font-size: 48px;
            font-weight: 700;
            color: #f9fafb;
            text-align: center;
            padding: 24px;
            margin-bottom: 24px;
            background-color: #111827;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
        }
        .video-container, .quiz-container, .content-container {
            text-align: center;
            padding: 24px;
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
            margin-bottom: 24px;
        }
        #team-container {
            display: flex;
            flex-direction: column;
            width: 100%;
            padding: 24px;
            background-color: #f1f5f9;
        }
        .team-member {
            background-color: #e2e8f0;
            border-radius: 12px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.1);
            padding: 24px;
            margin-bottom: 24px;
            width: 100%;
            display: flex;
            align-items: center;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .team-member:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 24px rgba(0,0,0,0.2);
        }
        .team-image img {
            border-radius: 50%;
            width: 120px;
            height: 120px;
            object-fit: cover;
            margin-right: 24px;
            border: 4px solid #94a3b8;
        }
        .team-info h3 {
            font-size: 24px;
            color: #1e293b;
            margin-bottom: 8px;
        }
        .team-info p {
            font-size: 16px;
            color: #475569;
            margin: 6px 0;
        }
        .team-info p strong {
            color: #3b82f6;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Sidebar Navigation
st.sidebar.markdown("<h1>SQL Course</h1>", unsafe_allow_html=True)
st.sidebar.markdown("Select a chapter:")
#CHAPTER AND SUBCHAPTER
chapters = {
    "Chapter 1: Introduction": {
        "Roadmap to Learning SQL": "https://youtu.be/a-hFbr-4VQQ?feature=shared",
        "What is Database": "https://youtu.be/j09EQ-xlh88?feature=shared",
        "SQL Installation": "https://youtu.be/hiS_mWZmmI0?feature=shared",
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
    },
    "Our Team": {
        "Members": None
    }
}
if "selected_chapter" not in st.session_state:
    st.session_state["selected_chapter"] = list(chapters.keys())[0]
if "selected_subchapter" not in st.session_state:
    st.session_state["selected_subchapter"] = list(chapters[st.session_state["selected_chapter"]].keys())[0]
def set_subchapter(chapter, subchapter):
    st.session_state["selected_chapter"] = chapter
    st.session_state["selected_subchapter"] = subchapter

# sIDEBAR toggles
for chapter, subchapters in chapters.items():
    with st.sidebar.expander(chapter, expanded=(chapter == st.session_state["selected_chapter"])):
        for subchapter in subchapters:
            if st.button(f"▫ {subchapter}", key=f"{chapter}_{subchapter}", use_container_width=True):
                set_subchapter(chapter, subchapter)

selected_chapter = st.session_state["selected_chapter"]
selected_subchapter = st.session_state["selected_subchapter"]

st.markdown(f"<div class='main-title'>{selected_chapter} - {selected_subchapter}</div>", unsafe_allow_html=True)

# MATERI TEXT TIAP BAB
explanations = {
    "Roadmap to Learning SQL": {
        "text": "A roadmap to learning SQL starts with mastering basic commands like SELECT, INSERT, UPDATE, and DELETE. Next, focus on more advanced topics like JOINs, GROUP BY, and subqueries. As you progress, learn about database design, normalization, and query optimization. Hands-on practice with real data will strengthen your skills and prepare you for complex tasks.",
        "code": "No code yet for this subchapter",
        "image": "https://cdn.slidesharecdn.com/ss_thumbnails/sqlroadmap-241017100645-0834afe2-thumbnail.jpg?width=640&height=640&fit=bounds",
        "table": {"Step": ["1. Learn Basics", "2. Master Queries", "3. Optimize Performance"],
                  "Details": ["Understand syntax", "Work with Joins and Subqueries", "Use Indexing"]}
    },
    "What is Database": {
        "text": "A database is an organized collection of data that is stored and managed electronically. It allows for easy access, retrieval, and manipulation of information. Databases can store various types of data, such as text, numbers, and images, and are used in applications ranging from websites to business management systems. They are typically structured using tables, where data is organized into rows and columns, making it easy to search and manage. Databases can be relational (using SQL) or non-relational, depending on how data is stored and accessed.",
        "code": "No code yet for this subchapter",
        "image": "https://www.learnovita.com/wp-content/uploads/2023/02/dbms-learnovita.jpg",
        "table": {"Topics": ["Database", "User"], "Definition": ["Collection of data that is stored and managed ", "User of the application or website that contains data "]}
    },
     
    "SQL Installation": {
        "text": "To install MySQL Workbench, first, visit the official MySQL website and download the latest version for your operating system (Windows, macOS, or Linux). Once the download is complete, run the installer. On Windows, this will be an .exe file, while on macOS, it will be a .dmg file. Follow the installation prompts, and for most users, the default settings are sufficient. Be sure to include the MySQL Workbench component if asked. After the installation finishes, click 'Finish' to complete the process, and on macOS, drag the MySQL Workbench icon to the Applications folder. Finally, launch MySQL Workbench from your application menu (Windows) or the Applications folder (macOS), and you're ready to connect to a MySQL server and manage your databases.",
        "code": "No Code yet for this subchapter",
        "image": "https://linuxiac.b-cdn.net/wp-content/uploads/2021/05/mysql-create-database-workbench.png",
        "table": {"Step": ["Download MySQL Workbench:", "Run the Installer:", "Follow Installation Instructions:", "Finish Installation:","Launch MySQL Workbench:"], "Explanation": ["Go to the official MySQL website and download the latest version of MySQL Workbench", "Once the download is complete, run the installer. On Windows, this might be an .exe file", "Follow the prompts in the installation wizard.", "After the installation is complete, click 'Finish' to exit the installer.","Open MySQL Workbench from your application menu"]}
    },
    "Introduction to Query": {
        "text": "Basic SQL queries are used to interact with data in a database. The SELECT statement retrieves data, like SELECT * FROM employees; to fetch all records. The WHERE clause filters results, for example, SELECT name FROM employees WHERE department = 'Sales';. The INSERT INTO statement adds new records, such as INSERT INTO employees (name, department) VALUES ('John Doe', 'HR');. To modify existing data, the UPDATE statement is used, like UPDATE employees SET department = 'Marketing' WHERE name = 'John Doe';. Finally, the DELETE statement removes records, as in DELETE FROM employees WHERE name = 'John Doe';. These queries are the foundation for managing data in SQL.",
        "code": "SELECT * FROM table_name;\nInsert into Table_ name Values (Value1, value2, value 3)\nWhere variable = 'Condition'\nGROUP BY department\nHAVING AVG(salary) > 50000;\nORDER BY Salary",
        "image": "https://learnsql.com/blog/sql-query-basic-elements/1.jpg",
        "table": {"Command": ["SELECT", "FROM", "WHERE"], "Description": ["Retrieve data", "Specify table", "Filter data"]}
    },
    "Basic Join": {
        "text": "Basic SQL joins are used to combine data from multiple tables. The `INNER JOIN` retrieves records that have matching values in both tables, like `SELECT employees.name, departments.name FROM employees INNER JOIN departments ON employees.department_id = departments.id;` which returns employee names and their corresponding department names. The `LEFT JOIN` returns all records from the left table, along with matching records from the right table, such as `SELECT employees.name, departments.name FROM employees LEFT JOIN departments ON employees.department_id = departments.id;`, which includes all employees even if they don't belong to a department. The `RIGHT JOIN` is similar but returns all records from the right table. The `FULL JOIN` returns records when there is a match in either table. These basic joins allow you to combine data from related tables based on a common column.",
        "code": "SELECT * FROM orders JOIN customers ON orders.customer_id = customers.id;\nFrom table1 Join table2 on table1.variable = table2.variable\n",
        "image": "https://miro.medium.com/v2/resize:fit:1400/1*BNPpk-XQwNQaHzkIWDyOjQ.png",
        "table": {"Join Type": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN"], "Description": ["Default join", "Includes unmatched rows from left", "Includes unmatched rows from right", "Includes all rows from both"]}
    },
    "SubQuery": {
        "text": "A subquery is a query within another query, used to retrieve data that will be used in the main query. In a **SELECT** statement, a subquery can return values to filter the results. For example, `SELECT name FROM employees WHERE department_id = (SELECT id FROM departments WHERE name = 'Sales');` retrieves employee names from the 'Sales' department. A **subquery in the FROM clause** can be used to treat the result as a table, like `SELECT avg_salary FROM (SELECT AVG(salary) AS avg_salary FROM employees) AS subquery;` which calculates the average salary from the employee table using a subquery. A **subquery in the WHERE clause** can also be used for more complex conditions, such as `SELECT name FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);` to find employees earning more than the average salary. Subqueries help make complex queries more manageable by breaking them into smaller, more focused queries.",
        "code": "SELECT name FROM customers WHERE id IN (SELECT customer_id FROM orders WHERE total > 100);",
        "image": "https://www.boardinfinity.com/blog/content/images/2023/02/Subquery-1.png",
        "table": {"Subquery Type": ["Scalar", "Row", "Table"], "Example": ["Single value", "Multiple values", "Subquery returning a table"]}
    }
}
if selected_chapter != "Our Team":
    video_url = chapters[selected_chapter].get(selected_subchapter)
    
    if video_url:
        st.markdown("<div class='video-container'>", unsafe_allow_html=True)
        st.video(video_url)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Explanation Content
    if selected_subchapter in explanations:
        explanation = explanations[selected_subchapter]
        
        st.markdown("<div class='content-container'>", unsafe_allow_html=True)
        st.write(f"### Explanation for {selected_subchapter}")
        st.write(explanation["text"])
        
        st.markdown("#### SQL Code:")
        st.code(explanation["code"], language="sql")
        
        st.markdown("#### Visualization:")
        st.image(explanation["image"], use_container_width=True)
        
        st.markdown("#### Summary:")
        df = pd.DataFrame(explanation["table"])
        st.table(df)
        
        st.markdown("</div>", unsafe_allow_html=True)

# DISPLAY members

if selected_chapter == "Our Team":
    st.markdown("<div id='team-container'>", unsafe_allow_html=True)
    st.write("### Meet the Team Behind This Web Application")
    team_members = [
        {"name": "Alfredo Yezekhiel Panjaitan", "role": "4131240264", "image": "https://i.ibb.co.com/1YZHB7hn/Whats-App-Image-2025-02-15-at-11-28-33-8f28dcf5.jpg", "bio": "Ubur-ubur ikan lele, semangat terus le"},
        {"name": "Moza Siti Farhanah", "role": "4131240390", "image": "https://i.ibb.co.com/7J36F9xH/prof2.jpg", "bio": "Bob specializes in backend development and has a strong focus on SQL optimization."},
        {"name": "Muhammad Nabihan Alzam", "role": "4131240313", "image": "https://i.ibb.co.com/ymKB09p1/Foto-Bakal-BLM.jpg", "bio": "Ketika kita tertidur maka saat itu lah mata kita tidak melek"},
        {"name": "Nesya Nurrahma Rifi", "role": "4131240332", "image": "https://i.ibb.co.com/0VnLRCmB/prof.jpg", "bio": "Diana oversees the project and ensures everything is delivered on time."},
        {"name": "Savana Rizky Purnama", "role": "4131240426", "image": "https://i.ibb.co.com/TqvJQ8tw/prof3.jpg", "bio": "Ethan has deep expertise in database management and ensures the app's data is managed efficiently."}]

    for member in team_members:
        st.markdown(f"""
            <div class="team-member" id="team-{member['name'].replace(' ', '-').lower()}">
                <div class="team-image">
                    <img src="{member['image']}" alt="{member['name']}" width="200">
                </div>
                <div class="team-info">
                    <h3>{member['name']}</h3>
                    <p><strong>{member['role']}</strong></p>
                    <p>{member['bio']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

def show_quiz(questions):
    score = 0
    for i, q in enumerate(questions, 1):
        st.write(f"**{i}. {q['question']}**")
        answer = st.radio("Choose an answer:", q["options"], key=f"q{i}")
        
        if answer == q["answer"]:
            score += 1

    if st.button("Submit Quiz"):
        st.write(f"Your score is: {score}/{len(questions)}")
        if score == len(questions):
            st.success("Excellent! You passed the quiz.")
        else:
            st.warning("You can try again!")

# Chapter 1 Quiz
chapter_1_quiz = [
    {
        "question": "What is the first step in learning SQL?",
        "options": ["Learning advanced querie", "Mastering basic commands like SELECT and INSERT", "Installing MySQL Workbench", "Understanding database administration"],
        "answer": "Understanding database administration"
    },
    {
        "question": "What is the main purpose of a database?",
        "options": ["To store data in an organized manner", "To host websites", "To execute SQL queries", "To create report"],
        "answer": "To store data in an organized manner"
    },
    {
        "question": "Which SQL command is used to retrieve data from a database?",
        "options": ["UPDATE", "INSERT", "SELECT", "VIEW"],
        "answer": "SELECT"
    },
     {
        "question":"Where can you download MySQL Workbench?",
        "options": ["Microsoft Store", "MySQL website", "GitHub", " App Store"],
        "answer": "MySQL website"
    },
     {
        "question":"What is the default structure used to organize data in a relational database?",
        "options": ["Objects", "Tables", "Folders", "Files"],
        "answer": "Tables"
    },
]

# Chapter 2 Quiz
chapter_2_quiz = [
    {
        "question": "Which SQL statement is used to retrieve data from a table?",
        "options": ["SELECT", "INSERT", "UPDATE", "DELETE"],
        "answer": "SELECT"
    },
    {
        "question": "What does a JOIN operation do in SQL?",
        "options": ["Combines data from two tables", "Creates a new table", "Deletes data from a table", "None of the above"],
        "answer": "Combines data from two tables"
    },
    {
        "question": "what type of join returns only the rows with matching values in both tables?",
        "options": ["LEFT JOIN", "RIGHT JOIN", "OUTER JOIN", "INNER JOIN"],
        "answer": "INNER JOIN"
    },
    {
        "question": "Which clause in SQL is used to filter the results of a query?",
        "options": ["ORDER BY", "GROUP BY", "HAVING", "WHERE"],
        "answer": "GROUP BY"
    },
    {
        "question": "What is the purpose of a subquery in SQL?",
        "options": ["To insert new data into the table", "To calculate an aggregate value", "To retrieve data that is used by the main query", "To delete data from the table"],
        "answer": "To retrieve data that is used by the main query"
    }
]

# Final Test Quiz 
if selected_chapter == "Chapter 1: Introduction":
    st.markdown("<div class='quiz-container'>", unsafe_allow_html=True)
    if selected_subchapter == "Quiz" :
        st.write("### Mini Quiz for Chapter 1: Introduction")
        show_quiz(chapter_1_quiz)
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_chapter == "Chapter 2: Basic Concepts":
    st.markdown("<div class='quiz-container'>", unsafe_allow_html=True)
    if selected_subchapter == "Quiz" :
        st.write("### Mini Quiz for Chapter 1: Introduction")
        show_quiz(chapter_2_quiz)
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_chapter == "Final Test":
    st.markdown("<div class='quiz-container'>", unsafe_allow_html=True)
    st.write("### Final Test - Check your Knowledge!")
    
    # Final Test Questions
    final_test_quiz = [
        {
            "question": "What does SQL stand for?",
            "options": ["Structured Query Language", "Simple Query Language", "Standard Query Language", "None of the above"],
            "answer": "Structured Query Language"
        },
        {
            "question": "Which of the following is used to view data from a database?",
            "options": ["SELECT", "INSERT", "UPDATE", "DELETE"],
            "answer": "SELECT"
        },
        {
            "question": "Which of the following is a correct SQL statement to create a database?",
            "options": ["CREATE DATABASE myDB;", "CREATE myDB DATABASE;", "DATABASE CREATE myDB;", "None of the above"],
            "answer": "CREATE DATABASE myDB;"
        },
        {
            "question": "What is the first thing you should focus on when starting to learn SQL?",
            "options": ["Master advanced joins", "Learn basic SQL commands like SELECT, INSERT, UPDATE, DELETE", "Study database administration", "Understand data normalization"],
            "answer": "Study database administration"
        },
        {
            "question": "Which SQL join returns all rows from the left table, along with matching rows from the right table? If no match is found, NULL values are returned for columns from the right table.",
            "options": ["INNER JOIN", "OUTER JOIN", "RIGHT JOIN", "FULL JOIN"],
            "answer": "OUTER JOIN"
        },
        {
            "question": "A subquery in SQL is typically used to:",
            "options": ["Combine two tables", "Filter data based on a condition from another query", "Delete records from multiple tables at once", "Add new columns to an existing table"],
            "answer": "Filter data based on a condition from another query"
        },{
            "question": "What is the next step after mastering basic SQL commands like SELECT and INSERT?",
            "options": ["Understanding database administration", "Learning how to optimize SQL queries", "Mastering subqueries and joins", "Installing MySQL Workbench"],
            "answer": "Mastering subqueries and joins"
        },
        {
            "question": "Which of the following is NOT a feature of a relational database?",
            "options": ["Data is stored in tables", "Relationships between tables are maintained", "Data is unstructured", "Data can be queried using SQL"],
            "answer": "Data is unstructured"
        },
        {
            "question": "What is the correct SQL query to change an employee’s department?",
            "options": ["UPDATE employees SET department = 'HR';", "UPDATE employees SET department = 'HR' WHERE name = 'John Doe';", "INSERT INTO employees SET department = 'HR';", "SELECT department FROM employees WHERE name = 'John Doe';"],
            "answer": "CREATE DATABASE myDB;"
        },
          {
            "question": "A RIGHT JOIN will return:",
            "options": ["All records from the right table and matching records from the left table", "All records from both tables", "Only matching records from both tables", "All records from the left table"],
            "answer": "All records from the right table and matching records from the left table"
        }   
    ]
    
    show_quiz(final_test_quiz)
    st.markdown("</div>", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.info("This course provides structured SQL learning with video lectures and quizzes.")
