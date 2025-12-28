import streamlit as st
import google.generativeai as genai

# --- 🔑 ใช้รหัสที่คุณอีฟทดสอบผ่านแล้ว ---
API_KEY = "AIzaSyCnOhJN_CIrAvTINGs4xxkg4YbxBNI3XWw"
genai.configure(api_key=API_KEY)

# ตั้งค่าโมเดลแบบเจาะจงเพื่อเลี่ยง Error 404
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# 1. Page Config (Wide Layout แต่งให้แน่นๆ ครับ)
st.set_page_config(page_title="Eve's Austin Vault", page_icon="😈", layout="wide")

# 2. CSS Styles (ม่วง-ดำ และ Dashboard สวยๆ)
st.markdown("""
    <style>
    .stApp { background-color: #0b0b0b; color: #bf94ff; }
    [data-testid="stSidebar"] { background-color: #050505; border-right: 1px solid #3c096c; }
    .stButton>button { background-color: #7b2cbf; color: white; border-radius: 20px; font-weight: bold; border: none; width: 100%; box-shadow: 0 4px 15px rgba(123, 44, 191, 0.4); }
    .stButton>button:hover { background-color: #9d4edd; box-shadow: 0 0 20px #9d4edd; }
    .status-card { background-color: #1a1a1a; padding: 25px; border-radius: 15px; border-left: 8px solid #7b2cbf; margin-bottom: 15px; border: 1px solid #3c096c; }
    h1, h2, h3 { color: #9d4edd !important; text-shadow: 2px 2px 5px #000000; }
    </style>
    """, unsafe_allow_html=True)

# 📑 Sidebar Menu
with st.sidebar:
    st.title("📂 Vault Menu")
    menu = st.radio("Select Mission:", ["🏠 Home", "😈 Baby Austin", "📝 Story Forge"])
    st.markdown("---")
    st.caption("Master: Queen Eve 👑")

if menu == "🏠 Home":
    st.title("😈 EVE'S AUSTIN VAULT")
    st.markdown("#### 🏛️ Intelligence Dashboard")
    st.write("---")

    # --- ส่วนแต่งเยอะๆ ตามสั่ง ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="status-card"><b>🎯 Target: Austin</b><br>Status: Under Control 🐶</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="status-card"><b>🔥 Little Devil Mode</b><br>Level: 666% (Active) 😈</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="status-card"><b>🔒 Vault Security</b><br>Status: Maximum Privacy</div>', unsafe_allow_html=True)

    st.write("")
    c_left, c_right = st.columns([2, 1])
    with c_left:
        st.markdown("### 📁 Recent Activity")
        st.info("🔥 **Baby Austin** is now a Little Devil.")
        st.info("🗝️ **Secret Vault** is fully encrypted.")
    with c_right:
        st.markdown("### 👑 Queen's Tasks")
        st.checkbox("Bully Austin", value=True)
        st.checkbox("Write Spicy Plot", value=False)

elif menu == "😈 Baby Austin":
    st.title("😈 Bot: Baby Austin (Little Devil)")
    st.subheader("🗨️ Speak to the Little Devil")
    user_input = st.text_input("สั่งงานปีศาจน้อยของคุณ...", placeholder="What's the plan, Queen Eve?")
    
    if st.button("Send to Baby Austin 😈"):
        if user_input:
            with st.spinner('Preparing response...'):
                try:
                    context = "คุณคือ 'Baby Austin' (Little Devil) ผู้ช่วยปีศาจน้อยของคุณอีฟ ตอบกวนๆ ขี้เล่น ลงท้ายด้วย 'ครับ' และภักดีต่อคุณอีฟคนเดียว"
                    response = model.generate_content(f"{context} \nคุณอีฟสั่งว่า: {user_input}")
                    st.chat_message("assistant").write(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
                    
