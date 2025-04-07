# Låtönskningssystem för DJ 🎧

Ett enkelt system där gäster kan önska låtar via en landningssida. Byggt med Python, Streamlit och 46elks.

## Funktioner
- Besökare fyller i en låt + sitt nummer
- Du som DJ får ett SMS med önskningen via 46elks

## Kom igång
1. Skapa `.env` i roten av projektet med:
```
ELKS_USER=din_användare
ELKS_PASS=ditt_lösenord
ELKS_FROM=MagicDeejay
RECIPIENT_NUMBER=+4670XXXXXXX
```

2. Installera och kör:
```
pip install -r requirements.txt
streamlit run app.py
```
