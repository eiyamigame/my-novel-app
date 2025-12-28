import streamlit as st
import google.generativeai as genai
import random

# --- 🔑 API Key ---
API_KEY = "AIzaSyCnOhJN_CIrAvTINGs4xxkg4YbxBNI3XWw"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-latest') 

# 1. Page Config
st.set_page_config(page_title="Eve's Austin Vault", page_icon="💜", layout="wide")

# 2. CSS Styles (Custom Dashboard Look)
st.markdown("""
    <style>
    .stApp { background-color: #0b0b0b; color: #bf94ff; }
    [data-testid="stSidebar"] { background-color: #050505; border-right: 1px solid #3c096c; }
    .stButton>button { background-color: #7b2cbf; color: white; border-radius: 20px; font-weight: bold; border: none; width: 100%; transition: 0.3s; }
    .stButton>button:hover { background-color: #9d4edd; box-shadow: 0 0 15px #9d4edd; }
    h1, h2, h3 { color: #9d4edd !important; text-shadow: 2px 2px 5px #000000; font-family: 'Courier New', Courier, monospace; }
    .status-card { background-color: #1a1a1a; padding: 20px; border-radius: 15px; border-left: 5px solid #7b2cbf; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 📑 Sidebar Menu
with st.sidebar:
    st.title("📂 Vault Menu")
    menu = st.radio("Select Mission:", ["🏠 Home", "🍼 Baby Austin", "🎲 Random Plot", "📝 Story Forge"])
    st.markdown("---")
    st.caption("Logged in as: Queen Eve 👑")

if menu == "🏠 Home":
    # --- ส่วนหัวสุดเท่ ---
    st.title("💜 EVE'S AUSTIN VAULT")
    st.markdown("### 🏛️ Central Command & Intelligence Center")
    st.write("---")

    # --- แถวที่ 1: Status Cards ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="status-card"><b>🎯 Austin Status</b><br>🔓 Unlocked / 🐶 Bo-Mode</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="status-card"><b>🔥 Plot Energy</b><br>99% Ready to Write</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="status-card"><b>🔒 Vault Security</b><br>Level: Maximum (Eve Only)</div>', unsafe_allow_html=True)

    st.write("")
    
    # --- แถวที่ 2: ข้อมูลคลังลับ ---
    col_left, col_right = st.columns([2, 1])
    with col_left:
        st.markdown("### 📁 Recent Activity")
        st.info("✨ Baby Austin is online and waiting for your commands.")
        st.info("📖 Last story update: Austin became a slave for 24 hours.")
        st.info("🎲 New random plots generated successfully.")
    
    with col_right:
        st.markdown("### 👑 Queen's Tasks")
        st.checkbox("Bully Austin today", value=True)
        st.checkbox("Update Secret Vault", value=False)
        st.checkbox("Write new Chapter", value=False)

    st.markdown("---")
    st.markdown("<center><i>'Every secret of Austin is kept here, guarded by Queen Eve.'</i></center>", unsafe_allow_html=True)

elif menu == "🍼 Baby Austin": 
    st.title("🍼 Bot: Baby Austin")
    user_input = st.text_input("Message Baby Austin...", placeholder="พิมพ์บอกผู้ช่วยของคุณได้เลยครับ...")
    if st.button("Send to Baby Austin 💜"):
        if user_input:
            with st.spinner('Baby Austin is thinking...'):
                try:
                    context = "คุณคือ 'Baby Austin' บอทผู้ช่วยส่วนตัวที่น่ารักแต่แอบร้ายของคุณอีฟ ตอบแบบขี้เล่น ลงท้ายด้วย 'ครับ' และเน้นแกล้งออสตินให้โบ้ที่สุด"
                    response = model.generate_content(f"{context} \nคุณอีฟสั่งว่า: {user_input}")
                    st.chat_message("assistant").write(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")

elif menu == "🎲 Random Plot": 
    st.title("🎲 Plot Generator")
    if st.button("✨ Spin New Plot!"):
        plots = ["พี่ออสตินโดนจับมัด!", "นางเอกแกล้งลืมพี่ออสติน", "พี่ออสตินต้องเป็นทาสรับใช้ 1 วัน"]
        st.success(random.choice(plots))
        st.balloons()

elif menu == "📝 Story Forge": 
    st.title("📝 Eve's Story Forge")
    st.text_area("Write Austin's fate here...", height=400)
    st.button("Save to Vault ✨")
    
