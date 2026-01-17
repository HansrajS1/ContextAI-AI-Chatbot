import streamlit as st
from pathlib import Path

from utils.rag import load_documents, build_vector_store, retrieve_context
from utils.web_search import web_search
from utils.prompts import get_prompt
from models.llm import get_llm_response


st.set_page_config(
    page_title="AI Assistant",
    layout="centered"
)

st.title("AI Assistant")

mode = st.radio(
    "Response Mode",
    ["Concise", "Detailed"],
    horizontal=True
)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.subheader("Upload Documents")

uploaded_files = st.file_uploader(
    "Upload PDF, CSV, or TXT files",
    type=["pdf", "csv", "txt"],
    accept_multiple_files=True
)

DATA_DIR = Path("data/docs")
DATA_DIR.mkdir(parents=True, exist_ok=True)

files_uploaded = False

if uploaded_files:
    for file in uploaded_files:
        file_path = DATA_DIR / file.name

        if not file_path.exists():
            with open(file_path, "wb") as f:
                f.write(file.getbuffer())
            files_uploaded = True

    if files_uploaded:
        st.success("Documents uploaded and indexed successfully")


@st.cache_resource(show_spinner=False)
def setup_rag():
    docs = load_documents()
    return build_vector_store(docs) if docs else None


if files_uploaded:
    setup_rag.clear()

store = setup_rag()


for msg in st.session_state.messages:
    avatar = "assets/user.png" if msg["role"] == "user" else "assets/bot.png"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user", avatar="assets/user.png"):
        st.markdown(user_input)

    context = ""

    if store:
        docs = retrieve_context(store, user_input)
        if docs:
            context = "\n".join(d.page_content for d in docs)

    if not context:
        context = web_search(user_input)

    prompt = get_prompt(
        mode=mode,
        context=context,
        query=user_input
    )

    with st.chat_message("assistant", avatar="assets/bot.png"):
        with st.spinner("Thinking..."):
            answer = get_llm_response(prompt)
            st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
