import os

#Initialize list
shopping_list = []


def show_help():
    #Give Guidence
    print("Available Commands: ")
    print(" \
    Enter 'HELP' to show this help.\n \
    Enter 'SHOW' to see current list.\n \
    Enter 'DONE' to exit list.\n \
    Enter 'DELETE' to remove item from list.")

def show_list():
    print("List:")
    #show contents of list
    for item in shopping_list:
        print(item)
def add_to_list(entry):
    #add to list
    shopping_list.append(entry)
    print("Added {}. You have {} items in list.".format(entry, len(shopping_list)))
def delete_item(del_item):
    #remove item from list
    shopping_list.remove(del_item)

def cleaning():
    os.system('clear')

show_help()
#loop until False
while True:
    entry = input("Add Item >:")
    cleaning()

    if entry == "done":
        break
    elif entry == "help":
        show_help()
        continue
    elif entry == "show":
        show_list()
        continue
    elif entry == "delete":
        show_list()
        del_item = input("What item would you liked removed? ")
        delete_item(del_item)
        show_list()
        continue
    add_to_list(entry)
show_list()
