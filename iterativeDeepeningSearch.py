from base import *

def getAccesibleStates(hanoi, history):
    accesibleStates = []
    for move in hanoi.valid_moves(True):
        hanoiCopy = hanoi.copy()
        hanoiCopy.transition(move[0], move[1])
        if hanoiCopy.state not in history:
            accesibleStates.append(hanoiCopy.copy())
    return accesibleStates

class Tree:
    def __init__(self, hanoi):
        self.node = hanoi
        self.childs = []
    
    def set_childs(self, history):
        for item in getAccesibleStates(self.node, history):
            self.childs.append(Tree(item))

    def __str__(self, level=1):
        s = ""
        s+= self.node.state.__str__() + '\n'
        for child in self.childs:
            s+= '\t' * level + child.__str__(level+1)
        return s

class IterativeDeepeningSearch:
    def __init__(self, hanoi, startHeight):
        self.hanoi = hanoi
        self.height = startHeight
        self.result = 0
        self.count_moves = 0
        self.tree = Tree(hanoi)
        self.tree.set_childs([])
        self.history = [hanoi.state]
        self.no_transitions = 0
        self.result_moves = 0
        
    def run(self, hanoi, depth):
        if self.result != 0:
            return 0
        self.no_transitions +=1
        if hanoi.end():
            self.result = hanoi
            self.result_moves = self.count_moves
            return 0
        elif depth == self.height:
            return 0
        available_states = getAccesibleStates(hanoi, self.history)
        for state in available_states:
            self.history.append(state.state_copy())
        for state in available_states:
            self.count_moves +=1
            self.run(state.copy(), depth+1)
            self.count_moves -=1
        for i in range(len(available_states)):
            self.history.pop()
    
    def runTree(self, tree, depth):
        if self.result != 0:
            return 0;
        if tree.node.end():
            self.result = tree.node
            self.result_moves = self.count_moves
            return 0
        if depth == self.height:
            return 0
        if tree.childs == []:
            tree.set_childs(self.history)
        for child in tree.childs:
            self.history.append(child.node.state_copy())
            self.count_moves +=1
            self.runTree(child, depth+1)
            self.count_moves -=1
        for i in range(len(tree.childs)):
            self.history.pop()

    def getResult(self):
        while self.result == 0:
            self.no_transitions = 0
            self.run(self.hanoi, 0)
            self.height += 1
        return (self.result.state, self.result_moves, self.no_transitions)

if __name__ == "__main__":
    h = Hanoi(3, 6, 0, 2)
    ids = IterativeDeepeningSearch(h, 5)
    print(ids.getResult())