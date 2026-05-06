def retrieve_context(email):
    try:
        with open("data/knowledge_base.txt", "r") as f:
            kb = f.read()
        return kb
    except:
        return ""
