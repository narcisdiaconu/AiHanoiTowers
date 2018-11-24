from base import *

def getAccesibleStates(hanoi):
    accesibleStates = []
    for move in hanoi.valid_moves(new_states_only=True):
        hanoiCopy = hanoi.copy()
        state_copy = []
        for item in hanoi.state_history:
            state_copy.append(item)
        hanoiCopy.state_history = state_copy
        hanoiCopy.transition(move[0], move[1])
        accesibleStates.append(hanoiCopy)
    return accesibleStates

class IterativeDeepeningSearch:
    def __init__(self, hanoi, startHeight):
        self.hanoi = hanoi
        self.height = startHeight
        self.result = 0
        
    def run(self, hanoi, height):
        if hanoi.end():
            self.result = hanoi
            return 0
        elif height == self.height:
            return 0
        for state in getAccesibleStates(hanoi):
            if self.result != 0:
                break
            self.run(state.copy(), height+1)
    
    def getResult(self):
        while self.result == 0:
            self.run(self.hanoi, 0)
            self.height += 1
        return self.result.state

h = Hanoi(10,4)

ids = IterativeDeepeningSearch(h, 5)
print(ids.getResult())