import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="FinBot", page_icon="🤖")

# Configure API key
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Missing GOOGLE_API_KEY in Streamlit secrets")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Use a valid model for google-generativeai==0.8.5
model = genai.GenerativeModel("gemini-1.5-flash")


system_prompt = """
You are FinBot, a friendly personal finance tutor. 
Explain money concepts simply. No professional advice.
"""


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm FinBot. Ask me anything about money, saving, SIPs, budgeting!"}
    ]


st.title("🤖 FinBot – Personal Finance AI")

# Display previous messages
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])


# Input box
user_input = st.chat_input("Type your question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # Build conversation
    prompt = system_prompt + "\n\n"
    for m in st.session_state.messages:
        prompt += f"{m['role']}: {m['content']}\n"

    # Call Gemini
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            reply = response.text
        except Exception as e:
            reply = f"Error: {e}"

        st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
