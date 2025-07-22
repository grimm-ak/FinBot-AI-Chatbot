import streamlit as st
import google.generativeai as genai
import os

# --- PAGE CONFIGURATION ---
# Sets the title and icon that appear in the browser tab
st.set_page_config(
    page_title="FinBot - Your Personal Finance AI",
    page_icon="🤖",
    layout="centered"
)

# --- GOOGLE GEMINI API SETUP ---
# This is the correct way to get the API key for a local Streamlit app.
# It automatically reads from a file named .streamlit/secrets.toml
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception as e:
    # If the key is not found, show an error message
    st.error("API key not found. Please create a .streamlit/secrets.toml file and add your GOOGLE_API_KEY.")
    st.stop() # Stop the app from running further

# --- MODEL AND CHATBOT LOGIC ---

# Set up the generative model to use the latest Gemini Flash model
model = genai.GenerativeModel('gemini-1.5-flash')

# This is the "brain" of your chatbot. It's the master instruction.
system_prompt = """
You are FinBot, a friendly and helpful AI assistant for young adults learning about personal finance.
Your goal is to explain complex financial topics in a simple, easy-to-understand way.
You must not give financial advice. Only provide educational information.
Keep your answers concise and encouraging.
"""

# Initialize the chat history in Streamlit's session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [
        # Start with a greeting from the assistant
        {"role": "assistant", "content": "Hello! I'm FinBot. How can I help you understand personal finance today?"}
    ]

# --- USER INTERFACE ---

# Display the title of the app
st.title("🤖 FinBot - Your Personal Finance AI")

# Display the existing chat messages from the history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get new input from the user from the chat input box at the bottom
if prompt := st.chat_input("Ask about mutual funds, SIPs, stocks..."):
    
    # Add the user's new message to the chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display the user's new message on the screen
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display the assistant's response
    with st.chat_message("assistant"):
        # Create a new prompt for the model that includes the system instructions and the history
        # This gives the model context for the conversation
        prompt_for_model = system_prompt + "\n\n" + "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
        
        # Call the API to get the response
        response = model.generate_content(prompt_for_model)
        response_text = response.text
        
        # Display the AI's response on the screen
        st.markdown(response_text)
    
    # Add the AI's response to the chat history
    st.session_state.messages.append({"role": "assistant", "content": response_text})