import streamlit as st

st.header("P. Aditya Vardhan 23EG107A45")

st.title("Welcome to Student Database")

st.subheader("Manage Student Records Efficiently")

st.markdown("---------------------------*Hello*--------------------------------")
st.markdown("<h3 style='color:red;'>Student Management System</h3>", unsafe_allow_html=True)
st.markdown("For more information, visit [B48 Anurag University](https://www.anurag.edu.in)")

st.text("This application allows you to manage student records, including adding new students, updating existing records, and viewing student information.")

#important method
c=3
st.write(c)

st.caption("This is a caption for the student management system.")

st.code("""
def add(a,b):
    return a+b
        """,language='python')

st.latex(r''' E = mc^2''')

st.divider()

if(st.button("Click me")):
    st.text("Oo yeah!!")
    st.success("Button clicked successfully!")
    st.balloons()
else:
    st.text("Please click the button")
st.divider()

name=st.text_input("Enter Student Name:")
if(not name.isalpha() or name!=""):
    st.error("Invalid input")
else:
    st.success(f"Hello, {name}!")
st.divider()

if(st.checkbox("Accept the terms and conditions")):
    st.text("Now you can proceed further.")
st.divider()

gender=st.radio("Select Gender:",("Male","Female","Other"))
st.write(f"You selected: {gender} hehehe")
st.divider()

country=st.selectbox("Select Country:",["India","USA","UK","Canada","Australia"])
st.divider()

course=st.multiselect("Select Course:",["B.Tech","M.Tech","MBA","PhD"])
st.write(f"You selected: {course}")
st.divider()

st.slider("Select your age:",0,100)
st.divider()

file=st.file_uploader("Upload Student Document:")
if(file is not None):
    st.success("File uploaded successfully!")
    st.write(f"Filename: {file.name}")
st.divider()

with st.form("student_form"):
    id=st.text_input("Student ID:")
    name=st.text_input("Student Name:")
    email=st.text_input("Student Email:")
    age=st.number_input("Student Age:",min_value=0,max_value=150,step=1)
    submit=st.form_submit_button("Submit")
if(submit):
    st.success("Form submitted successfully!")
st.divider()

with st.form("login_form"):
    username=st.text_input("Username:")
    password=st.text_input("Password:",type='password')
    login=st.form_submit_button("Login")
if(login):
    st.success("Logged in successfully!")
st.divider()

col1,col2,col3,col4=st.columns(4)
with col1:
    st.subheader("ID")
    st.text("23EG107A45")
with col2:
    st.subheader("Name")
    st.text("P. Aditya Vardhan")
with col3:
    st.subheader("Course")
    st.text("B.Tech AIML")
with col4:
    st.subheader("College")
    st.text("Anurag University")
st.divider()

con=st.container()
con.write("This is inside the container.")
if(con.button("Container Button")):
    con.success("Container inside button clicked!")
st.divider()

data = {
    'Name': ['Anurag', 'Anudeep', 'Aditya'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)
st.divider()

st.sidebar.title("Daily Tasks")
option=st.sidebar.radio("Select Option:",["HOME","COLLEGE","GYM"])
st.sidebar.write(f"You selected: {option}")

@st.cache_data
def compute_square(n):
    return n * n
num=st.number_input("Enter a number to compute its square:",min_value=0,step=1)
if(st.button("Compute Square")):
    result=compute_square(num)
    st.success(f"The square of {num} is {result}.")
st.divider()
