"""
feedback_logger.py
Centralized feedback logger for audit assistant.
"""
import datetime
from typing import Any, Dict, List

class FeedbackLogger:
    def __init__(self):
        self.feedback_log: List[Dict[str, Any]] = []

    def log_feedback(self, user_id: str, rating: int, comments: str, workflow_outcome: str):
        entry = {
            'timestamp': datetime.datetime.utcnow().isoformat(),
            'user_id': user_id,
            'rating': rating,
            'comments': comments,
            'workflow_outcome': workflow_outcome
        }
        self.feedback_log.append(entry)

    def get_feedback(self) -> List[Dict[str, Any]]:
        return self.feedback_log
