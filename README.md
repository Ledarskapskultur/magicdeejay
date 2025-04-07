# 🎧 Låtönskningssystem för DJ

Detta projekt är en enkel webbapp där besökare kan önska låtar och skicka in sitt mobilnummer. Du som DJ får ett SMS med önskningen via 46elks.

## 🛠 Funktioner
- Gäst fyller i låt + mobilnummer
- Du får SMS till valfritt nummer
- Kodad i Python med Streamlit

## 🔧 Kom igång

1. Skapa en `.env`-fil i projektets rot med följande innehåll:

```
ELKS_USER=din_användare
ELKS_PASS=ditt_lösenord
ELKS_FROM=+4676XXXXXXX       # eller ett godkänt namn, max 11 tecken
RECIPIENT_NUMBER=+4670XXXXXXX  # ditt nummer som får SMS
```

2. Installera paketen:
```
pip install -r requirements.txt
```

3. Kör appen:
```
streamlit run app.py
```
