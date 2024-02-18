init python:

    class Node():
        def __init__(self, message, character):
            self.left = None
            self.right = None
            self.message = message
            self.character = character


        # INSERT METHOD FOR THE NODE CLASS. SHOULD INSERT A NEW NODE.
        def insert(self, node):
            #self.left = Node(node.message, node.character)
        
            if self.message: #not empty node
                if self.left is None:
                    self.left = Node(node.message, node.character)
                    renpy.say(nvl_narrator, "Inserted left branch into: " + self.message)
                else:
                    self.right = Node(node.message, node.character)
                    renpy.say(nvl_narrator, "Inserted right branch: " + self.message)
            else:
                self.message = node.message
                self.character = node.character

        def isMenu(self):
            if (self.right and self.left):
                return True
            else:
                return False
    

        
