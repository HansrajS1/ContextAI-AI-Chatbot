from langchain_groq import ChatGroq
from config.config import GROQ_API_KEY

def get_llm_response(prompt):
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY not found")

    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-3.1-8b-instant",
        temperature=0.2
    )

    response = llm.invoke(prompt)
    return response.content
