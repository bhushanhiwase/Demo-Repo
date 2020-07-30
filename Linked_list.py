class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next

    def deleteitem(self,item):
        temp = self.head
        if temp is not None:
            if temp.data == item:
                self.head = temp.next
                temp = None
                return

        while temp:
            if temp.data == item:
                prev.next = temp.next
                temp.next = None

            prev = temp
            temp = temp.next

    def insertafter(self, prev, new):
        new_node = Node(new)
        new_node.next = prev.next
        prev.next = new_node

    def appends(self, new):
        new_node = Node(new)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_front(self, new):
        new_node = Node(new)
        new_node.next = self.head
        self.head = new_node



list1 = Linkedlist()
list1.head = Node(100)
second_element = Node(200)
third_element =  Node(300)
fourth_element = Node(400)
fifth_element = Node(500)

list1.head.next = second_element
second_element.next = third_element
third_element.next = fourth_element
fourth_element.next = fifth_element



list1.deleteitem(200)
list1.printlist()


