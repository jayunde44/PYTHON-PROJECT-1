tickets = []

def create_ticket():
    id = len(tickets) +1
    title = input("Enter ticket title: ")
    priority = input("Enter priority (low/medium/high): ")
    ticket = {
        "title": title,
        "priority": priority,
        "id": id,
        "status" : "open"
    }
    tickets.append(ticket)

def view_ticket():
    for ticket in tickets:
        print("Title:", ticket["title"], "| Priority:", ticket["priority"],"id:", ticket["id"], "|status:", ticket["status"])



def close_ticket():
    id = int(input("enter which id to close :"))
    for ticket in tickets:
     if ticket["id"] == id:
        ticket["status"] = "closed"
        print("ticket close")  

def update_priority():
   id = int(input("enter ticket id to update :"))
   new = input("enter new priority (low,medium,high):")
   for ticket in tickets:
      if ticket["id"] == id:
          ticket["priority"] = new
          print("priority updated")
   

   


     
     

create_ticket()
create_ticket()
view_ticket()
close_ticket()
view_ticket()
update_priority()