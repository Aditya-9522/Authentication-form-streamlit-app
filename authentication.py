import streamlit as st
import mysql.connector

def create_table_login():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS login (
            username VARCHAR(50) PRIMARY KEY,
            password VARCHAR(50) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    login()
    
def create_table_register():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS register (
            id VARCHAR(20) PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            username VARCHAR(50) UNIQUE NOT NULL,
            email VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            password VARCHAR(50) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    register()

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="student_db"
    )

def register():
    st.title("Register")
    with st.form("register_form"):
        id=st.text_input("Student ID:")
        first_name=st.text_input("First Name:")
        last_name=st.text_input("Last Name:")
        username=st.text_input("Username:")
        email=st.text_input("Email:")
        age=st.number_input("Age:",min_value=0,max_value=150,step=1)
        password=st.text_input("Password:",type='password')
        register_button=st.form_submit_button("Register")
        
    if(register_button):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO register (id, first_name, last_name, username, email, age, password)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (id, first_name, last_name, username, email, age, password))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Registered successfully!...You can login now.")
        st.balloons()
    
def login():
    st.title("Login")
    with st.form("login_form"):
        username=st.text_input("Username:")
        password=st.text_input("Password:",type='password')
        login_button=st.form_submit_button("Login")
        
    if(login_button):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM register WHERE username=%s AND password=%s
        """, (username, password))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            st.success("Logged in successfully!")
            st.balloons()
        else:
            st.error("Invalid username or password.")

def main():
    st.sidebar.title("Student Portal")
    option=st.sidebar.radio("Select Option:",["REGISTER","LOGIN"])
    if(option=="REGISTER"):
        create_table_register()
    elif(option=="LOGIN"):
        create_table_login()

if __name__ == "__main__":
    main()