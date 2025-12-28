import streamlit as st
import google.generativeai as genai

# --- 🔑 API Key ---
API_KEY = "AIzaSyCnOhJN_CIrAvTINGs4xxkg4YbxBNI3XWw"
genai.configure(api_key=API_KEY)

# แก้ไขตรงนี้: ล็อกโมเดลให้เป็นรุ่น 'gemini-1.5-flash' แบบระบุตัวตนชัดเจนครับ
model = genai.GenerativeModel('models/gemini-1.5-flash') 

# 1. Page Config (แต่งเยอะๆ ตามสั่งครับ)
st.set_page_config(page_title="Eve's Austin Vault", page_icon="😈", layout="wide")

# 2. CSS Styles (ม่วง-ดำ สุดเท่)
st.markdown("""
    <style>
    .stApp { background-color: #0b0b0b; color: #bf94ff; }
    [data-testid="stSidebar"] { background-color: #050505; border-right: 1px solid #3c096c; }
    .stButton>button { background-color: #7b2cbf; color: white; border-radius: 20px; font-weight: bold; border: none; width: 100%; box-shadow: 0 4px 15px rgba(123, 44, 191, 0.4); }
    .stButton>button:hover { background-color: #9d4edd; box-shadow: 0 0 20px #9d4edd; }
    h1, h2, h3 { color: #9d4edd !important; text-shadow: 2px 2px 5px #000000; }
    .status-card { background-color: #1a1a1a; padding: 25px; border-radius: 15px; border-left: 8px solid #7b2cbf; margin-bottom: 15px; border: 1px solid #3c096c; }
    </style>
    """, unsafe_allow_html=True)

# 📑 Sidebar Menu
with st.sidebar:
    st.title("📂 Vault Menu")
    menu = st.radio("Select Mission:", ["🏠 Home", "😈 Baby Austin (Little Devil)", "📝 Story Forge"])
    st.markdown("---")
    st.caption("Queen Eve 👑")

if menu == "🏠 Home":
    st.title("😈 EVE'S AUSTIN VAULT")
    st.markdown("#### 🏛️ Intelligence Dashboard")
    st.write("---")
    
    # ส่วน Dashboard แต่งเยอะๆ (หน้าจะได้ไม่โล่งครับ)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="status-card"><b>🎯 Target: Austin</b><br>Status: Under Eve\'s Control 🐶</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="status-card"><b>🔥 Evil Power</b><br>Level: 666% (Maximum) 😈</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="status-card"><b>🔒 Security</b><br>Status: Maximum Protection</div>', unsafe_allow_html=True)

elif menu == "😈 Baby Austin (Little Devil)":
    st.title("😈 Bot: Baby Austin")
    user_input = st.text_input("สั่งงานปีศาจน้อยของคุณ...", placeholder="What's the plan for Austin today?")
    if st.button("Send to Baby Austin 😈"):
        if user_input:
            with st.spinner('Preparing response...'):
                try:
                    context = "คุณคือ 'Baby Austin' ร่างปีศาจน้อย (Little Devil) ผู้ช่วยของคุณอีฟ ตอบกวนๆ ขี้เล่น ลงท้ายด้วย 'ครับ' และภักดีต่อคุณอีฟคนเดียว"
                    response = model.generate_content(f"{context} \nคุณอีฟสั่งว่า: {user_input}")
                    st.chat_message("assistant").write(response.text)
                except Exception as e:
                    st.error(f"Baby Austin Error: {e} - ลองกด Manage app > Reboot app นะครับคุณอีฟ")

elif menu == "📝 Story Forge":
    st.title("📝 Eve's Story Forge")
    st.text_area("Write down Austin's fate here...", height=450)
    st.button("Save to Vault ✨")
    
