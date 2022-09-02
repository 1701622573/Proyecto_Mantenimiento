"""
node class
"""
class TSTNode:
    """
    TST node
    """
    #constructor: this method receives the key, the value, the left node,
    # the right node and the parent node
    def __init__(self, id_node, name, party, x = 0, y = 0, left_child=None, middle_child=None,
                right_child=None, parent_node=None):
        self.id = id_node
        self.name = name
        self.party = party
        self.left_child = left_child
        self.middle_child = middle_child
        self.right_child = right_child
        self.parent_node = parent_node
        self.x = x
        self.y = y

    def has_parent_node(self):
        """
        has parent node
        """
        return self.parent_node

    def has_left_child(self):
        """
        This method verifies if the current node has a child node on the left
        """
        return self.left_child

    def has_middle_child(self):
        """
        This method verifies if the current node has a child node on the middle
        """
        return self.middle_child

    def has_right_child(self):
        """
        This method verifies if the current node has a child node on the right
        """
        return self.right_child

    def get_num_childs(self):
        """
        get number childs
        """
        num=0
        if self.left_child:
            num += 1
        if self.middle_child:
            num += 1
        if self.right_child:
            num += 1
        return num

    def what_child_is(self,son_id):
        """
        helps to know if child
        """
        pos=None
        if son_id == self.left_child.id:
            print("ES HIJO IZQUIERDO")
            pos=0
            return pos
        if son_id == self.middle_child.id:
            print("ES HIJO MEDIO")
            pos=0
            return pos
        if son_id == self.right_child.id:
            print("ES HIJO DERECHO")
            pos=0
            return pos
        return pos

    def is_left_child(self):
        """
        This method verifies if self node is left child of other one
        """
        return self.parent_node and self.parent_node.leftChild == self

    def is_middle_child(self):
        """
        This method verifies if self node is middle child of other one
        """
        return self.parent_node and self.parent_node.middleChild == self

    def is_right_child(self):
        """
        This method verifies if self node is right child of other one
        """
        return self.parent_node and self.parent_node.rightChild == self

    def is_root(self):
        """
        This method verifies if self node is lthe main root of the tree
        """
        return not self.parent_node

    def is_leaf(self):
        """
        This method verifies if self node is a leaf
        """
        return not (self.left_child or self.right_child or self.middle_child)

    def has_some_child(self):
        """
        This method verifies if self node has at least one child
        """
        return (self.right_child or self.left_child or self.middle_child)

    def has_all_childs(self):
        """
        This method verifies if self node has both children
        """
        return (self.right_child and self.left_child and self.middle_child)

    def update_node_information(self, key, name, left_child, middle_child, right_child):
        """
        #This method update the node information (key, value and children)
        """
        self.key = key
        self.name = name
        self.left_child = left_child
        self.middle_child = middle_child
        self.right_child = right_child
        if self.has_right_child():
            self.right_child.parentNode = self
        if self.has_middle_child():
            self.middle_child.parentNode = self
        if self.has_left_child():
            self.left_child.parentNode = self
