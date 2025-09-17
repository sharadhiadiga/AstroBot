import streamlit as st

# Remember stream_app.py is always the start point for a streamlit application

# Sample Header in streamlit
st.header("Sample Calculator")

# Sample Text Input
name = st.text_input("Your name ?")

# Sample Input in streamlit
number_1 = st.number_input("First Number")
number_2 = st.number_input("Second Number")

#sample_dropdown in streamlit
operator = st.selectbox("Operator",["+", "*","/","-"])

# Sample button in streamlit -
if st.button("Calculate"):
    if operator == "+":
        # Write the code to sum up two numbers (number_1,number_2)
        result = number_1 + number_2
    elif operator == "*":
        # Write the code to multiply two numbers (number_1,number_2)
        result = number_1 * number_2
    elif operator == "/":
        # Write the code to divide two numbers (number_1,number_2)
        result = number_1 / number_2
    elif operator == "-":
        # Write the code to subtract two numbers (number_1,number_2)
        result = number_1 - number_2
    # Add a case for modulus operator
    else:
        # Invalid operator
        st.write("Invalid operator")
    if result != 0:
        st.subheader(f"Hey! {name} {number_1} {operator} {number_2} is {result}. 😃")
        st.balloons()
    else:
        st.write("Recheck the code")
        st.error("Something went wrong")