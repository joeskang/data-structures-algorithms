"""

    generic node class for various data structures

"""


class Node:

    def __init__(self, value=None, parent=None, child=None, set_pos=None):
        self.parent = parent
        self.child = child
        self.value = value

        if set_pos:
            self.position = set_pos

    def __eq__(self, other):
        return self.value == other.value

    def __iter__(self):

        yield self.value if self.value else 0

        if self.child:
            yield from self.child.__iter__()

    def set_child(self, value):
        self.child = Node(value, parent=self)

    def set_parent(self, value):
        self.parent = Node(value, child=self)


class TreeNode(Node):

    def __init__(self, value=None, parent=None, child=None, set_pos=None, left=None, right=None):
        super().__init__(value=value, parent=parent, child=child, set_pos=set_pos)
        self.left = left
        self.right = right

    def __iter__(self):

        if self.left:
            yield from self.left.__iter__()

        yield self.value

        if self.right:
            yield from self.right.__iter__()

