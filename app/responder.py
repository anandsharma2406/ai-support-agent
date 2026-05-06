from app.llm import call_llm

def generate_response(email, context):
    prompt = f"""
    You are a helpful customer support assistant.

    Customer Email:
    {email}

    Knowledge Base:
    {context}

    Write a clear, polite, and helpful response.
    """

    return call_llm(prompt)
