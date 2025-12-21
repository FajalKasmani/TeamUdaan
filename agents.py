"""
Advanced Agent Implementations with Critical Priority Logic.
"""
from typing import Dict
from utils import get_llm_response, extract_category_from_response, extract_priority_from_response

class ClassifierAgent:
    def process(self, complaint: str) -> str:
        prompt = f"""Classify this complaint into ONE category:
[Payment Issue, Delivery Issue, Technical Issue, Account Issue, Security/Data Privacy, General Inquiry]
Complaint: "{complaint}"
Output ONLY the category name."""
        return extract_category_from_response(get_llm_response(prompt))

class PriorityAgent:
    def process(self, complaint: str, category: str) -> str:
        prompt = f"""Determine Priority (Critical, High, Medium, Low).
RULES:
- CRITICAL: Data breach, Legal threat ("sue"), Hacked, Unauthorized transaction.
- HIGH: System crash, Payment failed but deducted.
- MEDIUM: Delays.
- LOW: Questions.
Complaint: "{complaint}"
Category: {category}
Output ONLY the priority word."""
        return extract_priority_from_response(get_llm_response(prompt))

    def re_evaluate(self, complaint: str, priority: str, response: str) -> str:
        prompt = f"""Re-evaluate priority.
If complaint mentions 'police', 'court', 'illegal', 'stolen', ESCALATE to CRITICAL immediately.
Complaint: "{complaint}"
Current Priority: {priority}
Output ONLY the new priority."""
        return extract_priority_from_response(get_llm_response(prompt))

class ResponseAgent:
    def process(self, complaint: str, priority: str) -> str:
        tone = "Urgent & Reassuring" if priority.lower() in ['critical', 'high'] else "Polite & Helpful"
        prompt = f"""Draft a short customer response (Max 2 sentences).
Context: {complaint}
Priority: {priority}
Tone: {tone}
Action: If Critical, promise immediate human contact."""
        return get_llm_response(prompt)

class ActionAgent:
    def process(self, priority: str) -> str:
        prompt = f"""Recommend internal action for Priority: {priority}.
- Critical -> "🚨 TRIGGER INCIDENT RESPONSE"
- High -> "Escalate to Specialist"
- Medium/Low -> "Standard Queue"
Output ONLY the action."""
        return get_llm_response(prompt)

class ComplaintResolverWorkflow:
    def __init__(self):
        self.classifier = ClassifierAgent()
        self.priority = PriorityAgent()
        self.response = ResponseAgent()
        self.action = ActionAgent()
    
    def process_complaint(self, complaint: str) -> Dict:
        cat = self.classifier.process(complaint)
        init_p = self.priority.process(complaint, cat)
        resp = self.response.process(complaint, init_p)
        
        # Self-Correction Loop
        final_p = self.priority.re_evaluate(complaint, init_p, resp)
        
        act = self.action.process(final_p) # Action based on Final Priority
        
        # ERROR WAS HERE -> FIXED NOW
        return {
            'complaint': complaint,
            'category': cat,
            'initial_priority': init_p,
            'final_priority': final_p,  # Corrected variable name
            'response': resp,
            'action': act,
            'priority_changed': init_p != final_p
        }