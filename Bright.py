import streamlit as st
import pandas as pd
from googletrans import Translator

# Load the dataset from GitHub
url = "https://raw.githubusercontent.com/kark1982/agricultural-chatbot/main/Book1.csv"
df = pd.read_csv(url)

# Ensure column names are correctly formatted
df.columns = df.columns.str.strip()

# Initialize Translator
translator = Translator()

# Title of the chatbot
st.title("Agricultural Chatbot for Ghanaian Farmers")

# Select Language
languages = {
    "English": "en",
    "Twi": "tw",
    "Hausa": "ha",
    "Ewe": "ee",
    "French": "fr"
}
selected_lang = st.selectbox("Choose Language", list(languages.keys()))

# Get user input
query = st.text_input("Enter crop or disease:")

# Search dataset for matching crop or disease
if query:
    query = query.lower().strip()
    
    row = df[df.apply(lambda x: x.get("Crop", "").lower().strip() in query or x.get("Disease", "").lower().strip() in query, axis=1)]

    if row.empty:
        response = "❌ Sorry, no information found for this crop/disease."
    else:
        # Get solution
        solution = row.iloc[0]["Solution"]
        
        # Translate solution to selected language
        translated_solution = translator.translate(solution, dest=languages[selected_lang]).text
        response = f"✅ Solution ({selected_lang}): {translated_solution}"

    st.write(response)
