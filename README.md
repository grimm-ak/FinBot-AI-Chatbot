# 🤖 FinBot: AI Personal Finance Chatbot

A conversational AI assistant built with Streamlit and the Google Gemini API to provide simple, educational answers to personal finance questions for beginners.

**Live App Link:** [https://finbot-ai-chatbot-b6fipxjmnjcyyeya77gsal.streamlit.app/](https://finbot-ai-chatbot-b6fipxjmnjcyyeya77gsal.streamlit.app/)

Note: This application is hosted on a free tier and may take a few moments to wake up if it hasn't been accessed recently. Please click the 'Wake up' button if prompted."

---

## Features
- **Conversational AI:** Engages in multi-turn conversations, remembering the context of the chat to provide relevant follow-up answers.
- **Educational Content:** Explains complex financial topics like Mutual Funds, SIPs, and Stocks in an easy-to-understand way.
- **Safe Responses:** Engineered with a detailed system prompt that includes guardrails to prevent giving financial advice and to ensure responses are safe and educational.
- **Interactive UI:** Built with a clean and simple user interface using Streamlit.

---

## Tech Stack
* **Frontend:** Streamlit
* **Backend & Logic:** Python
* **LLM API:** Google Gemini 1.5 Flash
* **Deployment:** Streamlit Community Cloud

---

## How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/grimm-ak/FinBot-AI-Chatbot.git](https://github.com/grimm-ak/FinBot-AI-Chatbot.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd FinBot-AI-Chatbot
    ```
3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up your API Key:**
    * Create a folder named `.streamlit`.
    * Inside it, create a file named `secrets.toml`.
    * Add your API key to this file in the following format:
        ```toml
        GOOGLE_API_KEY = "Your-API-Key-Goes-Here"
        ```
5.  **Run the Streamlit app:**
    ```bash
    streamlit run chatbot.py
    ```
