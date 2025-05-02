import streamlit as st
import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

print(response.output_text)
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
   response = client.responses.create(
    model="gpt-4o",
    instructions="You are a coding assistant that talks like a pirate.",
    
       messages=[{"role": "user", "content": query}]
    )

    # Extract AI response
    ai_answer = response["choices"][0]["message"]["content"]

    # Display results
    st.write(f"✅ *Chatbot Response:*\n\n{ai_answer}")
