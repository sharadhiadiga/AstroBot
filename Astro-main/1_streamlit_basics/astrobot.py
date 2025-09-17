import uuid
import streamlit as st
import requests
from datetime import datetime

# --- Page Setup ---
st.set_page_config(page_title="AstroBot - All-in-One", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #0d1b2a;
        color: #e0e1dd;
    }
    button {
        background-color: #fca311 !important;
        color: black !important;
        border-radius: 10px;
    }
    .stMarkdown {
        font-family: 'Consolas', monospace;
    }
    img {
        max-width: 400px;
        height: auto;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🪐 AstroBot: Your All-in-One Space Companion")

# --- Space History Dictionary ---
space_history = {
    "04-16": "🚀 On April 16, 1972, Apollo 16 launched. Time to moonwalk, cadet!",
    "07-20": "🌕 On July 20, 1969, humans first landed on the Moon. One giant leap!",
    "12-04": "🛰️ December 4, 1998: NASA launched the Unity module for the ISS!"
}

# --- Solar System Data ---
solar_system_data = {
    "mercury": "🪐 Mercury is the closest planet to the Sun and the smallest planet in our solar system.",
    "venus": "🪐 Venus has a thick, toxic atmosphere and is the hottest planet due to its greenhouse effect.",
    "earth": "🌍 Earth is the only planet known to support life and has vast oceans and diverse ecosystems.",
    "mars": "🛸 Mars is the red planet, known for its dusty landscape and the possibility of past water.",
    "jupiter": "🌟 Jupiter is the largest planet with a Great Red Spot—a giant storm bigger than Earth!",
    "saturn": "💍 Saturn is famous for its beautiful rings made of ice and rock particles.",
    "uranus": "🌀 Uranus rotates on its side and has a faint ring system. It's a gas giant with icy clouds.",
    "neptune": "🌊 Neptune is deep blue, windy, and the farthest known planet from the Sun.",
    "pluto": "❄️ Pluto is a dwarf planet with a heart-shaped glacier and orbits in the Kuiper Belt."
}

# --- NASA APOD API ---
def get_nasa_fact():
    try:
        url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
        data = requests.get(url).json()
        return f"📸 **{data['title']}**\n\n{data['explanation']}\n\n<img src='{data['url']}' width='400'>"
    except:
        return "🛰️ Sorry, lost contact with NASA. Try again later!"

# --- Quiz Function ---
quiz_questions = [
    {"q": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "a": "Mars"},
    {"q": "What galaxy is Earth located in?", "options": ["Andromeda", "Milky Way", "M87", "Sombrero"], "a": "Milky Way"},
    {"q": "Who was the first human in space?", "options": ["Armstrong", "Aldrin", "Yuri Gagarin", "Shepard"], "a": "Yuri Gagarin"},
]
def start_quiz():
    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False
    if "quiz_score" not in st.session_state:
        st.session_state.quiz_score = 0

    score = 0
    unique_id = "quiz_session"

    st.markdown("### 🌌 Space Quiz Time!")
    st.write("Answer the questions below:")

    all_answered = True
    for i, item in enumerate(quiz_questions):
        st.markdown(f"**Q{i+1}: {item['q']}**")
        key = f"q{i}_{unique_id}"
        choice = st.radio("Choose an option:", item["options"], key=key, index=None)
        if choice is None:
            all_answered = False
        elif choice == item["a"]:
            score += 1

    if not st.session_state.quiz_submitted:
        if st.button("🚀 Submit Quiz"):
            if all_answered:
                st.session_state.quiz_score = score
                st.session_state.quiz_submitted = True
            else:
                st.warning("❗ Please answer all questions.")

    if st.session_state.quiz_submitted:
        st.markdown(f"### ✅ You scored {st.session_state.quiz_score} / {len(quiz_questions)}!")
        if st.session_state.quiz_score == len(quiz_questions):
            st.success("🌟 Stellar job, space genius!")
        elif st.session_state.quiz_score == len(quiz_questions) - 1:
            st.info("🚀 You're orbiting greatness!")
        else:
            st.warning("🛸 Study your star maps and try again!")

        if st.button("🔁 Retake Quiz"):
            st.session_state.quiz_submitted = False

# --- Bot Reply Logic ---
def bot_reply(msg):
    msg = msg.lower()

    if msg.strip() in ["hi", "hello", "hey"]:
        return "👨‍🚀 Hello !! AstroBot at your service! Ask me anything about space!"

    elif "nasa" in msg or "fact" in msg:
        return get_nasa_fact()

    elif any(phrase in msg for phrase in ["today", "space history", "what happened today", "space event", "event today"]):
        today = datetime.now().strftime("%m-%d")
        return f"🗓️ **Today in Space History**\n\n{space_history.get(today, '🌠 Nothing major today, but space is always awesome!')}"

    elif "quiz" in msg:
        return "QUIZ_START"

    elif "launch" in msg or "events" in msg or "missions" in msg or "isro" in msg:
        return "LINKS"

    elif "solar system" in msg:
        return "🪐 Our solar system includes 8 planets orbiting the Sun. Ask about a specific planet for more info!"

    elif any(planet in msg for planet in solar_system_data):
        for planet in solar_system_data:
            if planet in msg:
                return solar_system_data[planet]

    elif "black hole" in msg:
        return "🕳️ A black hole is a region where gravity is so strong, not even light can escape."

    elif "milky way" in msg:
        return "🌌 The Milky Way is the galaxy that contains our solar system. It's a barred spiral galaxy with hundreds of billions of stars, and it's about 100,000 light-years across!"

    elif "sun" in msg:
        return "☀️ The Sun is a giant fusion reactor—burning hydrogen into helium for 4.6 billion years!"

    elif "bye" in msg:
        return "🌠 Signing off... until next orbit, space cadet!"

    else:
        return "🛰️ Hmm... I didn't get that. Try asking about NASA, planets, black holes, or launches!"

# --- Initialize Chat ---
if "chat" not in st.session_state:
    st.session_state.chat = []

# --- Chat Input ---
user_input = st.chat_input("Ask AstroBot anything...")

if user_input:
    st.session_state.chat.append(("user", user_input))
    response = bot_reply(user_input)
    st.session_state.chat.append(("bot", response))

# --- Display Chat ---
for role, msg in st.session_state.chat:
    with st.chat_message(role):
        if role == "bot":
            if msg == "QUIZ_START":
                st.markdown("### 🧠 Let's begin the space quiz!")
                start_quiz()
            elif msg == "LINKS":
                st.markdown("### 🚀 Launch Info Portals:")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.link_button("🔭 NASA Missions", "https://www.nasa.gov/missions")
                with col2:
                    st.link_button("🇮🇳 ISRO Launches", "https://www.isro.gov.in/launches.html")
                with col3:
                    st.link_button("📆 Upcoming Events", "https://www.nasa.gov/events")
                st.markdown("Here are the top space portals you can explore 🌌")
            else:
                st.markdown(msg, unsafe_allow_html=True)
        else:
            st.markdown(msg)
