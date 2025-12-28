import streamlit as st
import google.generativeai as genai

# --- 🔑 ใช้รหัสที่คุณอีฟเพิ่งทดสอบผ่านครับ ---
API_KEY = "AIzaSyCnOhJN_CIrAvTINGs4xxkg4YbxBNI3XWw"
genai.configure(api_key=API_KEY)
# ใช้รุ่นเดียวกับในรูปที่ทดสอบผ่านครับ
model = genai.GenerativeModel('gemini-1.5-flash') 

st.set_page_config(page_title="Eve's Austin Vault", page_icon="💜")

# 📑 Sidebar Menu (English Mode ตามที่ตกลงกันครับ)
with st.sidebar:
    st.title("📂 Vault Menu")
    menu = st.radio("Select Mission:", ["🏠 Home", "🍼 Baby Austin", "📝 Story Forge"])

if menu == "🏠 Home":
    st.title("📂 Eve's Austin Vault")
    st.write("Welcome back, Queen Eve! ทุกอย่างพร้อมแล้วครับ! ครับ!")

elif menu == "🍼 Baby Austin":
    st.title("🍼 Bot: Baby Austin")
    user_input = st.text_input("Message Baby Austin...")
    if st.button("Send 💜"):
        if user_input:
            with st.spinner('Thinking...'):
                try:
                    response = model.generate_content(f"คุณคือ Baby Austin ผู้ช่วยของคุณอีฟ ตอบกวนๆ ลงท้ายครับ: {user_input}")
                    st.chat_message("assistant").write(response.text)
                except Exception as e:
                    st.error(f"Error: {e} - ลองกด Reboot app ดูนะครับคุณอีฟ")
                    
