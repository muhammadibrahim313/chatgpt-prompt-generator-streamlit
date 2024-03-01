import streamlit as st

st.set_page_config(page_title="Travel Guide Prompt Generator", page_icon=":airplane:", layout="centered")

# Header
st.title("✈️ Travel Guide Prompt Generator")
st.markdown("---")

# Sidebar
st.sidebar.success("✅ Select Prompt Options")
st.sidebar.subheader("🛠 Customize Your Prompt")

# Get user inputs
destination = st.text_input("🌍 Enter your destination")
day_count = st.slider("📅 Days at Destination", min_value=0, max_value=60, step=1)
activities = st.multiselect("🎉 Choose Activities", ["Visit Museums", "Spend Time in Nature", "Sightseeing", "Hiking", "Shopping", "Dining"])

# Generate prompt button
submitted = st.button("🚀 Generate Prompt")

# Prompt Builder Class
class PromptBuilder:
    def __init__(self, destination: str, day_count: int, activities: list):
        self.destination = destination
        self.day_count = day_count
        self.activities = activities

    def build_prompt(self):
        activity_prompt = ", ".join(self.activities)
        prompt = f"I want you to act as my travel guide. My destination is {self.destination}. I will spend {self.day_count} days at the destination. Please suggest me things to do such as {activity_prompt}. Please compile a complete plan for my holidays in {self.destination}. Give me a list with a different idea for each day."

        return prompt

# Main content
if submitted:
    with st.spinner("Generating Prompt..."):
        prompt_builder = PromptBuilder(destination, day_count, activities)
        prompt = prompt_builder.build_prompt()

        st.markdown("---")
        st.subheader("Generated Prompt:")
        st.code(prompt)

# Footer
st.markdown("---")
st.write("Made with :heart: by Muhammad Ibrahim", unsafe_allow_html=True)
