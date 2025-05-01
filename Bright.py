import streamlit as st
import openai
import os
# Securely fetch API key from Streamlit secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

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
crop_query = st.text_input("🌿 Enter a crop name or ask a question:")

if crop_query:
    # Generate the query for ChatGPT
    query = f"Provide detailed information about {crop_query}. Include common diseases, causes, symptoms, and solutions."

    # Send query to OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": query}]
    )

    # Extract AI response
    ai_answer = response["choices"][0]["message"]["content"]

    # Display results
    st.write(f"✅ *Chatbot Response:*\n\n{ai_answer}")
