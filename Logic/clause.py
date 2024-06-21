from typing import Self

class Clause:
    parameters: list
    name: str
    condition: list
    def __init__(self: Self):
        #self.parameters = 
        pass

    def set_parameters(self: Self, parameter):
        self.parameters.append(parameter)
    
    def __str__(self: Self):
        if self.condition is None:
            return f"{self.name.upper()}()"
        

    # class Interpreter:
    #     def __init__(self: Self):
    #         pass
        
    #     def interpret(self: Self, tree: Tree):
    #         self.tree = tree
    #         match self.tree.root.data:
    #             case "IMPLY":
    #                 self.handle_imply()
    #             case "QUESTION":
    #                 self.handle_question()
    #             case "FUNCTOR":
    #                 self.handle_functor()
    #             case _:
    #                 raise Exception("Unknown root data")

    #     def handle_imply(self: Self):
    #         # Implement the logic to handle the IMPLY node
    #         pass
        
    #     def handle_question(self: Self):
    #         # Implement the logic to handle the QUESTION node
    #         pass
        
    #     def handle_functor(self: Self):
    #         # Implement the logic to handle the FUNCTOR node
    #         pass
