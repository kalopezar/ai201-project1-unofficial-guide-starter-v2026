def judge(question: str, expects: str, answer: str, results) -> bool:
    if not expects:
        return False
    retrieved_text = " ".join(result.text for result in results)
    return expects.strip().casefold() in retrieved_text.casefold()