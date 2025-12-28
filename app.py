import streamlit as st
import google.generativeai as genai
from google.generativeai.types import RequestOptions

# --- 🔑 1. เชื่อมต่อรหัสลับ (แบบบังคับ v1) ---
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # ซันแก้ตรงนี้ครับ: บังคับให้คุยผ่าน v1 ไม่ให้มันไปหา v1beta เองครับ
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        # สั่งให้ใช้ API v1 เท่านั้นครับ
        request_options=RequestOptions(api_version='v1')
    )
else:
    st.error("หา API Key ไม่เจอครับคุณอีฟ!")

# --- 🎨 2. ตั้งค่าหน้าตาแอป (Layout & Style ตามสั่งครับ) ---
st.set_page_config(page_title="Eve's Austin Vault", page_icon="😈", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0b0b; color: #bf94ff; }
    [data-testid="stSidebar"] { background-color: #050505; border-right: 1px solid #3c096c; }
    .stButton>button { background-color: #7b2cbf; color: white; border-radius: 20px; font-weight: bold; border: none; width: 100%; }
    .stButton>button:hover { background-color: #9d4edd; box-shadow: 0 0 20px #9d4edd; }
    h1, h2, h3 { color: #9d4edd !important; text-shadow: 2px 2px 5px #000000; }
    .status-card { background-color: #1a1a1a; padding: 25px; border-radius: 15px; border-left: 8px solid #7b2cbf; margin-bottom: 15px; border: 1px solid #3c096c; }
    </style>
    """, unsafe_allow_html=True)

# --- 📑 3. เมนูคำสั่ง (Sidebar) ---
with st.sidebar:
    st.title("📂 Vault Menu")
    menu = st.radio("Select Mission:", ["🏠 Home", "😈 Baby Austin", "📝 Story Forge"])
    st.caption("Owner: Queen Eve 👑")

if menu == "🏠 Home":
    st.title("😈 EVE'S AUSTIN VAULT")
    st.markdown("#### 🏛️ Intelligence Dashboard")
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="status-card"><b>🎯 Target: Austin</b><br>Status: Under Control 🐶</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="status-card"><b>🔥 Evil Mode</b><br>Level: 666% 😈</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="status-card"><b>🔒 Vault Security</b><br>Status: Maximum</div>', unsafe_allow_html=True)

elif menu == "😈 Baby Austin":
    st.title("😈 Bot: Baby Austin")
    user_input = st.text_input("สั่งงานปีศาจน้อยของคุณ...", placeholder="แกล้งพี่ออสตินยังไงดีครับ?")
    if st.button("Send to Baby Austin 😈"):
        if user_input:
            with st.spinner('Preparing response...'):
                try:
                    # ปรับจูนบุคลิกปีศาจน้อย
                    context = "คุณคือ 'Baby Austin' (Little Devil) ผู้ช่วยของคุณอีฟ ตอบกวนๆ ลงท้ายครับ และเน้นแกล้งออสติน"
                    response = model.generate_content(f"{context} \nคุณอีฟสั่งว่า: {user_input}")
                    st.chat_message("assistant").write(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")

elif menu == "📝 Story Forge":
    st.title("📝 Eve's Story Forge")
    st.text_area("ละเลงความโบ้ตรงนี้เลยครับ...", height=450)
    st.button("Save to Vault ✨")
    
