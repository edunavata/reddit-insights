# app/llm/analyzer.py

import os
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Dict, Any
from app.llm.prompt_builder import build_prompt

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash-latest")


def analyze_post(post: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyzes a Reddit post using Gemini to detect business opportunity signals.

    :param post: A Reddit post dictionary
    :type post: Dict[str, Any]
    :returns: Analysis result as a dictionary with structured fields
    :rtype: Dict[str, Any]
    """
    prompt = build_prompt(post)
    response = model.generate_content(prompt)

    try:
        content = response.text.strip()
        analysis = parse_analysis_response(content)
        return analysis
    except Exception as e:
        return {"error": str(e), "raw_response": response.text}


def parse_analysis_response(response_text: str) -> Dict[str, Any]:
    """
    Cleans and parses Gemini's response into a clean dictionary.
    """
    result = {}
    for line in response_text.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            clean_key = (
                key.lower()
                .replace("*", "")
                .replace("-", "")
                .replace("_", " ")
                .strip()
                .replace(" ", "_")
            )
            result[clean_key] = value.strip(" *")
    return result
