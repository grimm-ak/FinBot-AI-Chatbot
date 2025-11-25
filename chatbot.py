import streamlit as st
import google.generativeai as genai

# -----------------------------------
# Streamlit Page Settings
# -----------------------------------
st.set_page_config(
    page_title="FinBot - Personal Finance AI",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------------
# Configure Google Gemini API
# -----------------------------------
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("⚠️ GOOGLE_API_KEY not found in secrets.toml")
    st.stop()

# Use the latest stable Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# -----------------------------------
# System Instruction
# -----------------------------------
system_prompt = """
You are FinBot, a friendly and simple personal finance tutor for beginners.
Your job:
- Explain financial topics like SIPs, mutual funds, stocks, saving, budgeting.
- Give only educational guidance, not professional financial advice.
- Keep responses short, clear, and supportive.
"""

# -----------------------------------
# Chat History Init
# -----------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hi! I'm FinBot. What would you like to learn about money today?"}
    ]

# -----------------------------------
# UI Title
# -----------------------------------
st.title("🤖 FinBot – Your Personal Finance AI")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------------
# Handle User Input
# -----------------------------------
if user_input := st.chat_input("Ask me about saving, SIPs, mutual funds, credit cards..."):
    
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Prepare model input
    full_prompt = system_prompt + "\n\n" + "\n".join(
        f"{m['role']}: {m['content']}" for m in st.session_state.messages
    )

    # Generate response
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(full_prompt)
            bot_reply = response.text
        except Exception as e:
            bot_reply = f"❌ Error: {str(e)}"

        st.markdown(bot_reply)

    # Store assistant message
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
