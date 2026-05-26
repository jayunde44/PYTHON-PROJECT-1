import json
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

def save_tickets():
    with open("tickets.json", "w") as f:
        json.dump(tickets, f)

def load_tickets():
    global tickets
    try:
        with open("tickets.json", "r") as f:
            tickets = json.load(f)
    except FileNotFoundError:
        tickets = []

load_tickets()  

while True:
   print("1. create ticket")
   print("2. view ticket")
   print("3. close ticket")
   print("4. update priority")
   print("5. exit")

   choice = (input("enter choice :"))
   if choice == "1":
      create_ticket()
   elif choice == "2":
    view_ticket()
   elif choice == "3":
    close_ticket()
   elif choice == "4":
    update_priority()
   elif choice == "5":
    save_tickets()
    break
      

    
    

    

     
     

