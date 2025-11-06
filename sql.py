from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
import os
import sqlite3

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(question,prompt):
    # Checking list of available models
    # for model in genai.list_models():
    #     print(f"Name: {model.name}, Description: {model.description}")
    model = genai.GenerativeModel("gemini-2.5-pro")
    
    response = model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(query, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    data = cursor.execute(query)
    results = data.fetchall()
    for row in results:
        st.write(row)
        print(row)
    conn.close()
    return results

prompt = ["""You are an expert SQL query generator and expert in converting English natural language questions to SQL queries.
          The SQL database has the name students.db and has the table students with the following columns:
          NAME,CLASS,SECTION \n\n For example, \nExample 1 - How many records are there in the students table? 
          \nSQL Query returned will be SELECT COUNT(*) FROM students; 
          \n Example 2 - List all the records from the students table where CLASS is '10th Grade'. 
          \nSQL Query returned will be SELECT * FROM students WHERE CLASS='10th Grade'; 
          Also the code should not have ``` in the beginning or end of the SQL query and the word 'SQL' in the output.
          """]

st.set_page_config(page_title="Text to SQL using Gemini 2.5 Pro", page_icon=":guardsman:", layout="wide")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Enter your question for the students database:", key="question_input")
submit_button = st.button("Ask the Question")


if submit_button and question:
    with st.spinner("Generating SQL Query..."):
        sql_query = get_gemini_response(question,prompt)
        st.subheader("Generated SQL Query:")
        st.code(sql_query, language='sql')
 
    with st.spinner("Executing SQL Query..."):
        st.subheader("Query Results:")
        results = read_sql_query(sql_query, 'student.db')
        if not results:
            st.write("No results found.")   



