from ticketsystem import TicketSystem
from priority import Priority


def main():
    
    system = TicketSystem()

    while True:

        print("\nTicket Management System")

        print("1. Create Ticket")
        print("2. View Ticket")
        print("3. Resolve Ticket")
        print("4. Delete Ticket")
        print("5. Exit")


        choice = input("Enter Your Choice: ").strip()


        if choice == "1":

            category = None

            while True:

                print("\nChoose one of the following category:-")

                print("1. Software")
                print("2. Hardware")
                print("3. Network")
                print("4. Other")

                choice2 = input("Enter Your Choice: ").strip()

                if choice2 == "1":

                    category = "Software"
                    break

                elif choice2 == "2":

                    category = "Hardware"
                    break

                elif choice2 == "3":

                    category = "Network"
                    break

                elif choice2 == "4":

                    category = "Other" 
                    break

                else:

                    print("Invalid choice. Please select a valid option!")


            while True:

                description = input("\nEnter the Ticket Description: ")

                priority = Priority.auto_assign(description)

                if priority is None:

                    print("Invalid description!: Try again!")
                    continue

                ticket_id = system.create_ticket(description, priority, category)
                break
        
        elif choice == "2":

            system.view_tickets()
        
        elif choice == "3":

            try:

                ticket_id = int(input("Enter the ticket ID to resolve: "))

                system.resolve_ticket(ticket_id)
            
            except ValueError:

                print("Invalid Ticket ID. Please Enter a number.")
        

        elif choice == "4":

            try:

                delete_ticket = int(input("Enter the ticket ID to delete: "))

                system.del_ticket(delete_ticket)
            
            except ValueError:

                print("Invalid Ticket ID. Please Enter a number")
        

        elif choice == "5":

            print("\nExiting the Ticket Management System.\n")
            break
        
        else:

            print("Invalid choice. Please select a valid option!")



if __name__ == "__main__":

    main()
