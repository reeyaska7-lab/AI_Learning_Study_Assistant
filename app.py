import streamlit as st
from agent import LearningAgent

st.set_page_config(
    page_title="AI Learning & Study Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Learning & Study Assistant")
st.write(
    "Your intelligent study assistant powered by Agentic AI, "
    "RAG, Memory and Study Tools."
)

if "agent" not in st.session_state:
    st.session_state.agent = LearningAgent()

if "messages" not in st.session_state:
    st.session_state.messages = []

st.sidebar.header("📖 Study Material")

uploaded_file = st.sidebar.file_uploader(
    "Upload your study notes",
    type=["txt"]
)

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    st.session_state.agent.load_document(text)
    st.sidebar.success("Study material loaded successfully!")

st.sidebar.divider()

st.sidebar.header("⚡ Quick Actions")

if st.sidebar.button("📅 Create 5-Day Study Plan"):
    response = st.session_state.agent.handle(
        "Create a 5 day study plan"
    )
    st.session_state.messages.append(
        ("You", "Create a 5 day study plan")
    )
    st.session_state.messages.append(
        ("Assistant", response)
    )

if st.sidebar.button("📝 Generate 5 MCQs"):
    response = st.session_state.agent.handle(
        "Generate 5 MCQs"
    )
    st.session_state.messages.append(
        ("You", "Generate 5 MCQs")
    )
    st.session_state.messages.append(
        ("Assistant", response)
    )

st.subheader("💬 Ask Your Study Assistant")

for sender, message in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**👤 You:** {message}")
    else:
        st.markdown(f"**🤖 Assistant:**\n\n{message}")

question = st.chat_input(
    "Ask something about your study material..."
)

if question:
    response = st.session_state.agent.handle(question)

    st.session_state.messages.append(
        ("You", question)
    )

    st.session_state.messages.append(
        ("Assistant", response)
    )

    st.rerun()

st.divider()

st.caption(
    "AI Learning & Study Assistant | "
    "Agentic AI Project"
)