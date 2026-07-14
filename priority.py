from validation import Validation


class Priority:

    @staticmethod

    def auto_assign(description):

        Validation.validate_description(description)

        ticket_text = f"{description}".strip().lower()


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
