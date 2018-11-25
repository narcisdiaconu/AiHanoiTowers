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
        
    def run(self, hanoi, depth):
        if hanoi.end():
            self.result = hanoi
            self.result_moves = self.count_moves
            return 0
        elif depth == self.height:
            return 0
        for state in getAccesibleStates(hanoi, self.history):
            if self.result != 0:
                break
            self.history.append(state.copy())
            self.count_moves +=1
            self.run(state.copy(), depth+1)
            self.count_moves -=1
            self.history.pop()
    
    def runTree(self, tree, depth):
        if tree.node.end():
            self.result = tree.node
            self.result_moves = self.count_moves
            return 0
        elif depth == self.height:
            return 0
        for child in tree.childs:
            self.history.append(child.node.state_copy())
            self.count_moves +=1
            if child.childs == []:
                child.set_childs(self.history)
            self.runTree(child, depth+1)
            self.count_moves -=1
        for i in range(len(tree.childs)):
            self.history.pop()

    def getResult(self):
        while self.result == 0:
            # self.runTree(self.tree, 0)
            self.run(self.hanoi, 0)
            self.height += 1
            # print(self.tree)
            # print(self.height)
        # print(self.tree)
        return (self.result.state, self.result_moves)

if __name__ == "__main__":
    h = Hanoi(3,4)
    ids = IterativeDeepeningSearch(h, 3)
    print(ids.getResult())