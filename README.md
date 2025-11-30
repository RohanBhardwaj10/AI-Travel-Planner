## Overview

AI Travel Planner is an intelligent web application that creates personalized travel itineraries based on the user’s destination, dates, budget, interests, and preferred travel style.
It uses the Groq LLaMA-3.3 70B model via LangChain to generate day-wise travel plans with activities, food recommendations, and tips.
The app also allows users to receive itineraries via email and download them as text files.

## Features

🗺 AI-Generated Day-by-Day Itinerary using Groq LLM

💸 Budget check for selected destination

⏳ Start/End date selection with automatic day calculation

❤️ Personalized itineraries based on interests & travel tone

📧 Email delivery of itinerary (HTML + plain text)

⬇️ Download option for saving itinerary

🖥 Simple and fast UI built with Streamlit

## Tech Stack

Python

Streamlit – UI

LangChain + Groq API – LLM integration

Markdown – Rendering

SMTP / Gmail API – Email sending

dotenv – Secure environment variable handling

## Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/yourusername/ai-travel-planner.git
cd ai-travel-planner

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Add your environment variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key_here
EMAIL_ADDRESS=your_gmail_here
EMAIL_PASSWORD=your_app_password_here


- Gmail now requires App Passwords for SMTP (Not your login password).

▶️ Run the Application
streamlit run app.py


Your app will run at:

http://localhost:8501/



## Project Structure
├── app.py
├── requirements.txt
├── .env (not uploaded)
├── README.md
## How It Works

User enters travel details in the form

App creates a detailed prompt

Prompt sent to Groq LLM via LangChain

Response rendered in markdown

Optional: itinerary emailed to the user

Optional: download as .txt file

## Future Enhancements

Live flight & hotel price integration

Google Maps / Places API for real-time data

Save user itinerary history

Multi-language support

Export itinerary to PDF
------------------------
Pull requests are welcome!
For major changes, please open an issue first to discuss what you would like to change.
