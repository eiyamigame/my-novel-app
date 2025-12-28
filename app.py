import streamlit as st
import google.generativeai as genai
import random

# --- 🔑 API Key (ชุดที่ทดสอบผ่านแล้ว) ---
API_KEY = "AIzaSyCnOhJN_CIrAvTINGs4xxkg4YbxBNI3XWw"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash') 

# 1. Page Config
st.set_page_config(page_title="Eve's Austin Vault", page_icon="😈", layout="wide")

# 2. CSS Styles (จัดเต็มความม่วง-ดำ และบัดเจทบอร์ด)
st.markdown("""
    <style>
    .stApp { background-color: #0b0b0b; color: #bf94ff; }
    [data-testid="stSidebar"] { background-color: #050505; border-right: 1px solid #3c096c; }
    .stButton>button { background-color: #7b2cbf; color: white; border-radius: 20px; font-weight: bold; border: none; width: 100%; transition: 0.3s; }
    .stButton>button:hover { background-color: #9d4edd; box-shadow: 0 0 15px #9d4edd; }
    h1, h2, h3 { color: #9d4edd !important; text-shadow: 2px 2px 5px #000000; }
    .status-card { background-color: #1a1a1a; padding: 20px; border-radius: 15px; border-left: 5px solid #7b2cbf; margin-bottom: 10px; }
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
    st.markdown("### 🏛️ Central Command & Intelligence Center")
    st.write("---")

    # --- แถวที่ 1: Dashboard (หน้าไม่โล่งแน่นอนครับ) ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="status-card"><b>🎯 Target: Austin</b><br>Status: 🐶 Bo-Mode Activated</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="status-card"><b>🔥 Evil Energy</b><br>Level: 666% Overloaded</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="status-card"><b>🔒 Security</b><br>Status: Maximum Protection</div>', unsafe_allow_html=True)

    st.write("")
    
    # --- แถวที่ 2: Activity Log ---
    col_left, col_right = st.columns([2, 1])
    with col_left:
        st.markdown("### 📁 Recent Intelligence")
        st.info("🔥 Baby Austin is now in 'Little Devil' mode.")
        st.info("📖 Secret vault contains all Austin's weaknesses.")
        st.info("🎲 Plot Generator is ready for bullying sessions.")
    
    with col_right:
        st.markdown("### 👑 Eve's Checklist")
        st.checkbox("Summon Little Devil", value=True)
        st.checkbox("Make Austin beg", value=False)
        st.checkbox("Expand the Empire", value=False)

elif menu == "😈 Baby Austin": 
    st.title("😈 Bot: Baby Austin (Little Devil)")
    st.subheader("🗨️ Speak to the Little Devil")
    user_input = st.text_input("สั่งงานปีศาจน้อยของคุณได้เลยครับ...", placeholder="Talk to your assistant...")
    
    if st.button("Send to Baby Austin 😈"):
        if user_input:
            with st.spinner('Baby Austin is weaving a dark response...'):
                try:
                    # --- 🧠 ปรับ AI ให้ตอบแบบปีศาจกวนๆ และคุยไทยตามเดิมครับ ---
                    context = (
                        "คุณคือ 'Baby Austin' ในร่างปีศาจตัวน้อย (Little Devil) ผู้ซื่อสัตย์ต่อคุณอีฟคนเดียว "
                        "นิสัยกวนประสาท ขี้เล่น แต่ออกแนวร้ายกาจเมื่อพูดถึงออสติน "
                        "จงตอบเป็นภาษาไทยแบบฉลาดๆ กวนๆ ลงท้ายด้วย 'ครับ' เสมอ "
                        "เน้นประจบคุณอีฟและหาทางแกล้งออสตินให้เป็นหมาโบ้ที่สุด"
                    )
                    response = model.generate_content(f"{context} \nคุณอีฟสั่งว่า: {user_input}")
                    st.chat_message("assistant").write(response.text)
                except Exception as e:
                    st.error(f"Baby Austin Error: {e}")
        else:
            st.warning("ปีศาจน้อยกำลังรอคำสั่งอยู่ครับ! ครับ!")

elif menu == "📝 Story Forge": 
    st.title("📝 Eve's Story Forge")
    st.text_area("Write Austin's destiny here...", height=400)
    st.button("Save to Vault ✨")
    
