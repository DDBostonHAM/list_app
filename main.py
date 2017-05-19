#Initialize list
shopping_list = []

def show_help():
    #Give Guidence
    print("What are you getting?: ")
    print("""
Enter 'HELP' to show this help.
Enter 'SHOW' to see current list.
Enter 'DONE' to exit list.
Enter 'DELETE' to remove item from list.
    """)

show_help()

def show_list():
    print("Here is your list.")
    #show contents of list
    for item in shopping_list:
        print(item)
def add_to_list(new_item):
    #add to list
    shopping_list.append(new_item)
    print("Added {}. You have {} items in list.".format(new_item, len(shopping_list)))
def delete_item(del_item):
    #remove item from list
    shopping_list.remove(del_item)

#loop until False
while True:
    #grab input
    new_item = input("> ")
    #Check to see if equal to DONE to exit app
    if new_item == "DONE" or new_item == "done":
        break
    elif new_item == "HELP" or new_item == "help":
        show_help()
        continue
    elif new_item == "SHOW" or new_item == "show":
        show_list()
        continue
    elif new_item == "DELETE" or new_item == "delete":
        del_item = input("What item would you liked removed? ")
        delete_item(del_item)
        continue
    add_to_list(new_item)
show_list()    
