"""
UTILITY FUNCTIONS FOR LLM INTEGRATION
Backend: Google Gemini (Stable)
"""
import os
import re
from dotenv import load_dotenv
import google.generativeai as genai  # Stable Library

# Load Environment Variables
load_dotenv()

def get_llm_response(prompt: str) -> str:
    """
    Hybrid Logic:
    1. Tries to use Google Gemini API (gemini-pro).
    2. If fails, falls back to Mock.
    """
    api_key = os.getenv("GOOGLE_API_KEY")

    # --- PLAN A: REAL AI (Google Gemini) ---
    if api_key:
        try:
            # Configure API
            genai.configure(api_key=api_key)
            
            # Use 'gemini-pro' (Most stable model)
            model = genai.GenerativeModel('gemini-pro')
            
            print(f"🚀 PINGING GEMINI PRO with prompt: {prompt[:30]}...")
            
            response = model.generate_content(prompt)
            
            # Check if response is valid
            if response.text:
                return response.text.strip()
            
        except Exception as e:
            print(f"⚠️ Google Gemini Error: {e}")
            print("👉 Switching to Mock Mode temporarily.")
    
    # --- PLAN B: SMART MOCK (Fallback) ---
    return get_mock_llm_response(prompt)

def get_mock_llm_response(prompt: str) -> str:
    """
    Fallback logic if API fails.
    """
    p_lower = prompt.lower()
    
    # Extract text inside quotes
    match = re.search(r'Complaint:\s*"(.*?)"', prompt)
    text_to_analyze = match.group(1).lower() if match else p_lower

    # 1. CLASSIFIER
    if "classify" in p_lower:
        if any(w in text_to_analyze for w in ["hack", "security", "breach", "stolen", "police"]):
            return "Security/Data Privacy"
        if any(w in text_to_analyze for w in ["refund", "deduct", "money", "charge"]):
            return "Payment Issue"
        return "General Inquiry"

    # 2. PRIORITY
    if "priority" in p_lower:
        if any(w in text_to_analyze for w in ["sue", "police", "legal", "hacked", "threat"]):
            return "Critical"
        if any(w in text_to_analyze for w in ["deducted", "fraud", "urgent", "scam"]):
            return "High"
        return "Low"

    # 3. ACTION
    if "recommend" in p_lower or "draft" in p_lower:
        if "critical" in p_lower: return "IMMEDIATE: Escalate to Legal Team."
        if "high" in p_lower: return "Investigate transaction immediately."
        return "Send standard help article."

    return "Processing..."

# Helpers
def extract_category_from_response(response: str) -> str:
    return response.replace("Category:", "").strip().split('\n')[0]

def extract_priority_from_response(response: str) -> str:
    r = response.lower().strip()
    if "critical" in r: return "Critical"
    if "high" in r: return "High"
    if "medium" in r: return "Medium"
    return "Low"