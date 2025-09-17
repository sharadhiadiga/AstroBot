import streamlit as st
import requests
from datetime import datetime

# Page setup
st.set_page_config(page_title="AstroBot", layout="centered")

# Cosmic styling
st.markdown("""
    <style>
    body {
        background-color: #0d1b2a;
        color: #e0e1dd;
    }
    .stChatInput > div {
        background-color: #1b263b !important;
        color: white !important;
        border-radius: 12px;
    }
    button {
        background-color: #fca311 !important;
        color: black !important;
        border-radius: 10px;
    }
    .stMarkdown {
        font-family: 'Consolas', monospace;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌌 AstroBot - Your Cosmic Chat Companion")

# 📅 Today in Space History
today = datetime.now().strftime("%m-%d")
space_history = {
    "04-16": "🚀 On April 16, 1972, Apollo 16 launched. Time to moonwalk, cadet!",
    "07-20": "🌕 On July 20, 1969, humans first landed on the Moon. One giant leap!",
    "12-04": "🛰️ December 4, 1998: NASA launched the Unity module for the ISS!"
}
if today in space_history:
    st.markdown(f"### 📅 Today in Space History:\n{space_history[today]}")

# 🚀 AstroBot Launchpad (Redirect Buttons)
st.markdown("## 🚀 AstroBot Launchpad")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🔭 NASA Missions"):
        st.markdown("[Go to NASA Missions](https://www.nasa.gov/missions)")
with col2:
    if st.button("🇮🇳 ISRO Launches"):
        st.markdown("[Go to ISRO Launches](https://www.isro.gov.in/launches.html)")
with col3:
    if st.button("📆 Upcoming Events"):
        st.markdown("[Go to Space Events](https://www.nasa.gov/events)")

# 🌌 NASA APOD (Astronomy Picture of the Day)
def get_nasa_fact():
    try:
        url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"  # Replace with real API key
        response = requests.get(url)
        data = response.json()
        return f"📸 **{data['title']}**\n\n{data['explanation']}\n\n![NASA Image]({data['url']})"
    except:
        return "Oops! I lost signal with NASA HQ. Try again later, space cadet."

# 💬 Chatbot Response Logic
def generate_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "🚀 AstroBot here! Ready to explore the cosmos with you!"
    elif "fact" in user_input or "nasa" in user_input:
        return get_nasa_fact()
    elif "black hole" in user_input:
        return "A black hole is a region in space where gravity is so strong that even light can't escape. Mind-blowing, right? 🕳️"
    elif "sun" in user_input:
        return "The Sun is a massive ball of hydrogen and helium—basically a huge fusion reactor. 🔆"
    elif "mars" in user_input:
        return "Mars is known as the Red Planet. Maybe the future home of humans? 🛸"
    elif "planet" in user_input:
        return "🪐 Our solar system has 8 planets... and yes, Pluto still waves from the Kuiper Belt!"
    elif "bye" in user_input:
        return "🌠 AstroBot signing off. May your orbits be ever stable!"
    else:
        return "🛰️ Beep beep... rerouting space signals. Try asking about black holes, Mars, or the Sun 🌞"

# 🧠 Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box
user_input = st.chat_input("Ask me something spacey...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = generate_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        st.markdown(response)
