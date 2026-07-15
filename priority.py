from validation import Validation


class Priority:

    @staticmethod


    def auto_assign(description):

        Validation.validate_description(description)

        ticket_text = f"{description}".strip().lower()


        priority_rules = {
            

"Critical": ["critical", "down", "outage", "crash", "breach", "security", "hacked", "compromised", "malware", "virus", "ransomware", "data loss", "corruption", "production down", "service unavailable", "database down", "server down", "system failure", "ddos", "unresponsive"],

"High": ["urgent", "error", "failed", "failure", "blocked", "login", "authentication", "access denied", "cannot access", "timeout", "api error", "sync failed", "payment failed", "exception", "500", "403", "404", "permission", "performance", "latency"],

"Medium": ["slow", "update", "reset", "account", "invoice", "billing", "subscription", "configuration", "install", "upgrade", "migration", "integration", "backup", "restore", "notification", "email issue", "license", "settings", "report", "export", "import"],
    
"Low": ["ui", "password", "how to", "question", "documentation", "feedback", "suggestion", "feature request", "enhancement", "typo", "cosmetic", "help", "guide", "tutorial", "faq", "clarification", "wishlist", "improvement", "training", "information"]


        }

        for priority, keywords in priority_rules.items():

            if any(keyword in ticket_text for keyword in keywords):

                return priority
            
        return None
