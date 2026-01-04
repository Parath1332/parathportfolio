import streamlit as st

st.set_page_config(
    page_title="Parath | Portfolio",
    page_icon="👨‍💻",
    layout="centered"
)

# Hide Streamlit UI (best possible)
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------- PORTFOLIO CONTENT ----------
st.title("👋 Hi, I'm Parath")

st.subheader("Python Developer | Student | Projects")

st.write("""
Welcome to my portfolio website.

I build Python projects using:
- Streamlit
- Tkinter
- MySQL
- Flask
""")

st.markdown("---")

st.subheader("🚀 Projects")

st.markdown("""
- 🏫 **School Management System**  
- 🏦 **Bank Management System**  
- 🧠 **Flashcard Learning App**  
- 📊 **Python Data Projects**
""")

st.markdown("---")

st.subheader("📬 Contact")

st.write("📧 Email: parath101112@gmail.com")  
st.write("🐙 GitHub: https://github.com/Parath1332")
