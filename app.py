import streamlit as st
import google.generativeai as genai
import random

# --- 🔑 API Key ของคุณอีฟ ---
API_KEY = "AIzaSyDzqa4yK0DS2wOg6UE7XJOlqz5E9uwmyXc"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 1. ตั้งค่าหน้าแอป
st.set_page_config(page_title="Eve's Austin Vault", page_icon="💜")

# 2. ธีมม่วง-ดำ และ CSS สวยๆ
st.markdown("""
    <style>
    .stApp { background-color: #0b0b0b; color: #bf94ff; }
    .stButton>button { background-color: #7b2cbf; color: white; border-radius: 15px; width: 100%; font-weight: bold; border: none; }
    h1, h2, h3 { color: #9d4edd !important; text-shadow: 2px 2px 4px #000000; }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea { background-color: #1a1a1a; color: #bf94ff; border: 1px solid #7b2cbf; }
    [data-testid="stSidebar"] { background-color: #050505; border-right: 1px solid #3c096c; }
    </style>
    """, unsafe_allow_html=True)

# 📑 เมนู Sidebar
with st.sidebar:
    st.title("📂 Main Menu")
    menu = st.radio("เลือกภารกิจ:", ["🏠 หน้าหลัก (The Vault)", "🍼 คุยกับเบบี้ออสติน", "🎲 สุ่มพล็อตแก้ตัน", "📝 ห้องปั่นนิยาย"])

if menu == "🏠 หน้าหลัก (The Vault)":
    # --- 📸 โชว์รูปหน้าปกที่คุณอีฟชอบ ---
    st.image("https://r2.erweima.ai/i/0_IovDNoQvub9YvI417Mow.png", use_container_width=True)
    st.title("📂 Eve's Austin Vault")
    st.write("ยินดีต้อนรับสู่คลังลับของคุณอีฟ! ทุกความลับของพี่ออสตินถูกเก็บไว้ที่นี่แล้วครับ! ครับ!")

elif menu == "🍼 คุยกับเบบี้ออสติน":
    st.title("🍼 บอท: เบบี้ออสติน")
    user_input = st.text_input("สั่งงานเบบี้ออสติน...")
    if st.button("ส่งคำสั่งให้เบบี้ 💜"):
        if user_input:
            with st.spinner('กำลังคิดให้ครับ...'):
                context = "คุณคือ 'เบบี้ออสติน' บอทผู้ช่วยส่วนตัวของคุณอีฟ ตอบแบบขี้เล่น กวนนิดๆ ลงท้ายด้วย 'ครับ' และเน้นแกล้งออสตินให้โบ้ที่สุด"
                prompt = f"{context} \nคุณอีฟสั่งว่า: {user_input}"
                response = model.generate_content(prompt)
                st.chat_message("assistant").write(response.text)

elif menu == "🎲 สุ่มพล็อตแก้ตัน":
    st.title("🎲 สุ่มพล็อต")
    if st.button("✨ กดสุ่มพล็อตใหม่!"):
        plots = ["พี่ออสตินโดนจับมัด!", "นางเอกแกล้งลืมพี่ออสติน", "พี่ออสตินต้องเป็นทาสรับใช้ 1 วัน"]
        st.info(random.choice(plots))
        st.balloons()

elif menu == "📝 ห้องปั่นนิยาย":
    st.title("📝 ปั่นนิยาย")
    st.text_area("ละเลงความโบ้ตรงนี้เลยครับ...", height=400)
    st.button("บันทึกเนื้อหา ✨")
    
    
