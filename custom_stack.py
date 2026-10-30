class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
        
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None


def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    # TODO: Implement stack logic to validate parentheses
    opening_stack = Stack()
    valid_pairs = ["()", "{}", "[]"]
    
    for char in s:
        if char in "({[":
            opening_stack.push(char)  # add the opening to the stack
        elif char in ")}]":
            opening = opening_stack.peek()  # look up the last opening
            if not opening or opening + char not in valid_pairs: 
                #  If there is no opening for this closing, or the opening and this closing are not balanced...
                return False
            else:
                #  Otherwise, it's a valid pair, and we can pop the opening off
                opening_stack.pop()
    
    #  At this point, the opening stack will have been emptied if everything was a valid pair
    return opening_stack.is_empty()