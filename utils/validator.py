def validate_request(text: str):

    if not text.strip():
        raise ValueError("Request cannot be empty.")

    return True