def clean_analysis_keys(raw: dict) -> dict:
    """
    Cleans raw LLM analysis output by stripping extraneous characters
    from keys and values. Converts confidence to float if possible.

    :param raw: Raw dictionary from LLM response
    :return: Cleaned dictionary with correct field names
    """
    cleaned = {}
    for key, value in raw.items():
        clean_key = key.strip().strip('"').strip("'").rstrip(",").strip()
        clean_value = value.strip().strip('"').strip("'").rstrip(",").strip()
        if clean_key.lower() == "confidence":
            try:
                clean_value = float(clean_value)
            except ValueError:
                clean_value = 0.0
        cleaned[clean_key] = clean_value
    return cleaned
