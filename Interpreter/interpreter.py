from typing import Self
from treelib import Tree, Node
from prolog.Interpreter.traversal import Traversal

class Interpreter:
    def __init__(self: Self):
        pass
    
    def interpret(self: Self, tree: Tree):
        self.tree = tree
        match self.tree.root.data:
            case "IMPLY":
                pass
            case "QUESTION":
                pass
            case "FUNCTOR":
                pass
            case _:
                raise Exception()
