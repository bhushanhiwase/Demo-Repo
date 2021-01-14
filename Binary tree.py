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
            
            
    def print_descending(self):
        if self.right:
            self.right.print_descending()
        print(self.data, end= ",")

        if self.left:
            self.left.print_descending()
            
    def maxDepth(node):
        if node is None:
            return 0
        else:
            lDepth = maxDepth(self.left)         # it will create a call stack and based on the number of iteration before hitting None, we get the parameter added with 1
            rDepth = maxDepth(self.right)

            if rDepth > lDepth:
                return rDepth+1                  # This addition is returned for each call stack and then maximumdepth is returned at the last.       
            else:
                return lDepth+1
            

    def searchitem(self, val):

        if val < self.data:
            if self.left is None:
                print("not exist")
                return
            return self.left.searchitem(val)
        elif val > self.data:
            if self.right is None:
                print("not exist")
                return
            return self.right.searchitem(val)
        else:
            print("Value exist")
            return


a = Node(4)
# a.insert(2)
# a.insert(5)
# a.insert(3)
# a.insert(10)

a.printtree()

