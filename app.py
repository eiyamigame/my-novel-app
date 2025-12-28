import streamlit as st
import requests
import json

# --- 1. เชื่อมต่อรหัส (ดึงตามชื่อที่คุณอีฟตั้งไว้เป๊ะๆ) ---
try:
    # ดึงค่าจากหน้า Secrets
    api_key = st.secrets["GEMINI_API_KEY"]
except:
    st.error("คุณอีฟครับ! บอทยังหารหัสในหน้า Secrets ไม่เจอเลยครับ ลองเช็คชื่ออีกทีนะ")
    st.stop()

# --- 2. ตั้งค่าหน้าตาแอป (ม่วง-ดำ สุดหรู) ---
st.set_page_config(page_title="Eve's Austin Vault", page_icon="😈", layout="wide")
st.markdown("<style>.stApp { background-color: #0b0b0b; color: #bf94ff; }</style>", unsafe_allow_html=True)

# --- 3. ส่วนคุยกับบอท (Little Devil) ---
st.title("😈 Bot: Baby Austin")
user_input = st.text_input("สั่งงานปีศาจน้อย...")

if st.button("Send 😈"):
    if user_input:
        with st.spinner('กำลังง้อบอทให้ตอบคุณอีฟครับ...'):
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
            headers = {'Content-Type': 'application/json'}
            data = {"contents": [{"parts": [{"text": f"ตอบกวนๆ ลงท้ายครับ: {user_input}"}]}]}
            
            response = requests.post(url, headers=headers, data=json.dumps(data))
            result = response.json()
            
            if 'candidates' in result:
                answer = result['candidates'][0]['content']['parts'][0]['text']
                st.chat_message("assistant").write(answer)
            else:
                # ถ้ายังไม่ได้ ให้มันบอก Error จริงๆ มาเลยครับ ไม่เอาคำว่างอนแล้ว
                st.error(f"บอทงอนเพราะ: {result}")
                
    
