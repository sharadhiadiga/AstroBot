🌌 AstroBot – Your Cosmic Space Companion 🚀

AstroBot is an interactive Streamlit-based space exploration app that brings together:

Fun chatbots 🤖

NASA Astronomy Picture of the Day integration 📸

Space facts & history 📅

Planet data 🌍🪐

Interactive quizzes 🧠

📂 Project Structure
📦 AstroBot
├── 1_streamlit_app.py     # Sample calculator demo (Streamlit basics)
├── astrobot.py            # Main interactive AstroBot app
├── echo_bot.py            # Lightweight chat-based bot
├── quiz.py                # Space trivia quiz app
├── planet_data.json       # Planet facts & descriptions
├── quiz_data.json         # Quiz dataset (questions + answers)

✨ Features

AstroBot Chat – Ask about planets, black holes, Sun, or NASA facts.

NASA APOD – Fetch Astronomy Picture of the Day via NASA API.

Space History – See what happened on today’s date in space.

Solar System Explorer – Learn about each planet in detail.

Quizzes – Test your space knowledge with interactive quizzes.

Streamlit UI – Styled with custom CSS for a cosmic feel.

🚀 Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/AstroBot.git
cd AstroBot

2. Create & activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt


(If requirements.txt is missing, install manually:)

pip install streamlit requests

4. Run the app

Choose one of the Streamlit apps:

streamlit run astrobot.py


Other apps you can try:

streamlit run echo_bot.py
streamlit run quiz.py
streamlit run 1_streamlit_app.py

🔑 API Key Setup (Optional for NASA Features)

The app uses NASA’s Astronomy Picture of the Day (APOD) API.
Currently, it uses DEMO_KEY which has limits.
To get your own API key:

Visit NASA API Portal
.

Generate a free API key.

Replace DEMO_KEY in the code (astrobot.py / echo_bot.py) with your key.

📖 Data Files

planet_data.json → Planet details (type, distance from Sun, moons, description).

quiz_data.json → Space quiz questions and answers.

📜 License

This project is open-source under the MIT License.
