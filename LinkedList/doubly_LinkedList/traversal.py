class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def traversal_printLL(self):
        if self.head is None:
            print('LinkedList is empty !!')

        else:
            n=self.head
            while n is not None:
                print(n.data , end='')
                n=n.nref

    def traversal_printLL_reverse(self):
        if self.head is None:
            print('LinkedList is empty !!')

        else:
            n = self.head
            """We need last Node to go reverse"""
            while n.nref is not None:

                n = n.nref
            while n is not None:
                print(n.data ,end ='')
                """going previous as n is referring to previous Node"""
                n=n.pref


dll=DoublyLinkedList()
dll.traversal_printLL()
dll.traversal_printLL_reverse()


