def load_transcript(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()
