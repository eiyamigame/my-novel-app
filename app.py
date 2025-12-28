import streamlit as st
import google.generativeai as genai
import random

# --- 🔑 API Key ---
API_KEY = "AIzaSyDzqa4yK0DS2wOg6UE7XJOlqz5E9uwmyXc"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro') 

# 1. Page Config
st.set_page_config(page_title="Eve's Austin Vault", page_icon="💜")

# 2. CSS Styles (Purple & Black)
st.markdown("""
    <style>
    .stApp { background-color: #0b0b0b; color: #bf94ff; }
    .stButton>button { background-color: #7b2cbf; color: white; border-radius: 20px; font-weight: bold; border: none; width: 100%; }
    h1, h2, h3 { color: #9d4edd !important; text-shadow: 2px 2px 4px #000000; }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea { background-color: #1a1a1a; color: #bf94ff; border: 1px solid #7b2cbf; }
    [data-testid="stSidebar"] { background-color: #050505; border-right: 1px solid #3c096c; }
    </style>
    """, unsafe_allow_html=True)

# 📑 Sidebar Menu
with st.sidebar:
    st.title("📂 Vault Menu")
    menu = st.radio("Select Mission:", ["🏠 Home", "🍼 Chat with Baby Austin", "🎲 Random Plot", "📝 Story Forge"])

if menu == "🏠 Home":
    st.title("📂 Eve's Austin Vault")
    st.write("Welcome to the secret vault, My Lady Eve! Everything is ready for you. ครับ!")

elif menu == "🍼 Chat with Baby Austin":
    st.title("🍼 Bot: Baby Austin")
    st.subheader("🗨️ Baby Austin's Command Center")
    user_input = st.text_input("Message Baby Austin...", placeholder="Type your command here...")
    
    if st.button("Send to Baby Austin 💜"):
        if user_input:
            with st.spinner('Baby Austin is thinking...'):
                try:
                    context = "You are 'Baby Austin', a cute but mischievous personal assistant bot for Eve. You treat Eve as your Queen and Austin as a naughty brother who needs to be tamed. Your tone is playful, end your sentences with 'ครับ' and focus on pleasing Eve."
                    response = model.generate_content(f"{context} \nEve says: {user_input}")
                    st.chat_message("assistant").write(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a command! ครับ!")

elif menu == "🎲 Random Plot":
    st.title("🎲 Plot Generator")
    if st.button("✨ Spin New Plot!"):
        plots = ["Austin gets tied up!", "Eve pretends to forget Austin.", "Austin must be a slave for a day."]
        st.info(random.choice(plots))
        st.balloons()

elif menu == "📝 Story Forge":
    st.title("📝 Eve's Story Forge")
    st.text_area("Write down Austin's fate here...", height=400)
    st.button("Save to Vault ✨")
    
