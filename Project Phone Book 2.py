import sys


class Node:
    def __init__(self, first_name, last_name, phone_number):
        self.next = None
        self.prev = None
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tempNode = None


########################################

phone_book = DoublyLinkedList()


########################################

def menu():
    print(".....................................................................")
    print("\nYou can now perform the following operations on this phonebook\n")
    print("1- Add a new contact")
    print("2- Delete an existing contact")
    print("3- Search for a contact")
    print("4- Show all contacts")
    print("5- Exit")

    option = int(input("\nPlease choose an option: "))

    return option


def add_contact():
    first_name = str(input("Enter your firstName: "))
    last_name = str(input("Enter your lastName: "))
    phone_number = int(input("Enter your phoneNumber: "))

    new_contact = Node(first_name, last_name, phone_number)

    if phone_book.head == None:
        phone_book.head = new_contact

    else:
        phone_book.tempNode = phone_book.head

        while phone_book.tempNode.next != None:
            phone_book.tempNode = phone_book.tempNode.next

        phone_book.tempNode.next = new_contact
        new_contact.prev = phone_book.tempNode

    print("\nContact Added successfully!\n", new_contact.first_name, new_contact.last_name, new_contact.phone_number)


def delete_contact():
    contact = str(input("Please enter the name of the contact you want to remove: "))

    phone_book.tempNode = phone_book.head

    find = False

    while phone_book.tempNode != None:
        if contact == phone_book.tempNode.first_name:
            find = True
            break

        phone_book.tempNode = phone_book.tempNode.next

    if find == True:
        if phone_book.tempNode == phone_book.head:
            phone_book.head.prev = None
            phone_book.head = phone_book.head.next

        elif phone_book.tempNode.next != None:
            phone_book.tempNode.prev.next = phone_book.tempNode.next
            phone_book.tempNode.next.prev = phone_book.tempNode.prev

        elif not phone_book.tempNode.next != None:
            phone_book.tempNode.prev.next = None

        print("\nThe contact deleted successfully !\n")

    else:
        print("\nThere is no contact with the entered name !\n")


def search():
    option = int(input("\nEnter a search option: \n1. firstName\n2. lastName\n3. phoneNumber\n"))

    temp = []

    if option == 1:
        contact = str(input("Please enter the firstname of the contact you want to search: "))

        phone_book.tempNode = phone_book.head

        while phone_book.tempNode != None:
            if contact in phone_book.tempNode.first_name:
                temp.append(phone_book.tempNode)

            phone_book.tempNode = phone_book.tempNode.next

    elif option == 2:
        contact = str(input("Please enter the lastname of the contact you want to search: "))

        phone_book.tempNode = phone_book.head

        while phone_book.tempNode != None:
            if contact in phone_book.tempNode.last_name:
                temp.append(phone_book.tempNode)

            phone_book.tempNode = phone_book.tempNode.next

    elif option == 3:
        contact = int(input("Please enter the number of the contact you want to search: "))

        while phone_book.tempNode != None:
            if contact in phone_book.tempNode.phone_number:
                temp.append(phone_book.tempNode)

            phone_book.tempNode = phone_book.tempNode.next

    else:
        print("Invalid a search option!")
        return -1

    if len(temp) == 0:
        return -1

    else:
        display_all(temp)
        return 1


def display_all(temp = []):  # displays all content of phonebook
    if len(temp) == 0:
        if phone_book.head == None:
            print("phonebook is empty!")

        else:
            # start the node
            phone_book.tempNode = phone_book.head

            # traverse till last
            while phone_book.tempNode != None:
                print(phone_book.tempNode.first_name)
                phone_book.tempNode = phone_book.tempNode.next

    else:
        for item in temp:
            print(item.first_name)

def exit():
    print("Thank you for using our phone directory.\n")

    sys.exit("Goodbye, have a nice day!")


########################################

print("\nHello dear user, welcome to our smartphone directory system\n")

ch = 1

while ch in (1, 2, 3, 4, 5):
    ch = menu()

    if ch == 1:
        add_contact()

    elif ch == 2:
        delete_contact()

    elif ch == 3:
        d = search()

        if d == -1:
            print("The contact does not exist. Please try again")

    elif ch == 4:
        display_all()

    else:
        exit()
