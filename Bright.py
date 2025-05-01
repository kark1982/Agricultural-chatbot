import streamlit as st
import pandas as pd
from googletrans import Translator

# Load crop disease dataset
url = "https://raw.githubusercontent.com/kark1982/agricultural-chatbot/main/Book1.csv"
df = pd.read_csv(url)

translator = Translator()

# Supported languages
language_codes = {
    "english": "en", "twi": "tw", "ga": "gaa", "ewe": "ee", "hausa": "ha"
}

def get_crop_disease_info(query):
 row = df[df.apply(lambda x: x.get("Crop", "").lower() in query and x.get("Disease", "").lower() in query, axis=1)]

if 'row' not in locals():
    response = "Error: Data retrieval failed."

elif not row.empty:
    response = row.iloc[0]["Solution"]
else:
    response = "Sorry, no information found for this crop/disease."

# Streamlit UI
st.title("🌾 Agricultural Chatbot for Farmers in Ghana")
st.write("Ask about crops, diseases and solutions!")

user_input = st.text_input("Enter your crop disease query:")
language = st.selectbox("Choose language:", list(language_codes.keys()))

if st.button("Get Info"):
    response = get_crop_disease_info(user_input)
    
    if language != "english":
        response = {key: translator.translate(value, dest=language_codes[language]).text for key, value in response.items()}
    
    st.write(response)
