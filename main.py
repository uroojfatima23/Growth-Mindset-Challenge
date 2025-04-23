import streamlit as st
import random
import time

# Custom CSS for colors and style
st.markdown("""
    <style>
        body {
            background-color: #FFF0F5;
        }
        .stApp {
            background-color: #FAF3F3;
        }
        h1 {
            color: #FF69B4;
        }
        h3 {
            color: #8A2BE2;
        }
        .stButton > button {
            background-color: #FFB6C1;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            height: 3em;
        }
        .stTextInput, .stTextArea {
            background-color: #fff0f5;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.title("🌸 Urooj's Growth Mindset Challenge")
st.markdown("<h3>Welcome to your daily boost of positivity and purpose!</h3>", unsafe_allow_html=True)
st.write("Each day, you'll receive a motivational quote and a simple challenge to help grow your mindset 💫")

# Quotes
quotes = [
    "Failure is an opportunity to grow. - Kevin Kruse 🚀",
    "I can learn anything I want to. - Carol S. Dweck 🧠",
    "Effort is what makes you smart or talented. - Carol S. Dweck 🌟",
    "Challenges help me to grow. - Carol S. Dweck 🌱",
    "My effort and attitude determine everything. - Carol S. Dweck 🌈",
    "I believe in my ability to improve. - Carol S. Dweck 🎯",
    "I love a challenge! - Carol S. Dweck 😍",
    "Feedback is a gift that helps me grow. - Carol S. Dweck 🎁",
]

# Challenges
challenges = [
    "Take 10 minutes to learn something new today.",
    "Set a goal for the week and create a plan to achieve it.",
    "Write about a time you turned a failure into a learning experience.",
    "List three new things you want to learn this month.",
    "Try something outside your comfort zone today and reflect on the experience.",
    "Write a letter to your future self, encouraging growth and perseverance.",
    "Read a book or article on a topic you're curious about.",
    "Reach out to someone you admire and ask for advice.",
    "Set one small goal today and take action towards achieving it.",
]

# Random selections
quote = random.choice(quotes)
challenge = random.choice(challenges)

# Display content
st.info(f"🌼 **Quote of the Day**: _{quote}_")
st.success(f"🧠 **Today's Challenge**: _{challenge}_")

# Session state
if "thoughts" not in st.session_state:
    st.session_state.thoughts = []
if "user_challenge" not in st.session_state:
    st.session_state.user_challenge = None

# User's Custom Challenge
st.subheader("💡  Create Your Own Challenge!")
user_challenge = st.text_input("Write your own challenge:")

if st.button("📌 Submit Challenge"):
    if not user_challenge.strip():
        st.error("⚠ Please enter a challenge before submitting!")
    elif st.session_state.user_challenge is not None:
        st.warning("⚠ You have already submitted a challenge today!")
    else:
        st.session_state.user_challenge = user_challenge.strip()
        st.success("✅ Your challenge has been saved!")

# Show stored challenge
if st.session_state.user_challenge:
    st.subheader("📌 Your Custom Challenge:")
    st.write(f"📝 {st.session_state.user_challenge}")

# User Thoughts Section
st.subheader("📝 Your Growth Journal")
user_response = st.text_area("How do you feel about today's challenge?", key="challenge_feeling")

if len(st.session_state.thoughts) < 3:
    if st.button("✅ Submit Your Response"):
        if not user_response.strip():
            st.error("⚠ Please share your thoughts before submitting!")
        else:
            st.session_state.thoughts.append(user_response.strip())
            st.success(f"🎉 Your thought has been recorded! ({len(st.session_state.thoughts)}/3 thoughts submitted)")
            time.sleep(1)
            st.rerun()
else:
    st.warning("⚠ You have already submitted 3 thoughts today! Try again tomorrow.")

# Show Thoughts
if st.session_state.thoughts:
    st.subheader("📚 Your Submitted Thoughts:")
    for idx, thought in enumerate(st.session_state.thoughts, start=1):
        st.write(f"{idx}. {thought}")