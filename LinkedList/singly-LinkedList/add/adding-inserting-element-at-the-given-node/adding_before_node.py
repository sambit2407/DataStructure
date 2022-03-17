"""adding element in between the node  of the linkedList(Before any Node) :
         1. Finding X (after which node).
         2. Take the particular(X) node reference save in the new_node reference.
         3.Then what even the new_node added we have to save in the X reference.
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


        else :
            """for head is not null we have to traverse through each node data and print data saving node reference 
            in n """
            n=self.head
            while n is not None:
                print(n.data,end=' ')
                n=n.ref

    def adding_element_at_begining(self,data):
        """creating the node"""
        new_node_obj=Node(data)
        """whatever the head value(address) that assigned to new node reference"""
        new_node_obj.ref=self.head
        # print(new_node_obj.ref)
        """As Node is in the beginning address of the new node would be stored in the head"""
        self.head=new_node_obj
        # print(self.head)

    def adding_element_at_end(self,data):
        """creating the node """
        new_node_obj = Node(data)
        """checking for the empty LinkedList"""
        if self.head is None:
            """By adding element we had to put the address to head """
            self.head=new_node_obj
        else:
            """taking new variable saving the head value"""
            n=self.head
            while n.ref is not None:
                """saving the variable 'n'  second last node reference"""
                n=n.ref
            """here 'n' refers to the last node , so saving new-node reference to second last node"""
            n.ref=new_node_obj

    def adding_after_the_node(self,data,x):
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.ref
        if n is None:
            print('Data is not in LinkedList')
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def adding_before_node(self,data,x):
        """checking if LinkedList is empty"""
        n=self.head
        if n is None:
            print('LinkedList is Empty !!')
            return
        """checking adding before first Node"""
        if n.data==x:
            self.adding_element_at_begining(data)
        """Finding out till the last Node"""
        while n.ref is not None:
            """Finding out the previous Node---As n.ref.data >>n is current node who has next node reference and by 
            that we are accessing the data """
            if n.ref.data==x:
                break
            n=n.ref
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




ll=LinkedList()
ll.adding_element_at_begining(21)
ll.adding_element_at_begining(19)
ll.adding_element_at_begining(15)
ll.adding_before_node(30,21)
ll.print_LinkedList()