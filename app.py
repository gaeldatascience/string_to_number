import streamlit as st
from main import string_to_number

st.set_page_config(
    page_title="String to Number Converter",
    page_icon="🔢",
    layout="centered"
)

st.title("🔢 String to Number Converter")
st.markdown("Convert written numbers to their numeric value")

# Input
user_input = st.text_input(
    "Enter a number in words:",
    placeholder="e.g., twenty three"
)

# Quick examples
examples = [
    "twenty three",
    "one hundred twenty three", 
    "five thousand six hundred seventy eight",
    "one million two hundred thousand"
]

selected_example = st.selectbox("Quick examples:", [""] + examples)

if selected_example:
    user_input = selected_example

# Convert and display result
if user_input.strip():
    try:
        result = string_to_number(user_input.strip().lower())
        st.success(f"**Result:** {result:,}")
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.info("Please check spelling and use English words only.")
