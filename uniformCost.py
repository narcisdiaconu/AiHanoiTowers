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
        self.history = [hanoi.state]

    def run(self):
        bfs_list = [(self.hanoi, 0)]
        while len(bfs_list) > 0:
            self.no_transitions +=1
            accesible_state = getAccesibleStates(bfs_list[0][0], self.history)
            for state in accesible_state:
                self.states.append((state.state, bfs_list[0][1] + 1))
                self.history.append(state.state)
                if state.end():
                    self.result = [i for i in self.states if i[0] == state.state]
                    return state
                bfs_list.append((state, bfs_list[0][1] + 1))
            del bfs_list[0]

if __name__ == "__main__":
    h = Hanoi(4, 4)
    uc = UniformCost(h)
    uc.run()
    print(uc.result)