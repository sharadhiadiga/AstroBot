import streamlit as st

# Set page config
st.set_page_config(page_title="🧠 Space Trivia Quiz", layout="centered")

# Cosmic Style
st.markdown("""
    <style>
    body {
        background-color: #0d1b2a;
        color: #e0e1dd;
    }
    .question {
        font-size: 20px;
        font-weight: bold;
    }
    .score {
        font-size: 22px;
        color: #fca311;
    }
    button {
        background-color: #fca311 !important;
        color: black !important;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Quick-Fire Space Quiz")
st.markdown("Think you’re a true space cadet? Let’s test your cosmic knowledge! 🌌")

# Quiz data
questions = [
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What galaxy is Earth located in?",
        "options": ["Andromeda", "Messier 87", "Milky Way", "Sombrero"],
        "answer": "Milky Way"
    },
    {
        "question": "Who was the first human in space?",
        "options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Alan Shepard"],
        "answer": "Yuri Gagarin"
    },
    {
        "question": "How many moons does Jupiter have (as of 2023)?",
        "options": ["1", "27", "53", "92"],
        "answer": "92"
    },
    {
        "question": "What is the hottest planet in our solar system?",
        "options": ["Mercury", "Venus", "Mars", "Neptune"],
        "answer": "Venus"
    }
]

# Score tracker
if "score" not in st.session_state:
    st.session_state.score = 0
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Display questions
user_answers = []
for i, q in enumerate(questions):
    st.markdown(f"**Q{i+1}: {q['question']}**")
    answer = st.radio(f"Question {i+1}", q["options"], key=f"q{i}")
    user_answers.append(answer)
    st.markdown("---")

# Submit button
if st.button("🚀 Submit Answers"):
    score = 0
    for i, q in enumerate(questions):
        if st.session_state[f"q{i}"] == q["answer"]:
            score += 1
    st.session_state.score = score
    st.session_state.submitted = True

# Show result
if st.session_state.submitted:
    st.markdown(f"### 🎉 You scored: **{st.session_state.score} / {len(questions)}**")
    if st.session_state.score == len(questions):
        st.success("🌟 Cosmic Genius! You aced it!")
    elif st.session_state.score >= 3:
        st.info("🚀 Not bad, space cadet!")
    else:
        st.warning("🛸 Keep training, rookie!")
