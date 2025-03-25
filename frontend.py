import streamlit as st
import requests

st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")

# UI Components
system_prompt = st.text_area("Define your AI Agent:", height=70, 
                           placeholder="Type your system prompt here...")

provider = st.radio("Select Provider:", ("Groq", "DeepSeek", "GoogleAI"))  # Added GoogleAI

model_options = {
    "Groq": ["llama3-70b-8192", "llama-3.3-70b-versatile"],
    "DeepSeek": ["deepseek/deepseek-r1-zero:free", "deepseek/deepseek-r1-distill-qwen-32b:free"],
    "GoogleAI": ["gemini-2.0-pro-exp-02-05","gemini-1.5-flash"]  # Added GoogleAI models
}

selected_model = st.selectbox("Select Model:", model_options[provider])
allow_web_search = st.checkbox("Enable Web Search", value=True)
user_query = st.text_area("Enter your query:", height=150, placeholder="Ask Anything!")


API_URL = "https://recent-jourdan-ustec-17c8d79f.koyeb.app/chat"
if st.button("Ask Agent!"):
    if user_query.strip():
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [{"role": "user", "content": user_query}],
            "allow_search": allow_web_search
        }

        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                result = response.json()
                st.subheader("Agent Response")
                st.write(result.get("response", "No response"))  # Use st.write instead of st.success
            else:
                st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
        except Exception as e:
            st.error(f"Connection error: {str(e)}")