from ticket import Tickets


class TicketSystem:

    def __init__(self):

        self.tickets = []

        self.next_id = 1
    
    
    def create_ticket(self, description, priority, category=None):

        ticket = Tickets(self.next_id, description, category, priority)

        self.tickets.append(ticket)

        self.next_id += 1

        print(f"Ticket #{ticket.ticket_id} created.")

        return ticket.ticket_id

    
    def view_tickets(self):

        if not self.tickets:

            print("No tickets found.")
        
        else:

            for ticket in self.tickets:

                print(f"ID: {ticket.ticket_id}, Description: {ticket.description}, Category: {ticket.category}, Priority: {ticket.priority}, Status: {ticket.status}")

    
    def set_category(self, ticket_id, category):

        
        for ticket in self.tickets:

            if ticket.ticket_id == ticket_id:

                ticket.category = category

                print(f"Ticket #{ticket_id} category set to {category}.")
                return
            
            
        print(f"Ticket #{ticket_id} not found.")

    
    def resolve_ticket(self, ticket_id):
        
        for ticket in self.tickets:

            if ticket.ticket_id == ticket_id:

                ticket.resolve()

                print(f"Ticket #{ticket_id} resolved.")
                return
            
        print(f"Ticket #{ticket_id} not found.")
    
    def del_ticket(self, ticket_id):
        
        for ticket in self.tickets:

            if ticket.ticket_id == ticket_id:

                self.tickets.remove(ticket)

                print(f"Ticket #{ticket_id} deleted.")
                return
            
        print(f"Ticket #{ticket_id} not found.")
