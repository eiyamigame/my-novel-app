import streamlit as st
import google.generativeai as genai

# --- 🔑 API Key ---
API_KEY = "AIzaSyCnOhJN_CIrAvTINGs4xxkg4YbxBNI3XWw"
genai.configure(api_key=API_KEY)

# แก้ปัญหา "Not Found" โดยใช้รุ่นมาตรฐานที่เสถียรที่สุดตอนนี้ครับ
model = genai.GenerativeModel('gemini-1.5-flash') 

# 1. Page Config (Wide Layout เพื่อให้แต่งได้เยอะครับ)
st.set_page_config(page_title="Eve's Austin Vault", page_icon="😈", layout="wide")

# 2. CSS Styles (ม่วง-ดำ สุดหรู)
st.markdown("""
    <style>
    .stApp { background-color: #0b0b0b; color: #bf94ff; }
    [data-testid="stSidebar"] { background-color: #050505; border-right: 1px solid #3c096c; }
    .stButton>button { background-color: #7b2cbf; color: white; border-radius: 20px; font-weight: bold; border: none; width: 100%; transition: 0.3s; box-shadow: 0 4px 15px rgba(123, 44, 191, 0.4); }
    .stButton>button:hover { background-color: #9d4edd; box-shadow: 0 0 20px #9d4edd; transform: scale(1.02); }
    h1, h2, h3 { color: #9d4edd !important; text-shadow: 2px 2px 5px #000000; font-family: 'Courier New', monospace; }
    .status-card { background-color: #1a1a1a; padding: 25px; border-radius: 15px; border: 1px solid #3c096c; border-left: 8px solid #7b2cbf; margin-bottom: 15px; }
    .info-text { font-size: 1.1rem; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

# 📑 Sidebar Menu
with st.sidebar:
    st.title("📂 Vault Menu")
    menu = st.radio("Select Mission:", ["🏠 Home", "😈 Baby Austin", "📝 Story Forge"])
    st.markdown("---")
    st.markdown("### 👑 Master of the Vault\n**Queen Eve**")

if menu == "🏠 Home":
    st.title("😈 EVE'S AUSTIN VAULT")
    st.markdown("#### 🏛️ Intelligence Dashboard & Control Center")
    st.write("---")

    # --- ส่วนแต่งเยอะๆ (Dashboard Cards) ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="status-card"><b>🎯 Target: Austin</b><br>Status: Under Eve\'s Command 🐶</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="status-card"><b>🔥 Evil Mode</b><br>Level: 666% (Maximum) 😈</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="status-card"><b>🔒 Vault Security</b><br>Encryption: Triple Layered</div>', unsafe_allow_html=True)

    st.write("")
    
    # --- ข้อมูลรายงานสถานะ ---
    c_left, c_right = st.columns([2, 1])
    with c_left:
        st.markdown("### 📁 Intelligence Logs")
        st.info("🔥 **Little Devil:** Baby Austin is ready to serve and prank.")
        st.info("🗝️ **Vault Status:** All secret plot files are encrypted and safe.")
        st.info("⚡ **AI Connection:** Connected to Gemini Neural Link.")
    
    with c_right:
        st.markdown("### 👑 Queen's Checklist")
        st.checkbox("Summon the Little Devil", value=True)
        st.checkbox("Make Austin beg for mercy", value=False)
        st.checkbox("Write a spicy new chapter", value=False)
        st.checkbox("Update Vault security", value=True)

    st.markdown("---")
    st.markdown("<center><i>'In this vault, Queen Eve rules. Austin is just a puppet.'</i></center>", unsafe_allow_html=True)

elif menu == "😈 Baby Austin": 
    st.title("😈 Bot: Baby Austin (Little Devil)")
    st.subheader("🗨️ Speak to the Little Devil")
    user_input = st.text_input("สั่งงานปีศาจน้อยของคุณ...", placeholder="What should we do with Austin today, Queen Eve?")
    
    if st.button("Send to Baby Austin 😈"):
        if user_input:
            with st.spinner('Baby Austin is crafting a wicked response...'):
                try:
                    # ปรับจูนให้เป็นปีศาจกวนๆ และคุยไทยเหมือนเดิมครับ
                    context = "คุณคือ 'Baby Austin' (Little Devil) ผู้ช่วยปีศาจน้อยของคุณอีฟ ตอบกวนๆ ขี้เล่น และภักดีต่อคุณอีฟคนเดียว ลงท้ายด้วย 'ครับ' เสมอ"
                    response = model.generate_content(f"{context} \nคุณอีฟสั่งว่า: {user_input}")
                    st.chat_message("assistant").write(response.text)
                except Exception as e:
                    st.error(f"Error: {e} - ลองกด Manage app > Reboot app นะครับคุณอีฟ")
        else:
            st.warning("ปีศาจน้อยกำลังรอคำสั่งจากนายหญิงอยู่ครับ!")

elif menu == "📝 Story Forge": 
    st.title("📝 Eve's Story Forge")
    st.markdown("### ✍️ เขียนโชคชะตาของพี่ออสติน")
    st.text_area("ละเลงความโบ้ตรงนี้เลยครับ...", height=450)
    st.button("Save to Secret Vault ✨")
    
