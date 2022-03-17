"""adding element in the begining of the linkedList :
         1. Creating the Node.
         2. Put head value to the node_reference
         3. Then put node object address to the head  """

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
                print(n.data)
                n=n.ref

    def adding_element(self,data):
        new_node_obj=Node(data)
        new_node_obj.ref=self.head
        print(new_node_obj.ref)
        self.head=new_node_obj
        print(self.head)


obj=LinkedList()
obj.adding_element(19)
obj.adding_element(21)

obj.adding_element(20)
obj.adding_element(25)

obj.print_LinkedList()