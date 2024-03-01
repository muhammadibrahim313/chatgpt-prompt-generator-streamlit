import streamlit as st

st.set_page_config(page_title="Coding Project Prompt Generator", page_icon=":computer:", layout="centered")

# Header
st.title("💻 Coding Project Prompt Generator 💡")
st.markdown("---")

# Get user inputs
usecase_options = ["school", "college", "portfolio", "work", "fun"]
language_options = ["Python", "JavaScript", "Java", "C", "Lua", "Ruby", "C++", "C#", "Visual Basic", "Pascal", "HTML", "CSS"]
topics_options = ["Loops", "If/Else", "Object Oriented Programming", "Input/Output (Text Based)", "Functions", "Reading/Writing Files", "Language Specific Magic", "Strings", "Integers", "Floats", "Arrays", "Binary Trees", "Search Trees"]

usecase = st.selectbox("📚 REQUIRED: Select what the project is for", options=usecase_options)
language = st.selectbox("💻 REQUIRED: Select the programming language", options=language_options)
language2 = st.text_input("💡 OPTIONAL: Insert alternative programming language/technology here, leave empty if a language was selected")
include = st.multiselect("🔍 OPTIONAL: Select topics that should be included in the project", options=topics_options)
exclude = st.multiselect("🚫 OPTIONAL: Select topics that should be excluded in the project", options=topics_options)
lines = st.slider("📝 OPTIONAL: Project Size (Lines of Code)", 0, 1000, (50, 100))

# Generate prompt button
submitted = st.button("🚀 Generate Prompt")

# Sidebar
st.sidebar.success("✅ Select Prompt Options")
st.sidebar.subheader("📝 Customize Your Prompt")

# Prompt Builder Class
class PromptBuilder:
    def __init__(self, usecase, language, topics, min_size, max_size, include_topics, exclude_topics):
        self.usecase = usecase
        self.language = language
        self.topics = topics
        self.min_size = min_size
        self.max_size = max_size
        self.include_topics = include_topics
        self.exclude_topics = exclude_topics

    def build_prompt(self):
        project_size = f"📏 The project should also be about {self.min_size} - {self.max_size} lines of code (this is important!)"
        include = "🔍 The project should use these topics: " + ", ".join(self.include_topics) if self.include_topics else ""
        exclude = "🚫 The project should not use these topics: " + ", ".join(self.exclude_topics) if self.exclude_topics else ""
        technologies = f"{include}\n{exclude}" if include or exclude else ""
        prompt = f"✨ Create a coding project for {self.usecase} in the {self.language} programming language. The project should be creative and useful (e.g., a game or useful application). {project_size}\n{technologies}\n✏️ Add comments in the code to explain what is happening and provide a title for the project along with a short description of what it does."
        return prompt

# Main content
if submitted:
    with st.spinner("Generating Prompt..."):
        selected_language = language2 if language2 else language
        prompt_builder = PromptBuilder(usecase, selected_language, topics_options, lines[0], lines[1], include, exclude)
        prompt = prompt_builder.build_prompt()
        st.markdown("---")
        st.subheader("📋 Generated Prompt:")
        st.code(prompt)

# Footer
st.markdown("---")
st.write("Made with :heart: by Muhammad Ibrahim 🚀", unsafe_allow_html=True)


