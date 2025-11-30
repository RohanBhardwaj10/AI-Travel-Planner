import streamlit as st
from datetime import datetime
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD=os.getenv("EMAIL_PASSWORD")

client = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile"
)

st.set_page_config(page_title="AI Travel Planner", layout="centered")
st.title("🌍 AI Travel Planner — Streamlit + ChatGroq + Email")

with st.form("trip_form"):
    home = st.text_input("Your Location (city or country)", value="Delhi")
    dest = st.text_input("Destination (city or country)", value="Paris")
    start = st.date_input("Start date", value=datetime.today())
    end = st.date_input("End date", value=datetime.today())
    interests = st.text_input("Interests (comma-separated)", value="culture, food")
    budget = st.text_input("Approx budget (optional)", placeholder="e.g. 1500 or ₹50000")
    tone = st.selectbox("Tone", ["Practical", "Luxury", "Backpacker", "Romantic"])
    email = st.text_input("Enter your email to receive the itinerary (optional)")
    submitted = st.form_submit_button(" Generate itinerary")

if submitted:
    if end < start:
        st.error("End date must be the same or after start date.")
    else:
        days = (end - start).days + 1
        st.info(f"Planning a {days}-day trip to {dest}...")

        prompt = f"""
You are a helpful travel planner assistant.
User trip:
- Current Location: {home}
- Destination: {dest}
- Dates: {start.isoformat()} to {end.isoformat()} ({days} days)
- Interests: {interests}
- Budget: {budget or 'Flexible'}
- Tone: {tone}

Produce a day-by-day itinerary (Day 1, Day 2, ...), 3–4 activities per day (morning/afternoon/evening),
one recommended restaurant or local dish per day, and short travel tips. Also write on the first line if the budget in rupees is sufficient for the particular destination to travel. Also make it visually pleasing with attractive creativeness and emojis. Respond in markdown format.
"""

        with st.spinner("Generating itinerary..."):
            try:
                response = client.invoke(
                    input=[
                        {"role": "system", "content": "You are a concise, factual travel assistant."},
                        {"role": "user", "content": prompt},
                    ]
                )

                itinerary = response.content
                st.markdown(itinerary)

                html_itinerary = markdown.markdown(itinerary)

                msg = MIMEMultipart("alternative")
                msg["Subject"] = f"Your {dest} Itinerary from AI Travel Planner"
                msg["From"] = EMAIL_ADDRESS
                msg["To"] = email


                msg.attach(MIMEText(itinerary, "plain"))
                msg.attach(MIMEText(html_itinerary, "html"))

                try:
                    with smtplib.SMTP("smtp.gmail.com", 587) as server:
                        server.starttls()
                        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                        server.send_message(msg)
                        st.success(f"📧 Itinerary sent successfully to {email}")
                except Exception as email_error:
                    st.error(f"Email sending failed: {email_error}")


                st.download_button(
                    "📄 Download Itinerary",
                    itinerary,
                    file_name=f"{dest}_itinerary.txt"
                )

            except Exception as e:
                st.error(f"Error: {e}")
