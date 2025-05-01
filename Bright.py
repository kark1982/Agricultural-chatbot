import streamlit as st
import openai
import os

# Fetch API key securely from Streamlit secrets
openai.api_key = openai.api_key = os.getenv("OPENAI_API_KEY")

# Title of the chatbot
st.title("🌱 Agricultural AI Chatbot")

# Select Language
languages = {
    "English": "en",
    "Twi": "tw",
    "Hausa": "ha",
    "Ewe": "ee",
    "French": "fr"
}
selected_lang = st.selectbox("Choose Language", list(languages.keys()))

# User input
query = st.text_input("🌿 Ask about a crop or disease:")

if query:
    # Generate AI-powered query
    prompt = f"Provide detailed information about {query}. Include common diseases, causes, symptoms, and solutions."

    # Send query to OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    # Extract AI response
    ai_answer = response["choices"][0]["message"]["content"]

    # Display results
    st.write(f"✅ *Chatbot Response:*\n\n{ai_answer}")
