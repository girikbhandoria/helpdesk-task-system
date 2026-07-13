
class Tickets:
    
    def __init__(self, ticket_id, description, category, priority):

        self.ticket_id = ticket_id

        self.description = description

        self.category = category

        self.priority = priority

        self.status = "Open"
    

    def resolve(self):
        
        self.status = "Resolved"
