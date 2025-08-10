def run(prompt: str, user_query: str = "") -> str:
    """
    Your first custom AI model (rule-based stub).
    Returns a short, friendly sentence using the prompt.
    If user_query is provided, it’s appended as extra context.
    """
    p = (prompt or "").strip() or "something mysterious"
    text = f"A fun story about {p} begins."
    if user_query:
        # ensure sentence separation + include the optional query
        if not text.rstrip().endswith(('.', '!', '?')):
            text += "."
        text += f" It considers the question: '{user_query.strip()}'."
    return text
