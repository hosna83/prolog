from typing import Self
from treelib import Tree, Node
node = Node()
#print(type(node.successors()))

class Traversal:
    def __init__(self: Self, tree: Tree):
        self.tree = tree
        self.nodes = []

    def inorder_traversal(self: Self, root: Node=None): 
        
        if root:
            successors = root.successors(tree_id=self.tree.identifier)
            if len(successors) > 0:
                left = self.tree.get_node(successors[0])
                yield self.inorder_traversal(left)
                yield root.data
                remainings = self.tree.get_node(successors[1:])
                for remaining in remainings:
                    yield self.inorder_traversal(remaining)

    
                



# def main():
#     tree = Tree()
#     node1 = Node("HOSNA")
#     tree.add_node(node1)
#     node = Node(data="242")
#     tree.add_node(node, parent=node1)
#     id = node.identifier
#     node: Node = tree.get_node(id)
#     print(tree.root)
#     print(tree.get_node(node1.successors(tree_id=tree.identifier)[0]).data)


# if __name__ == "__main__":
#     main() 