"""
Advanced Memory Module with Smart ID Generation.
"""
from datetime import datetime
from typing import List, Dict, Optional

class ComplaintMemory:
    def __init__(self):
        self.high_priority_complaints: List[Dict] = []
    
    def add_complaint(self, complaint: str, category: str, priority: str, 
                      complaint_id: Optional[str] = None) -> None:
        """Add complaint with Smart ID based on severity."""
        
        if complaint_id is None:
            count = len(self.high_priority_complaints) + 1
            p_lower = priority.lower()
            
            # Smart ID Generation
            if p_lower == 'critical':
                generated_id = f"CRIT-{count:03d}" # e.g., CRIT-001
            elif p_lower == 'high':
                generated_id = f"HIGH-{count:03d}" # e.g., HIGH-001
            else:
                generated_id = f"TKT-{count:03d}"
        else:
            generated_id = complaint_id

        complaint_entry = {
            'id': generated_id,
            'complaint': complaint,
            'category': category,
            'priority': priority.capitalize(),
            'timestamp': datetime.now().strftime("%H:%M:%S"), # Short time for UI
            'status': 'Open'
        }
        self.high_priority_complaints.append(complaint_entry)
    
    def get_all_complaints(self) -> List[Dict]:
        return self.high_priority_complaints.copy()
    
    def get_complaint_count(self) -> int:
        return len(self.high_priority_complaints)
    
    def clear_memory(self) -> None:
        self.high_priority_complaints.clear()