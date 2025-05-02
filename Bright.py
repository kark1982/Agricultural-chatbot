import streamlit as st
import pandas as pd
from googletrans import Translator

# Load the dataset from GitHub
url = "https://github.com/kark1982/Agricultural-chatbot/blob/main/crops.csv"
df = pd.read_csv(url)


# Ensure column names are correctly formatted
df.columns = df.columns.str.strip()

# Initialize Translator
translator = Translator()

# Title of the chatbot
st.title("🌱 Agricultural Chatbot for Farmers")

# Select Language
languages = {
    "English": "en",
    "Hausa": "ha",
    "French": "fr"
}
selected_lang = st.selectbox("Choose Language", list(languages.keys()))

# User Input for Disease
disease_input = st.text_input("Enter the disease affecting the crop:")

if disease_input:
    # Normalize user input
    disease_query = disease_input.lower().strip()
    
    # Search dataset for matching disease
    row = df[df["Disease"].str.lower().str.strip() == disease_query]

    if row.empty:
        translated_message = translator.translate(
            "Sorry, no information found for this disease.", dest=languages[selected_lang]
        ).text
        st.write(translated_message)
    else:
        # Retrieve disease information
        crop = row.iloc[0]["Crop"]
        cause = row.iloc[0]["Cause"]
        symptoms = row.iloc[0]["Symptoms"]
        solution = row.iloc[0]["Solution"]

        # Construct full message in English
        response_text = (
            f"Oh no! {disease_query.capitalize()} can really affect your {crop}. "
            f"It's usually caused by {cause}. You might notice symptoms like {symptoms}. "
            f"{solution} to help your crop become healthy"
        )

        # **Translate the entire message, not just individual words**
        translated_response = translator.translate(response_text, dest=languages[selected_lang]).text

        # Display the fully translated response
        st.write(translated_response)
