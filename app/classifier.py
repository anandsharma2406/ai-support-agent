import json
from app.llm import call_llm

def classify_email(email):
    prompt = f"""
    Classify the customer support email.

    Email: "{email}"

    Return ONLY valid JSON:
    {{
      "urgency": "Low" or "Medium" or "High",
      "topic": "Account" or "Billing" or "Bug" or "Feature Request" or "Technical Issue"
    }}
    """

    result = call_llm(prompt)

    try:
        return json.loads(result)
    except:
        return {
            "urgency": "Medium",
            "topic": "Technical Issue"
        }
