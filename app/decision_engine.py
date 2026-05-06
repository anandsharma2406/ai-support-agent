def decide_action(classification, email):
    urgency = classification.get("urgency", "Medium")
    topic = classification.get("topic", "Technical Issue")

    if urgency == "High":
        return "ESCALATE"

    if topic in ["Billing", "Technical Issue"]:
        return "ESCALATE"

    if any(word in email.lower() for word in ["error", "fail", "crash"]):
        return "ESCALATE"

    return "AUTO_REPLY"


def follow_up_needed(topic):
    if topic in ["Bug", "Technical Issue"]:
        return "Follow up in 24 hours"
    return None
