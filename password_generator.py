import streamlit as st
import random
import string

st.title("Password Generator")

st.header("Welcome! Create your own unique password below:")

# Choose your password length
num_length = st.number_input("Choose your password length:", min_value=5, max_value=24, value=8)

# User chooses whether uppercase values will be included
upper_include = st.checkbox("Include uppercase letters?")

# User chooses whether symbol values will be included
symbol_include = st.checkbox("Include symbols?")

# Define the symbol cart
symbol_cart = '!@#$%^&*'

# Define the generate_pass function
def generate_pass(size=num_length, chars=string.ascii_lowercase + string.digits + (string.ascii_uppercase if upper_include else '') + (symbol_cart if symbol_include else '')):
    return ''.join(random.choice(chars) for _ in range(size))

# When the button is pressed, generate the password
generate_btn = st.button("Generate Password")
if generate_btn:
    new_pass = generate_pass()
    st.text("Your new password is:")
    st.text_area("Generated Password", new_pass, height=50)
    






