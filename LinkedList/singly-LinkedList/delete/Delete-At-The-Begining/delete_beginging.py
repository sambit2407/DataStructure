"""Deleting at the beginning of the LinkedList :
         1. Check LinkedList is empty.
         2. Delete the first node if not empty.
         3..
          """

''' Two scenarios >>>
        1. If LinkedList is empty.
        2. If linked List is not empty.  '''


class Node:
    """Creating Node for Linked List"""

    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    """Traversing through the LinkedList"""

    def __init__(self):
        """Here LinkedList is empty ,so Head is now empty"""
        self.head = None

    def print_LinkedList(self):
        """ For Head is null """
        if self.head is None:

            print('Linked list is empty.')


        else:
            """for head is not null we have to traverse through each node data and print data saving node reference 
            in n """
            n = self.head
            while n is not None:
                print(n.data, end=' ')
                n = n.ref

    def adding_element_at_begining(self, data):
        """creating the node"""
        new_node_obj = Node(data)
        """whatever the head value(address) that assigned to new node reference"""
        new_node_obj.ref = self.head
        # print(new_node_obj.ref)
        """As Node is in the beginning address of the new node would be stored in the head"""
        self.head = new_node_obj
        # print(self.head)

    def adding_element_at_end(self, data):
        """creating the node """
        new_node_obj = Node(data)
        """checking for the empty LinkedList"""
        if self.head is None:
            """By adding element we had to put the address to head """
            self.head = new_node_obj
        else:
            """taking new variable saving the head value"""
            n = self.head
            while n.ref is not None:
                """saving the variable 'n'  second last node reference"""
                n = n.ref
            """here 'n' refers to the last node , so saving new-node reference to second last node"""
            n.ref = new_node_obj

    def adding_after_the_node(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print('Data is not in LinkedList')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def adding_before_node(self, data, x):
        """checking if LinkedList is empty"""
        n = self.head
        if n is None:
            print('LinkedList is Empty !!')
            return
        """checking adding before first Node"""
        if n.data == x:
            self.adding_element_at_begining(data)
        """Finding out till the last Node"""
        while n.ref is not None:
            """Finding out the previous Node---As n.ref.data >>n is current node who has next node reference and by 
            that we are accessing the data """
            if n.ref.data == x:
                break
            n = n.ref
        """Here we got the previous node as n"""
        if n.ref is None:
            print('Data not found in LinkedList')

            """After getting the previous node we just have to add after the previous node"""
        else:
            """Creating the new node"""
            new_node = Node(data)
            """taking reference of the new node from the previous node as we are adding after the previous node"""
            new_node.ref = n.ref
            """setting the previous node reference as new node"""
            n.ref = new_node

    def insert_empty(self, data):

        if self.head is None:
            new_node = Node(data)
            self.head = new_node

        else:
            print('LinkedList is Not Empty !!')

    def delete_beginning(self):
        """ This is the first Node as i assigned the head value to n(First Node)"""
        n = self.head
        if self.head is None:
            print('LinkedList is Empty Already !!!')
        elif n.data is not None and n.ref is None:
            n.data = None
            self.head = None
        else:
            """Then i have assigned the reference of first first Node to head"""
            self.head = n.ref

    def delete_at_end(self):
        if self.head is None:
            print('LinkedList is empty!!')
        else:
            """Taking the first Node as assigning head as n"""
            n = self.head
            """n.ref.ref means checking the next node ref is none or not"""
            while n.ref.ref is not None:
                """going to the next Node"""
                n = n.ref
            """then after getting previous node i deleted the reference of the next node to delete the last node"""
            n.ref=None


ll = LinkedList()
ll.adding_element_at_begining(10)


ll.delete_beginning()
ll.print_LinkedList()
