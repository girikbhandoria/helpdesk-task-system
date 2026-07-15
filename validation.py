class Validation:

    VALID_CATEGORIES = ["Software", "Hardware", "Network", "Other"]
    VALID_PRIORITIES = ["Critical", "High", "Medium", "Low"]

    @staticmethod

    def validate_description(description):

        if not isinstance(description, str) or not description.strip():

            raise ValueError("Description cannot be empty.")
        

    @staticmethod
    
    def validate_category(category):

        if category not in Validation.VALID_CATEGORIES:

            raise ValueError("Invalid category.")
        

    @staticmethod

    def validate_priority(priority):

        if priority not in Validation.VALID_PRIORITIES:

            raise ValueError("Invalid priority.")
        

    @staticmethod

    def validate_ticket_id(ticket_id):

        if not isinstance(ticket_id, int) or ticket_id <= 0:

            raise ValueError("Ticket ID must be a positive integer.")
        
        