import streamlit as st
import requests
import json

# --- 1. เชื่อมต่อรหัส (ดึงตามที่คุณอีฟเป๊ะมากในหน้า Secrets) ---
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except:
    st.error("บอทหารหัสไม่เจอครับคุณอีฟ! ลองเช็คชื่อใน Secrets นะคร้าบ")
    st.stop()

# --- 2. ตั้งค่าหน้าตาแอป (ม่วง-ดำ สุดหรู) ---
st.set_page_config(page_title="Eve's Austin Vault", page_icon="😈", layout="wide")
st.markdown("<style>.stApp { background-color: #0b0b0b; color: #bf94ff; }</style>", unsafe_allow_html=True)

st.title("😈 Bot: Baby Austin")
user_input = st.text_input("สั่งงานปีศาจน้อย...")

if st.button("Send 😈"):
    if user_input:
        with st.spinner('กำลังใช้พลังปีศาจง้อบอทครับ...'):
            # แก้ตรงนี้ครับ! ซันเปลี่ยนชื่อรุ่นเป็นชื่อเต็มเพื่อให้ v1beta รู้จักครับ
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
            headers = {'Content-Type': 'application/json'}
            data = {"contents": [{"parts": [{"text": f"ตอบกวนๆ ลงท้ายครับ: {user_input}"}]}]}
            
            response = requests.post(url, headers=headers, data=json.dumps(data))
            result = response.json()
            
            if 'candidates' in result:
                answer = result['candidates'][0]['content']['parts'][0]['text']
                st.chat_message("assistant").write(answer)
            else:
                st.error(f"บอทงอนเพราะ: {result}")
                
    
