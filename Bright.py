import streamlit as st
import pandas as pd
from googletrans import Translator

# Load crop disease dataset
df = pd.read_csv("C:/Users/karko/OneDrive/Desktop/Book1.csv")

translator = Translator()

# Supported languages
language_codes = {
    "english": "en", "twi": "tw", "ga": "gaa", "ewe": "ee", "hausa": "ha"
}

def get_crop_disease_info(query):
    row = df[df.apply(lambda x: x["Crop"].lower() in query and x["Disease"].lower() in query, axis=1)]
    return row.to_dict(orient="records")[0] if not row.empty else {"response": "Crop/disease info not found."}

# Streamlit UI
st.title("🌾 Agricultural Chatbot for Farmers in Ghana")
st.write("Ask about crop diseases and solutions!")

user_input = st.text_input("Enter your crop disease query:")
language = st.selectbox("Choose language:", list(language_codes.keys()))

if st.button("Get Info"):
    response = get_crop_disease_info(user_input)
    
    if language != "english":
        response = {key: translator.translate(value, dest=language_codes[language]).text for key, value in response.items()}
    
    st.write(response)