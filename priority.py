class Priority:

    @staticmethod

    def auto_assign(description):

        ticket_text = f"{description}".strip().lower()

        if not ticket_text:

            return None
        
        priority_rules = {

            "Critical": ["down", "crash", "breach", "outage", "broken", "security"],

            "High": ["urgent", "error", "fail", "blocked", "login"],

            "Medium": ["slow", "update", "reset", "invoice", "account"],

            "Low": ["ui", "password", "how to", "question", "documentation", "feedback", "suggestion", "feature request", "typo"]


        }

        for priority, keywords in priority_rules.items():

            if any(keyword in ticket_text for keyword in keywords):

                return priority
            
        return None
