import streamlit as st

# Set page title
st.set_page_config(page_title="SQL Lecture - Chapter 1", layout="wide")

# Sidebar Navigation
st.sidebar.title("SQL Lecture")
st.sidebar.markdown("Navigate through the lecture sections:")
page = st.sidebar.button("Go to", ["Introduction", "Basic Concepts", "SQL Queries", "Examples", "Practice"])

# Introduction
if page == "Introduction":
    st.title("Introduction to SQL")
    st.write("Structured Query Language (SQL) is the standard language for relational database management systems.")
    st.markdown("### What You Will Learn:")
    st.markdown("- What is SQL?")
    st.markdown("- Why SQL is important?")
    st.markdown("- Basic SQL structure")

# Basic Concepts
elif page == "Basic Concepts":
    st.title("Basic SQL Concepts")
    st.markdown("### Key Topics:")
    st.write("- Databases and Tables")
    st.write("- SQL Data Types")
    st.write("- Primary Keys and Foreign Keys")
    st.write("- SQL Syntax Rules")

# SQL Queries
elif page == "SQL Queries":
    st.title("Writing SQL Queries")
    st.markdown("### Common SQL Commands:")
    st.code("""
    SELECT column1, column2 FROM table_name;
    INSERT INTO table_name (column1, column2) VALUES (value1, value2);
    UPDATE table_name SET column1 = value1 WHERE condition;
    DELETE FROM table_name WHERE condition;
    """, language='sql')

# Examples
elif page == "Examples":
    st.title("SQL Query Examples")
    st.write("Here are some example queries:")
    st.code("""
    -- Creating a table
    CREATE TABLE Students (
        ID INT PRIMARY KEY,
        Name VARCHAR(50),
        Age INT
    );
    
    -- Inserting data
    INSERT INTO Students (ID, Name, Age) VALUES (1, 'Alice', 22);
    """, language='sql')

# Practice
elif page == "Practice":
    st.title("Practice Writing SQL Queries")
    query = st.text_area("Write your SQL query below:")
    if st.button("Run Query"):
        st.write("Query execution feature coming soon!")

st.sidebar.markdown("---")
st.sidebar.info("This lecture is part of the SQL course. Stay tuned for more!")
