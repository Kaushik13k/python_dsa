## CREATE TREES USING LIST

## LEFT: cell[2x]
## RIGHT: cell[2x + 1]


class BinaryTree:
    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_used_index = 0
        self.max_size = size
    
    def insert_node(self, value):
        if self.last_used_index + 1 == self.max_size:
            return "The node is full"
        self.custom_list[self.last_used_index + 1] = value
        self.last_used_index += 1
        print(f"The value {value} is successfully inserted!")
        return f"The value {value} is successfully inserted!"
    
    def search_element(self, value): # The searching uses the LEVEL ORDER TRAVERSAL!
        for val in range(len(self.custom_list)):
            if self.custom_list[val] == value:
                return f"found the element {value} in postition {val}"
        return "element not found"


tree_instance = BinaryTree(4)
tree_instance.insert_node(1)
tree_instance.search_element(1)