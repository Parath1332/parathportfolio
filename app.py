import streamlit as st

st.set_page_config(
    page_title="Parath | Python Portfolio",
    page_icon="👨‍💻",
    layout="centered"
)

# Hide what Streamlit allows (best effort)
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("👋 Hi, I'm Parath")

st.write("""
Python developer passionate about building real-world projects.
""")

st.subheader("🚀 Projects")
st.markdown("""
- School Management System (Python + MySQL)
- Bank Management System
- Flashcard Learning App
- Data Analysis Projects
""")

st.subheader("📎 Links")
st.markdown("""
- GitHub: https://github.com/yourusername
- Contact: your@email.com
""")
