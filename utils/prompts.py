def get_prompt(mode, context, query):
    if mode == "Concise":
        return f"Answer briefly.\nContext:\n{context}\nQuestion:\n{query}"
    return f"Answer in detail with examples.\nContext:\n{context}\nQuestion:\n{query}"
