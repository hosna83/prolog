from typing import Self
from prolog.Parser.tokenizer import Tokenizer
from treelib import Node, Tree
import uuid

class Parser:
    def __init__(self: Self) -> None:
        self.tokenizer = Tokenizer()
    
    def set_text(self, text):
        self.text = text
        
    #TODO: Ask about this with hosna
    def parse(self: Self):
        pre_tokens = []
        for token in self.tokenizer.tokenize(self.text):
            if (
                token[0] != "L_PARENTHES" and
                token[0] != "R_PARENTHES" and
                token[0] != "SPACE"
            ):
                pre_tokens.append(token)

        self.tokens = []
        self.tokens.append(pre_tokens[0])
        for i in range(1, len(pre_tokens) - 1):
            if (
            pre_tokens[i][0] == "COMMA" and
            pre_tokens[i - 1][0] == "ID" and
            pre_tokens[i + 1][0] == "ID"
            ):
                continue
            self.tokens.append(pre_tokens[i])
        self.tokens.append(pre_tokens[-1])
        self.parse_tree()
        

    def parse_tree(self: Self):
        print(self.tokens)
        self.tree = Tree()
        self.kinds = [i for i, j in self.tokens]
        self.values = [j for i, j in self.tokens]
        if "IMPLY" in self.kinds:
            root = Node(data="<-", tag="IMPLY")
            self.tree.add_node(root)
            self.current_parent = root
            index = self.kinds.index("IMPLY")
            self.parse_subtree(self.kinds[:index], self.values[:index])
            self.parse_subtree(self.kinds[index + 1:], self.values[index + 1:])
            
        elif "QUESTION" in self.kinds:
            root = Node(data="?", tag="QUESTION", identifier=str(uuid.uuid4()))
            self.tree.add_node(root)
            self.current_parent = root
            index = self.kinds.index("QUESTION")
            self.parse_subtree(self.kinds[:index], self.values[:index])
            self.parse_subtree(self.kinds[index + 1:], self.values[index + 1:])
        
        elif "FUNCTOR" in self.kinds:
            index = self.kinds.index("QUESTION")
            root = Node(data=self.values[index], tag="FUNCTOR", identifier=str(uuid.uuid4()))
            self.tree.add_node(root)
            self.current_parent = root
            self.parse_subtree(self.kinds[:index], self.values[:index])
            self.parse_subtree(self.kinds[index + 1:], self.values[index + 1:])
        #            <-
            #     ,              ,
            # functor  =       functor =
            # * /               * / 
            # +-                +-
            # id                 id 

    def parse_subtree(self: Self, kinds: list, values: list):
        if len(kinds) == 1 and len(values) == 1:
            node = Node(data=values[0], tag=kinds[0], identifier=str(uuid.uuid4()))
            self.tree.add_node(node, parent=self.current_parent)
        else:
            if "COMMA" in kinds:
                node = Node(data=",", tag="COMMA", identifier=str(uuid.uuid4()))
                self.tree.add_node(node, parent=self.current_parent)
                self.current_parent = node
                index = kinds.index("COMMA")
                self.parse_subtree(kinds[:index], values[:index])
                self.parse_subtree(kinds[index + 1:], values[index + 1:])
            elif "FUNCTOR" in kinds:
                index = kinds.index("FUNCTOR")
                node = Node(data=values[index], tag="FUNCTOR", identifier=str(uuid.uuid4()))
                self.tree.add_node(node, parent=self.current_parent)
                self.current_parent = node
                self.parse_subtree(kinds[:index], values[:index])
                self.parse_subtree(kinds[index + 1:], values[index + 1:])
            elif "ASSIGN" in kinds:
                index = kinds.index("ASSIGN")
                node = Node(data=values[index], tag="ASSIGN", identifier=str(uuid.uuid4()))
                self.tree.add_node(node, parent=self.current_parent)
                self.current_parent = node
                self.parse_subtree(kinds[:index], values[:index])
                self.parse_subtree(kinds[index + 1:], values[index + 1:])

def main():
    syntax = "Father1(x, y)  <- Sister(x, y), s=2;"
    syx = "father(x,y)?"
    parser = Parser()
    parser.set_text(syx)
    parser.parse()
    parser.tree._Tree__print_backend()

if __name__ == "__main__":
    main()