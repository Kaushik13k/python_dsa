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
    
    def pre_order_traversal(self, index):
        if index > self.last_used_index:
            return
        print(self.custom_list[index]) # ROOT
        self.pre_order_traversal(index * 2) # LEFT: cell[2x]
        self.pre_order_traversal(index * 2 + 1) # RIGHT: cell[2x + 1]
    
    def in_order_traversal(self, index):
        if index > self.last_used_index:
            return
        self.in_order_traversal(index * 2) # LEFT: cell[2x]
        print(self.custom_list[index]) # ROOT
        self.in_order_traversal(index * 2 + 1) # RIGHT: cell[2x + 1]

    def post_order_traversal(self, index):
        if index > self.last_used_index:
            return
        self.post_order_traversal(index * 2) # LEFT: cell[2x]
        self.post_order_traversal(index * 2 + 1) # RIGHT: cell[2x + 1]
        print(self.custom_list[index]) # ROOT

    def level_order_traversal(self, index):
        for i in range(index, self.last_used_index +1):
            print(self.custom_list[i])
        
    def delete_node(self, value):
        if self.last_used_index ==0:
            return "There is nothing to delete"
        for i in range(1, self.last_used_index +1):
            if self.custom_list[i] == value:
                self.custom_list[i] = self.custom_list[self.last_used_index]
                self.last_used_index -= 1
                return f"The value {value} is deleted!"

    def delete_tree(self):
        self.custom_list = None
        return "The tree is been deleted!"


tree_instance = BinaryTree(7)
tree_instance.insert_node(1)
tree_instance.insert_node(2)
tree_instance.insert_node(3)
tree_instance.insert_node(4)
tree_instance.insert_node(5)
tree_instance.insert_node(6)
tree_instance.search_element(2)

tree_instance.pre_order_traversal(1)
tree_instance.in_order_traversal(1)
tree_instance.post_order_traversal(1)
tree_instance.level_order_traversal(1)

tree_instance.delete_tree()