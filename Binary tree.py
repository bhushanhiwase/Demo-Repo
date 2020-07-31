class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


    def insert(self, item):

        if self.data:
            if item < self.data:
                if self.left is None:             # see if the left node is None, if so directly insert element
                    self.left = Node(item)
                else:                             # else, if node not None, travel to bottom left node using recursion
                    self.left.insert(item)

            elif item > self.data:
                if self.right is None:
                    self.right = Node(item)
                else:
                    self.right.insert(item)

        else:
            self.data = data

    def printtree(self):                        # use recursion to print the tree
        if self.left:                           # we first print all the left elements and then the right
            self.left.printtree()               # Recursion uses call stack
        print(self.data)                        # This prints the node data even if there is only single node
        if self.right:
            self.right.printtree()



a = Node(4)
# a.insert(2)
# a.insert(5)
# a.insert(3)
# a.insert(10)

a.printtree()

