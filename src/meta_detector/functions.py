def is_meta_question(msg):
    msg = msg.lower()
    return len(msg) < 110 and (
        'anyone' in msg or 'any' in msg or 'someone' in msg
    ) and 'how' not in msg and 'what' not in msg and 'why' not in msg
