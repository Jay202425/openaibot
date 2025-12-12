import streamlit as st
import os
from openai import OpenAI

# Set page config
st.set_page_config(
    page_title="OpenAI Bot",
    page_icon="🤖",
    layout="wide"
)

# Initialize the OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("⚠️ OPENAI_API_KEY environment variable not set!")
    st.stop()

client = OpenAI(api_key=api_key)

# App title and description
st.title("🤖 OpenAI Bot - GPT-5.2")
st.write("Chat with OpenAI's latest model. Type your message and get instant responses!")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if user_input := st.chat_input("Type your message here..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-5.2",
                    messages=[
                        {
                            "role": "user",
                            "content": user_input
                        }
                    ]
                )
                bot_response = response.choices[0].message.content
                st.markdown(bot_response)
                
                # Add bot response to history
                st.session_state.messages.append({"role": "assistant", "content": bot_response})
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Sidebar with info
with st.sidebar:
    st.title("ℹ️ Information")
    st.write("**Model:** GPT-5.2")
    st.write("**API:** OpenAI")
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
