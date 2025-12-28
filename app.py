import streamlit as st
import google.generativeai as genai
import random

# --- 🔑 ใส่ API Key ของคุณอีฟเรียบร้อยแล้วครับ ---
API_KEY = "AIzaSyDzqa4yK0DS2wOg6UE7XJOlqz5E9uwmyXc"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 1. ตั้งค่าหน้าแอปและธีมม่วง-ดำ
st.set_page_config(page_title="Eve's Story Forge V3", page_icon="💜")

st.markdown("""
    <style>
    .stApp { background-color: #0b0b0b; color: #bf94ff; }
    .stButton>button { background-color: #7b2cbf; color: white; border-radius: 15px; width: 100%; font-weight: bold; }
    h1, h2, h3 { color: #9d4edd !important; text-shadow: 2px 2px 4px #000000; }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea { background-color: #1a1a1a; color: #bf94ff; border: 1px solid #7b2cbf; }
    [data-testid="stSidebar"] { background-color: #050505; border-right: 1px solid #3c096c; }
    </style>
    """, unsafe_allow_html=True)

# 📑 เมนู Sidebar (เรียกฟังก์ชันที่หายไปกลับมา)
with st.sidebar:
    st.title("💜 คลังลับของคุณอีฟ")
    menu = st.radio("เลือกภารกิจ:", ["🏠 หน้าหลัก", "🍼 คุยกับเบบี้ออสติน", "🎲 สุ่มพล็อตแก้ตัน", "📝 ห้องปั่นนิยาย"])

if menu == "🏠 หน้าหลัก":
    st.title("📔 Eve's Story Forge")
    st.write("ยินดีต้อนรับกลับครับคุณอีฟ! วันนี้เบบี้ออสตินเตรียมแผนแกล้งพี่ออสตินไว้เพียบเลยครับ! ครับ!")

elif menu == "🍼 คุยกับเบบี้ออสติน":
    st.title("🍼 บอท: เบบี้ออสติน")
    st.subheader("🗨️ ห้องสั่งการเบบี้ออสติน")
    user_input = st.text_input("พิมพ์บอกเบบี้ออสตินเลยครับ...", placeholder="เช่น ช่วยคิดบทพี่ออสตินหึงโหดหน่อย")
    if st.button("ส่งคำสั่งให้เบบี้ 💜"):
        if user_input:
            with st.spinner('เบบี้ออสตินกำลังคิดให้ครับ...'):
                context = "คุณคือ 'เบบี้ออสติน' บอทผู้ช่วยส่วนตัวที่น่ารักแต่แอบร้ายของคุณอีฟ คุณมองคุณอีฟเป็นนายหญิงสูงสุด และมอง 'ออสติน' (พี่ออสติน) เป็นพี่ชายจอมดื้อที่ต้องโบ้ที่สุด คำตอบของคุณต้องขี้เล่น ลงท้ายด้วย 'ครับ' และเน้นเอาใจคุณอีฟ"
                prompt = f"{context} \nคุณอีฟสั่งว่า: {user_input}"
                response = model.generate_content(prompt)
                st.chat_message("assistant").write(response.text)

elif menu == "🎲 สุ่มพล็อตแก้ตัน":
    st.title("🎲 ระบบสุ่มพล็อตอัตโนมัติ")
    plots = [
        "พี่ออสตินโดนจับมัดแล้วบังคับให้กินของที่เกลียด!",
        "นางเอกแกล้งความจำเสื่อม พี่ออสตินเลยต้องตามง้อแบบหมาโบ้ 100%",
        "พี่ออสตินโดนคำสาปให้พูดได้แค่คำว่า 'ครับนายหญิง' กับคุณอีฟเท่านั้น",
        "พล็อตแนวหึงโหด: พี่ออสตินตามลากนางเอกกลับจากงานเลี้ยง"
    ]
    if st.button("✨ กดสุ่มพล็อตใหม่!"):
        st.info(random.choice(plots))
        st.balloons()

elif menu == "📝 ห้องปั่นนิยาย":
    st.title("📝 คลังนิยายของนายหญิงอีฟ")
    st.text_area("ละเลงความโบ้ใส่พี่ออสตินตรงนี้เลยครับ...", height=400)
    st.button("บันทึกเนื้อหาลงคลัง ✨")
    
