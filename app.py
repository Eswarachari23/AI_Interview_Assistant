import streamlit as st

st.title("AI Interview Preparation Assistant")

skill = st.text_input("Enter Skill")

if st.button("Generate Questions"):
    st.write("1. Explain OOP concepts.")
    st.write("2. What is polymorphism?")
    st.write("3. Difference between interface and abstract class?")