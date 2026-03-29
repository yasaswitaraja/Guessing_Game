import streamlit as st
import random
# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Page config
st.set_page_config(page_title="Guess The Number 🎯", page_icon="🎯")

# Title
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>🎯 Guess The Number Game</h1>",
    unsafe_allow_html=True
)

st.write("### I'm thinking of a number between 1 and 100 🤔")

# Input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Submit button
if st.button("Submit Guess"):
    if not st.session_state.game_over:
        st.session_state.attempts += 1

        if guess < st.session_state.number:
            st.warning("📉 Too low! Try again.")
        elif guess > st.session_state.number:
            st.warning("📈 Too high! Try again.")
        else:
            st.success("🎉 Correct! You guessed it!")
            st.balloons()
            st.write(f"### Attempts: {st.session_state.attempts}")
            st.session_state.game_over = True

# Restart button
if st.button("Restart Game 🔄"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.rerun()