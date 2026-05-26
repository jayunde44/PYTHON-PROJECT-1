tickets = []

def create_ticket():
    title = input("Enter ticket title: ")
    priority = input("Enter priority (low/medium/high): ")
    ticket = {
        "title": title,
        "priority": priority
    }
    tickets.append(ticket)

def view_tickets():
    for ticket in tickets:
        print("Title:", ticket["title"], "| Priority:", ticket["priority"])

create_ticket()
create_ticket()
view_tickets()



        
