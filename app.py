import streamlit as st

st.set_page_config(
    page_title="Grade Calculator",
    page_icon="🎓"
)

st.title("🎓 Student Grade Calculator")

# Student Details
name = st.text_input("Enter Student Name")

# Subject Marks
st.subheader("Enter Marks")

sub1 = st.number_input("Python", 0, 100)
sub2 = st.number_input("Java", 0, 100)
sub3 = st.number_input("Database", 0, 100)
sub4 = st.number_input("Networking", 0, 100)
sub5 = st.number_input("Web Technology", 0, 100)

# Calculate Button
if st.button("Calculate Result"):

    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    result = "PASS" if percentage >= 40 else "FAIL"

    st.success(f"Student Name: {name}")
    st.success(f"Total Marks: {total}/500")
    st.success(f"Percentage: {percentage:.2f}%")
    st.success(f"Grade: {grade}")
    st.success(f"Result: {result}")
