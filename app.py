import streamlit as st

st.set_page_config(page_title="Python Portfolio", page_icon="🐍", layout="centered")

st.title("👨‍💻 Parath S")
st.subheader("Python Developer | Student")
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.write("""
I build Python projects using **Tkinter, MySQL, and Flask**.
This portfolio showcases my live Python projects.
""")

st.divider()

st.header("📂 Projects")

with st.expander("🎮 Tic Tac Toe Game"):
    st.write("A simple Python game")
    st.button("Run Game")

with st.expander("🏦 Bank Management System"):
    st.write("Account creation, deposit, withdraw, transfer")
    st.button("View Project")

with st.expander("🔐 Login System"):
    st.write("Login, register, forgot password using MySQL")
    st.button("View Demo")

st.divider()

st.header("📄 Resume")
st.write("Coming soon")

st.divider()

st.header("📞 Contact")
st.write("Email: yourmail@gmail.com")
st.write("GitHub: https://github.com/yourusername")

