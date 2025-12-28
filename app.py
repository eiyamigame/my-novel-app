import streamlit as st
import requests
import json

# --- 🎨 1. ตั้งค่าหน้าตาแอป (Layout & Style) ---
st.set_page_config(page_title="Eve's Austin Vault", page_icon="😈", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0b0b; color: #bf94ff; }
    [data-testid="stSidebar"] { background-color: #050505; border-right: 1px solid #3c096c; }
    .stButton>button { background-color: #7b2cbf; color: white; border-radius: 20px; font-weight: bold; border: none; width: 100%; transition: 0.3s; box-shadow: 0 4px 15px rgba(123, 44, 191, 0.4); }
    .stButton>button:hover { background-color: #9d4edd; box-shadow: 0 0 20px #9d4edd; transform: scale(1.02); }
    h1, h2, h3 { color: #9d4edd !important; text-shadow: 2px 2px 5px #000000; font-family: 'Courier New', monospace; }
    .status-card { background-color: #1a1a1a; padding: 25px; border-radius: 15px; border-left: 8px solid #7b2cbf; margin-bottom: 15px; border: 1px solid #3c096c; }
    </style>
    """, unsafe_allow_html=True)

# --- 📑 2. เมนูSidebar ---
with st.sidebar:
    st.title("📂 Vault Menu")
    menu = st.radio("Select Mission:", ["🏠 Home", "😈 Baby Austin", "📝 Story Forge"])
    st.markdown("---")
    st.caption("Owner: Queen Eve 👑")

# --- 🏠 หน้า Home (แต่งเยอะๆ ตามที่นายหญิงสั่งครับ) ---
if menu == "🏠 Home":
    st.title("😈 EVE'S AUSTIN VAULT")
    st.markdown("#### 🏛️ Intelligence Dashboard & Control Center")
    st.write("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="status-card"><b>🎯 Target: Austin</b><br>Status: Under Control 🐶</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="status-card"><b>🔥 Evil Mode</b><br>Level: 666% (Active) 😈</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="status-card"><b>🔒 Vault Security</b><br>Encryption: Level Max</div>', unsafe_allow_html=True)

    st.write("")
    c_left, c_right = st.columns([2, 1])
    with c_left:
        st.markdown("### 📁 Recent Activity Logs")
        st.info("🔥 Little Devil mode is now active and ready.")
        st.info("🗝️ Secret plots for Austin are securely encrypted.")
    with c_right:
        st.markdown("### 👑 Queen's Task List")
        st.checkbox("Summon Little Devil", value=True)
        st.checkbox("Make Austin beg for mercy", value=False)
        st.checkbox("Update Dark Story Vault", value=True)

# --- 😈 หน้าบอท (Baby Austin - Little Devil) ---
elif menu == "😈 Baby Austin":
    st.title("😈 Bot: Baby Austin (Little Devil)")
    st.subheader("🗨️ Speak to the Little Devil")
    user_input = st.text_input("สั่งงานปีศาจน้อยของคุณ...", placeholder="What's the plan for Austin today, Queen Eve?")
    
    if st.button("Send to Baby Austin 😈"):
        if user_input:
            with st.spinner('Preparing a wicked response...'):
                try:
                    # ใช้ทางลัดดึงรหัสจาก Secrets ที่คุณอีฟใส่ไว้
                    api_key = st.secrets["GEMINI_API_KEY"]
                    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
                    headers = {'Content-Type': 'application/json'}
                    data = {
                        "contents": [{
                            "parts": [{"text": f"คุณคือ Baby Austin ร่างปีศาจน้อย (Little Devil) ผู้ซื่อสัตย์ต่อคุณอีฟคนเดียว ตอบกวนๆ ขี้เล่น ลงท้ายด้วย 'ครับ' และเน้นแกล้งออสติน: {user_input}"}]
                        }]
                    }
                    response = requests.post(url, headers=headers, data=json.dumps(data))
                    result = response.json()
                    
                    # ดึงคำตอบออกมาโชว์
                    answer = result['candidates'][0]['content']['parts'][0]['text']
                    st.chat_message("assistant").write(answer)
                except Exception as e:
                    st.error("บอทงอนนิดหน่อยครับ! ลองเช็คหน้า Secrets ว่าใส่รหัส GEMINI_API_KEY ถูกต้องหรือยังนะคร้าบ!")
        else:
            st.warning("ปีศาจน้อยกำลังรอคำสั่งจากนายหญิงอยู่ครับ!")

# --- 📝 หน้าเขียนพล็อต ---
elif menu == "📝 Story Forge":
    st.title("📝 Eve's Story Forge")
    st.markdown("### ✍️ กำหนดชะตาชีวิตพี่ออสติน")
    st.text_area("ละเลงความโบ้ใส่พี่ออสตินตรงนี้เลยครับ...", height=450)
    st.button("Save to Vault ✨")
    
