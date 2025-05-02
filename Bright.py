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
st.title("🌱 Agricultural Chatbot for Farmers")

# Select Language
languages = {
    "English": "en",
    "Hausa": "ha",
    "French": "fr"
}
selected_lang = st.selectbox("Choose Language", list(languages.keys()))

# User Inputs for  Disease
disease_input = st.text_input("Enter the disease affecting the crop:")

if disease_input:
    # Normalize user inputs
    disease_query = disease_input.lower().strip()
    
    # Search dataset for matching disease
    row = (df["Disease"].str.lower().str.strip() == disease_query)

    if row.empty:
        st.write("Sorry, no information found for this disease.")
    else:
        # Retrieve disease information
        cause = row.iloc[0]["Cause"]
        symptoms = row.iloc[0]["Symptoms"]
        solution = row.iloc[0]["Solution"]
        
        # Translate information to the selected language
        translated_cause = translator.translate(cause, dest=languages[selected_lang]).text
        translated_symptoms = translator.translate(symptoms, dest=languages[selected_lang]).text
        translated_solution = translator.translate(solution, dest=languages[selected_lang]).text
        
        # Display the results
        (f"Oh no! {Disease} can really affect your crops. This disease mainly affect {Crop}. "
         f"It's usually caused by {Cause}. You might notice symptoms like {Symptoms}. "
         f"But the good news is that you can manage it by using {Solution}. ")
