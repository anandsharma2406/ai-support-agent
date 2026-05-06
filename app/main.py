import json
from app.classifier import classify_email
from app.retriever import retrieve_context
from app.responder import generate_response
from app.decision_engine import decide_action, follow_up_needed


def process_email(email):
    classification = classify_email(email)
    context = retrieve_context(email)
    response = generate_response(email, context)
    decision = decide_action(classification, email)
    follow_up = follow_up_needed(classification["topic"])

    return {
        "email": email,
        "classification": classification,
        "response": response,
        "decision": decision,
        "follow_up": follow_up
    }


def main():
    with open("data/sample_emails.json", "r") as f:
        emails = json.load(f)

    results = []

    for item in emails:
        print(f"Processing Email ID: {item['id']}")
        result = process_email(item["email"])
        results.append(result)

    with open("outputs/results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\n✅ Processing complete. Results saved to outputs/results.json")


if __name__ == "__main__":
    main()
