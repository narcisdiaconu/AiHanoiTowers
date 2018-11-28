from base import *
from iterativeDeepeningSearch import getAccesibleStates
from iterativeDeepeningSearch import Tree

class UniformCost:
    def __init__(self, hanoi):
        self.hanoi = hanoi
        self.states = [[hanoi.state,0]]
        self.result = 0
        self.tree = 0
        self.no_transitions = 0

    def run(self):
        bfs_list = [(self.hanoi, 0)]
        while len(bfs_list) > 0:
            self.no_transitions +=1
            accesible_state = getAccesibleStates(bfs_list[0][0], [])
            for state in accesible_state:
                added = False
                if state.state not in [i[0] for i in self.states]:
                    self.states.append((state.state, bfs_list[0][1] + 1))
                    added = True
                if state.end():
                    self.result = [i for i in self.states if i[0] == state.state]
                    return state
                if added == True:    
                    bfs_list.append((state, bfs_list[0][1] + 1))
            del bfs_list[0]

if __name__ == "__main__":
    h = Hanoi(4, 4, 1, 2)
    uc = UniformCost(h)
    uc.run()
    print(uc.result)