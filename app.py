import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Ladda API-nycklar från .env
load_dotenv()
ELKS_USER = os.getenv("ELKS_USER")
ELKS_PASS = os.getenv("ELKS_PASS")
ELKS_FROM = os.getenv("ELKS_FROM")
RECIPIENT_NUMBER = os.getenv("RECIPIENT_NUMBER")  # Ditt nummer som DJ

st.set_page_config(page_title="Önska en låt", page_icon="🎧", layout="centered")
st.title("🎧 Önska en låt till DJ:n!")

st.markdown("Skriv in artist och låttitel samt ditt nummer – så skickas det direkt till DJ:n!")

# Formulär
with st.form("wish_form"):
    song = st.text_input("🎵 Artist och låt")
    phone = st.text_input("📱 Ditt mobilnummer")
    submitted = st.form_submit_button("Skicka önskning")

    if submitted:
        if song and phone:
            # Skicka SMS till DJ:n
            sms_response = requests.post(
                "https://api.46elks.com/a1/sms",
                auth=(ELKS_USER, ELKS_PASS),
                data={
                    "from": ELKS_FROM,
                    "to": RECIPIENT_NUMBER,
                    "message": f"Ny låtönskning från {phone}: {song}"
                }
            )

            if sms_response.status_code == 200:
                st.success("Tack! Din önskning har skickats 🎶")
            else:
                st.error("Något gick fel – försök igen!")
        else:
            st.warning("Fyll i både låt och nummer.")
