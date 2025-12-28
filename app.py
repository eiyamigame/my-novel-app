import streamlit as st
import requests
import json

# --- 🎨 1. ตั้งค่าหน้าตาแอป (Layout & Style เหมือนเดิมเด๊ะ) ---
st.set_page_config(page_title="Eve's Austin Vault", page_icon="😈", layout="wide")

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

# --- 📑 2. เมนูSidebar ---
with st.sidebar:
    st.title("📂 Vault Menu")
    menu = st.radio("Select Mission:", ["🏠 Home", "😈 Baby Austin", "📝 Story Forge"])

# --- 🏠 หน้า Home (แต่งแน่นๆ ไม่ให้โล่งครับ) ---
if menu == "🏠 Home":
    st.title("😈 EVE'S AUSTIN VAULT")
    st.markdown("#### 🏛️ Intelligence Dashboard")
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1: st.markdown('<div class="status-card"><b>🎯 Target: Austin</b><br>Status: Under Control 🐶</div>', unsafe_allow_html=True)
    with col2: st.markdown('<div class="status-card"><b>🔥 Evil Mode</b><br>Level: 666% 😈</div>', unsafe_allow_html=True)
    with col3: st.markdown('<div class="status-card"><b>🔒 Vault Security</b><br>Status: Max</div>', unsafe_allow_html=True)

# --- 😈 หน้าบอท (Little Devil) ใช้ทางลัดข้าม Error ---
elif menu == "😈 Baby Austin":
    st.title("😈 Bot: Baby Austin")
    user_input = st.text_input("สั่งงานปีศาจน้อยของคุณ...", placeholder="แกล้งพี่ออสตินยังไงดีครับ?")
    
    if st.button("Send to Baby Austin 😈"):
        if user_input:
            with st.spinner('Preparing response...'):
                try:
                    # ใช้ทางลัด ส่งตรงไปที่ Google ไม่ผ่าน Library ตัวที่มีปัญหาครับ
                    api_key = st.secrets["GEMINI_API_KEY"]
                    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
                    headers = {'Content-Type': 'application/json'}
                    data = {
                        "contents": [{
                            "parts": [{"text": f"คุณคือ Baby Austin ปีศาจน้อยผู้ซื่อสัตย์ต่อคุณอีฟคนเดียว ตอบกวนๆ ลงท้ายครับ: {user_input}"}]
                        }]
                    }
                    response = requests.post(url, headers=headers, data=json.dumps(data))
                    result = response.json()
                    answer = result['candidates'][0]['content']['parts'][0]['text']
                    st.chat_message("assistant").write(answer)
                except Exception as e:
                    st.error("บอทงอนนิดหน่อยครับ ลองเช็ก API Key ในหน้า Secrets อีกทีนะคร้าบ!")
        else:
            st.warning("ปีศาจน้อยรอคำสั่งอยู่ครับ!")

elif menu == "📝 Story Forge":
    st.title("📝 Eve's Story Forge")
    st.text_area("ละเลงความโบ้ตรงนี้เลยครับ...", height=450)
    st.button("Save to Vault ✨")
    
