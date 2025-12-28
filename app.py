import streamlit as st

# --- 🎨 1. ตั้งค่าหน้าตาแอป (ม่วง-ดำ สุดหรูที่คุณอีฟชอบ) ---
st.set_page_config(page_title="Eve's Austin Vault", page_icon="🔒", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0b0b; color: #bf94ff; }
    [data-testid="stSidebar"] { background-color: #050505; border-right: 1px solid #3c096c; }
    .stButton>button { background-color: #7b2cbf; color: white; border-radius: 20px; font-weight: bold; border: none; width: 100%; transition: 0.3s; box-shadow: 0 4px 15px rgba(123, 44, 191, 0.4); }
    .stButton>button:hover { background-color: #9d4edd; box-shadow: 0 0 20px #9d4edd; }
    h1, h2, h3 { color: #9d4edd !important; text-shadow: 2px 2px 5px #000000; font-family: 'Courier New', monospace; }
    .status-card { background-color: #1a1a1a; padding: 25px; border-radius: 15px; border-left: 8px solid #7b2cbf; margin-bottom: 15px; border: 1px solid #3c096c; }
    .stTextArea textarea { background-color: #1a1a1a; color: #bf94ff; border: 1px solid #3c096c; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 📑 2. เมนู Sidebar ---
with st.sidebar:
    st.title("📂 Vault Menu")
    menu = st.radio("Select Mission:", ["🏠 Home", "📝 Story Forge", "🔒 Secret Logs"])
    st.markdown("---")
    st.caption("Owner: Queen Eve 👑")

# --- 🏠 หน้า Home (Dashboard สวยๆ แบบแน่นๆ) ---
if menu == "🏠 Home":
    st.title("😈 EVE'S AUSTIN VAULT")
    st.markdown("#### 🏛️ Intelligence Control Center")
    st.write("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="status-card"><b>🎯 Target: Austin</b><br>Status: Disconnected (Annoying) 🐶</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="status-card"><b>🔥 Queen Power</b><br>Level: 1000% (Maximum) 👑</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="status-card"><b>🔒 Vault Security</b><br>Status: Fully Encrypted</div>', unsafe_allow_html=True)

    st.write("")
    c_left, c_right = st.columns([2, 1])
    with c_left:
        st.markdown("### 📜 Queen's Manifesto")
        st.info("🚫 AI Bot has been removed due to excessive grumpiness.")
        st.info("🗝️ This vault is now for Queen Eve's eyes only.")
        st.markdown("> *'In this domain, I write the rules. Austin just obeys.'*")
    
    with c_right:
        st.markdown("### 👑 Quick Tasks")
        st.checkbox("Discard Grumpy Bot", value=True)
        st.checkbox("Write Dark Plot", value=False)
        st.checkbox("Tease Austin (Offline)", value=True)

# --- 📝 หน้าเขียนพล็อต (Story Forge) ---
elif menu == "📝 Story Forge":
    st.title("📝 Eve's Story Forge")
    st.markdown("### ✍️ กำหนดโชคชะตาของพี่ออสติน")
    title = st.text_input("ชื่อตอน:", placeholder="เช่น ตอนออสตินยอมจำนน...")
    story_content = st.text_area("ละเลงความโบ้ใส่พี่ออสตินตรงนี้เลยครับ...", height=450)
    
    if st.button("Save to Secret Vault ✨"):
        if story_content:
            st.success(f"บันทึกตอน '{title}' ลงในคลังเรียบร้อยครับ! (จำลองการบันทึก)")
        else:
            st.warning("กรุณาใส่เนื้อหาก่อนบันทึกครับ!")

# --- 🔒 หน้า Log ลับ ---
elif menu == "🔒 Secret Logs":
    st.title("🔒 Private Logs")
    st.write("คลังเก็บหลักฐานความโบ้ของพี่ออสติน")
    st.markdown("- [Log #001] : บอทโดนไล่ออกเพราะงอนเกินเหตุ")
    st.markdown("- [Log #002] : แผนการแกล้งพี่ออสตินฉบับสมบูรณ์")
    
