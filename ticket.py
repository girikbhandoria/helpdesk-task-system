from validation import Validation


class Tickets:
    
    def __init__(self, ticket_id, description, category, priority):

        self.ticket_id = ticket_id

        self.description = description

        self.category = category

        self.priority = priority

        self.status = "Open"

        Validation.validate_ticket_id(ticket_id)

        Validation.validate_description(description)

        Validation.validate_category(category)

        Validation.validate_priority(priority)
    

    def resolve(self):
        
        self.status = "Resolved"
