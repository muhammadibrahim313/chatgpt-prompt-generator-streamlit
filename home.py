import streamlit as st

# Title and Sidebar
st.title("🤖 ChatGPT Prompt Generator 📝")
st.sidebar.title("Select Prompt Type 🎯")

# About Me Section
st.sidebar.header("About the Developer 👨‍💻")
st.sidebar.markdown("👨‍💻 I am a dedicated data analyst with a passion for developing web applications and exploring innovative projects.")
st.sidebar.header("Connect with Me 🔗")
st.sidebar.markdown("[![LinkedIn](https://img.icons8.com/color/48/000000/linkedin.png)](https://www.linkedin.com/in/muhammad-ibrahim-qasmi-9876a1297/) [![GitHub](https://img.icons8.com/ios-filled/50/000000/github.png)](https://github.com/muhammadibrahim313) [![Kaggle](https://img.icons8.com/color/48/000000/kaggle.png)](https://www.kaggle.com/muhammadibrahimqasmi)")

# App Description
st.subheader("Welcome to ChatGPT Prompt Generator 🚀")
st.markdown(
        """
        <hr style="border: 1px solid white;">
        <p style="font-size: 12px; color: gray; text-align: center;">
        Developed with ❤️ by [MUHAMMAD IBRAHIM ]
        </p>
        """,
        unsafe_allow_html=True
    )
# Prompt Generators
st.markdown("### Choose Your Inspiration:")
st.markdown("- Coding Project: Let's ignite your coding creativity! 💻")
st.markdown("- Travel Guide: Plan your adventures with ease. ✈️")

# Description
st.write("This application empowers you to generate prompts using ChatGPT tailored for specific use cases.")
st.write("Select a prompt generator from the sidebar to get started. 🚀")
