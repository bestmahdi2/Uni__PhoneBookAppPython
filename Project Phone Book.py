from __future__ import annotations
import os
import msvcrt
from enum import Enum
from re import compile, fullmatch


class OperationBy(Enum):
    """
       Enum class for OperationBy
    """

    FirstName = 1
    LastName = 2
    PhoneNumber = 3
    EmailAddress = 4


class Node:
    """
        This is a class for simulating a Node.

        Attributes:
            first_name (str): The string value of node first name
            last_name (str): The string value of node last name
            phone_number (str): The string value of phone number
            email_address (str): The DriverStatus value of email address
            next: The Node object of the next node
            prev: The Node object of the previous node
    """

    def __init__(self, first_name: str = "", last_name: str = "", phone_number: str = "-",
                 email_address: str = "-") -> None:
        """
            Constructor function,

            ?
            next: The Node object of the next node
            prev: The Node object of the previous node
            ?

            Parameters:
                first_name (str): The string value of node first name
                last_name (str): The string value of node last name
                phone_number (str): The string value of phone number
                email_address (str): The DriverStatus value of email address
       """

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.next = None
        self.prev = None

    @property
    def next(self) -> Node:
        """
            next node getter function

            Returns:
                self.next: A Node value of next
        """
        return self._next

    @next.setter
    def next(self, next_node: Node) -> None:
        """
            The function to set next node of the node

            Parameters:
                next_node (Node): The string value of next node
        """

        self._next = next_node

    @property
    def prev(self) -> Node:
        """
            prev node getter function

            Returns:
                self.prev: A Node value of prev
        """
        return self._prev

    @prev.setter
    def prev(self, prev_node: Node) -> None:
        """
            The function to set prev node of the node

            Parameters:
                prev_node (Node): The string value of prev node
        """

        self._prev = prev_node

    @property
    def first_name(self) -> str:
        """
            first name getter function

            Returns:
                self.first_name: A string value of first name
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        """
            The function to set first name of the node

            Parameters:
                first name (str): The string value of new first name
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """
            last name getter function

            Returns:
                self.last_name: A string value of last name
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        """
            The function to set last name of the node

            Parameters:
               last name (str): The string value of new last name
        """

        self._last_name = last_name

    @property
    def phone_number(self) -> str:
        """
            phone number getter function

            Returns:
                self.phone_number: A string value of phone number
        """

        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number: str) -> None:
        """
            The function to set phone number of the node

            Parameters:
               phone number (str): The string value of new phone number
        """

        if phone_number == "-":
            self._phone_number = phone_number
            return

        if len(phone_number) != 11:
            print(">> Phone number must be 11 numbers ! The default value used ! <<")

        elif not phone_number.isdigit():
            print(">> Invalid character entered for phone number ! <<")

        else:
            self._phone_number = phone_number

    @property
    def email_address(self) -> str:
        """
            email address getter function

            Returns:
                self.email_address: A string value of email address
        """

        return self._email_address

    @email_address.setter
    def email_address(self, email_address: str) -> None:
        """
            The function to set email address of the node

            Parameters:
               email address (str): The string value of new email_address
        """

        if email_address == "-":
            self._email_address = email_address
            return

        regex = compile(
            r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

        if fullmatch(regex, email_address):
            self._email_address = email_address

        else:
            print(">> Invalid email address is entered ! The default value used ! <<")

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.phone_number}, {self.email_address}"


class LinkedList:
    """
        This is a class for simulating a Node.

        Attributes:
            pointer (Node): The Node object to keep the head of the doubly linked list
            head (Node): The temp Node object to keep the temp node
    """

    def __init__(self) -> None:
        self.head = None
        self.pointer = None

    def insert_contact(self) -> None:
        """
            method to insert a contact to the end of the linked list
        """

        print("\n________________Insertion________________\n")

        # create a new node
        new_contact = Node()

        # initialize the node's values
        new_contact.first_name = input("  Enter First Name > ")
        new_contact.last_name = input("  Enter Last Name > ")
        new_contact.phone_number = input("  Enter Phone Number > ")
        new_contact.email_address = input("  Enter Email Address > ")

        # if no head is created yet, so this new node become the root !
        if not self.head:
            self.head = new_contact

        else:
            # start from head to find last node in linked list and sets its next the new node and
            # sets the pinter to the previous of the new node.
            self.pointer = self.head

            while self.pointer.next:
                self.pointer = self.pointer.next

            self.pointer.next = new_contact
            new_contact.prev = self.pointer

        print("\n>> Contact Added successfully! <<", new_contact, sep="\n")

    def delete_contact(self) -> None:
        """
            method to delete a contact from the linked list
        """

        print("\n________________Deletion________________\n")

        delete_by = input("Which one you want to delete by ?\n 1- First name 2- Last Name\n > ")

        # if the entered input is wrong !
        if not delete_by.isdigit() or not 1 <= int(delete_by) <= 2:
            print(">> Wrong command ! <<")
            return

        delete_by = int(delete_by)

        # get the name (first or last)
        name = input("  Enter the first name > ") if delete_by == OperationBy.FirstName.value else input(
            "  Enter the last name > ")

        # create a pointer to the head
        self.pointer = self.head

        # if should delete by the first name
        if delete_by == OperationBy.FirstName.value:
            while self.pointer:
                if name == self.pointer.first_name:
                    break

                self.pointer = self.pointer.next

            # if no break happened !
            else:
                print("\n>> There is no contact with the entered first name ! <<\n ")
                return

        # if should delete by the last name
        else:
            while self.pointer:
                if name == self.pointer.last_name:
                    break

                self.pointer = self.pointer.next

            # if no break happened !
            else:
                print(">> There is no contact with the entered last name ! <<")
                return

        # if the selected node is the head
        if self.pointer == self.head:
            self.head.prev = None
            self.head = self.head.next

        # if the selected node is after head and has next
        elif self.pointer.next:
            self.pointer.prev.next = self.pointer.next
            self.pointer.next.prev = self.pointer.prev

        # if the selected node is after head and doesn't have next
        elif not self.pointer.next:
            self.pointer.prev.next = None

        print("\n>> The contact deleted successfully ! <<\n")
        self.pointer = None  # empty the pointer !

    def search_contact(self, string: str) -> list:
        """
            method to search a contact in the linked list
        """

        # list to keep the found contacts
        found = []

        self.pointer = self.head

        while self.pointer:
            # find if any of first, last name or email or phone has a letter of "string"
            values = [i for i in [self.pointer.first_name, self.pointer.last_name, self.pointer.email_address,
                                  self.pointer.phone_number] if string in i]

            if values: found.append(self.pointer)  # add the node to the list

            self.pointer = self.pointer.next

        return found

    def sort_contact(self, sort_by: OperationBy) -> None:
        """
            method to search a contact in the linked list
        """

        node = self.head

        print("head", self.head)

        if sort_by == OperationBy.FirstName:
            while node.next:
                node_next = node.next

                while node_next:
                    if node.first_name > node_next.first_name:
                        temp = node.next
                        node.next = node_next.next
                        node_next.next = temp

                        if node.next is not None:
                            node.next.prev = node

                        if node_next.next is not None:
                            node_next.next.prev = node_next

                        temp = node.prev
                        node.prev = node_next.prev
                        node_next.prev = temp

                        if node.prev is not None:
                            node.prev.next = node

                        if node_next.prev is not None:
                            node_next.prev.next = node_next

                    node_next = node_next.next

                node = node.next

        else:
            while node.next:
                node_next = node.next

                while node_next:
                    if node.last_name > node_next.last_name:
                        temp = node.next
                        node.next = node_next.next
                        node_next.next = temp

                        if node.next is not None:
                            node.next.prev = node

                        if node_next.next is not None:
                            node_next.next.prev = node_next

                        temp = node.prev
                        node.prev = node_next.prev
                        node_next.prev = temp

                        if node.prev is not None:
                            node.prev.next = node

                        if node_next.prev is not None:
                            node_next.prev.next = node_next

                    node_next = node_next.next

                node = node.next

    def display(self) -> None:
        """
            method to display the contacts in the linked list
        """

        if not self.head:
            print("\n>> List is empty ! <<")

        # start the node
        self.pointer = self.head

        # traverse till last
        while self.pointer:
            print(self.pointer, end="")

            if self.pointer.next:
                print(" <-> ", end="")

            self.pointer = self.pointer.next

        print()


if __name__ == "__main__":
    # welcome message
    print("\n________________Phone Book________________\n")

    # the linked list
    linked_list = LinkedList()

    continue_ = "y"

    while continue_ == 'y':
        inputer = input(
            "\nEnter your command:\n\n 1- Add new contact.\n 2- Delete existing contact.\n 3- Search for a contact.\n 4- Display contacts.\n 5- Exit.\n > ")

        if not inputer.isdigit() or not 1 <= int(inputer) <= 4:
            print(">> Wrong input entered ! <<")
            continue

        inputer = int(inputer)
        continue_2 = "y"

        # insert
        if inputer == 1:
            while continue_2.lower() == 'y':
                linked_list.insert_contact()
                continue_2 = input("\n> Would you like to continue adding contacts ? [Y/N] \n> ")

        # delete
        elif inputer == 2:
            while continue_2.lower() == 'y':
                linked_list.delete_contact()
                continue_2 = input("> Would you like to continue deleting contacts ? [Y/N] \n> ")

        # search
        elif inputer == 3:
            lister = []
            update = False

            os.system("cls")

            while True:
                if msvcrt.kbhit():
                    key = msvcrt.getch()

                    if key == b'\x1b':
                        break

                    elif key == b'\x08':
                        os.system("cls")

                        if len(lister) > 0: lister.pop()
                        print("Searching for contact: " + "".join(lister))

                        results = linked_list.search_contact("".join(lister))
                        if not results:
                            print("\n>> No contact is found ! <<\n")
                            continue

                        else:
                            print()
                            print(*results, sep="\n")

                    try:
                        if key.decode("utf-8").isalpha() or key.decode("utf-8").isdigit() or key.decode(
                                "utf-8").isalpha():
                            os.system("cls")
                            lister.append(key.decode("utf-8"))
                            print("Searching for contact: " + "".join(lister))

                            results = linked_list.search_contact("".join(lister))
                            if not results:
                                print("\n>> No contact is found ! <<\n")
                                continue

                            else:
                                print()
                                print(*results, sep="\n")

                    except:
                        pass

        # display
        elif inputer == 4:
            linked_list.display()

        # exit
        elif inputer == 5:
            break

        # wrong input
        else:
            print("\n>> Wrong input ! <<")

        continue_ = input("\n>> Would you like to continue operations ? [Y/N] \n> ")

    # goodbye message
    print("\n>> Have a good day ! <<")
