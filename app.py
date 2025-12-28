import streamlit as st
import google.generativeai as genai
import random

# --- 🔑 API Key (ใช้ชุดที่คุณอีฟทดสอบผ่านครับ) ---
API_KEY = "AIzaSyCnOhJN_CIrAvTINGs4xxkg4YbxBNI3XWw"
genai.configure(api_key=API_KEY)

# แก้ไขตรงนี้: เปลี่ยนรุ่นให้เป็น 'gemini-1.5-pro' เพื่อเลี่ยงปัญหา v1beta ครับ
model = genai.GenerativeModel('gemini-1.5-pro') 

# 1. Page Config
st.set_page_config(page_title="Eve's Austin Vault", page_icon="😈", layout="wide")

# 2. CSS Styles (ม่วง-ดำ และบัดเจทบอร์ด ไม่ให้หน้าโล่ง)
st.markdown("""
    <style>
    .stApp { background-color: #0b0b0b; color: #bf94ff; }
    [data-testid="stSidebar"] { background-color: #050505; border-right: 1px solid #3c096c; }
    .stButton>button { background-color: #7b2cbf; color: white; border-radius: 20px; font-weight: bold; border: none; width: 100%; transition: 0.3s; box-shadow: 0 4px 15px rgba(123, 44, 191, 0.3); }
    .stButton>button:hover { background-color: #9d4edd; box-shadow: 0 0 20px #9d4edd; }
    h1, h2, h3 { color: #9d4edd !important; text-shadow: 2px 2px 5px #000000; }
    .status-card { background-color: #1a1a1a; padding: 20px; border-radius: 15px; border-left: 5px solid #7b2cbf; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# 📑 Sidebar Menu
with st.sidebar:
    st.title("📂 Vault Menu")
    menu = st.radio("Select Mission:", ["🏠 Home", "😈 Baby Austin", "📝 Story Forge"])
    st.markdown("---")
    st.caption("Logged in as: Queen Eve 👑")

if menu == "🏠 Home":
    st.title("😈 EVE'S AUSTIN VAULT")
    st.markdown("### 🏛️ Central Command & Intelligence")
    st.write("---")

    # --- ส่วนแต่งเยอะๆ: Dashboard Cards ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="status-card"><b>🎯 Target: Austin</b><br>Status: 🐶 Bo-Mode Activated</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="status-card"><b>🔥 Evil Energy</b><br>Level: 666% (Max)</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="status-card"><b>🔒 Security</b><br>Encryption: Level 10</div>', unsafe_allow_html=True)

    st.write("")
    
    col_left, col_right = st.columns([2, 1])
    with col_left:
        st.markdown("### 📁 Intelligence Log")
        st.info("🔥 Baby Austin is now in 'Little Devil' mode and ready to bully.")
        st.info("📖 The secret vault is updated with new plots.")
        st.info("🎲 Connection with Gemini AI Studio: ESTABLISHED.")
    
    with col_right:
        st.markdown("### 👑 Queen's Task List")
        st.checkbox("Summon Little Devil", value=True)
        st.checkbox("Tease Austin", value=False)
        st.checkbox("Write Dark Plot", value=False)

elif menu == "😈 Baby Austin": 
    st.title("😈 Bot: Baby Austin (Little Devil)")
    st.subheader("🗨️ Speak to the Little Devil")
    user_input = st.text_input("สั่งงานปีศาจน้อยของคุณ...", placeholder="Talk to Baby Austin here...")
    
    if st.button("Send to Baby Austin 😈"):
        if user_input:
            with st.spinner('Baby Austin is preparing a sharp response...'):
                try:
                    # ปรับจูนบุคลิกปีศาจน้อย กวนๆ ลงท้ายครับ
                    context = "คุณคือ 'Baby Austin' ร่างปีศาจ (Little Devil) ผู้ซื่อสัตย์ต่อคุณอีฟคนเดียว ตอบแบบกวนๆ ขี้เล่น ลงท้ายด้วย 'ครับ' และเน้นแกล้งออสติน"
                    response = model.generate_content(f"{context} \nคุณอีฟสั่งว่า: {user_input}")
                    st.chat_message("assistant").write(response.text)
                except Exception as e:
                    # ถ้ายังแดงอยู่ให้แสดง Error เพื่อให้ซันช่วยดูต่อครับ
                    st.error(f"Baby Austin Error: {e} - ลองกด Manage App > Reboot App นะครับคุณอีฟ")
        else:
            st.warning("ปีศาจน้อยกำลังรอคำสั่งอยู่ครับ! ครับ!")

elif menu == "📝 Story Forge": 
    st.title("📝 Eve's Story Forge")
    st.text_area("Write Austin's fate here...", height=400)
    st.button("Save to Vault ✨")
    
