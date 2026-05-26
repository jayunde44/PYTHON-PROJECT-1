tickets = []
def create_ticket():
    title = input("Enter ticket title: ")
    priority = input("Enter priority (low/medium/high): ")
    ticket = {
        "title": title,        # variable, not hardcoded
        "priority": priority   # variable, not hardcoded
    }
    tickets.append(ticket)

create_ticket()
create_ticket()

print(tickets)