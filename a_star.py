from base import *
from iterativeDeepeningSearch import getAccesibleStates

class AStar():
    def __init__(self, hanoi):
        self.hanoi = hanoi

    def h_score(self, hanoi):
        return len(hanoi.tower(hanoi.poz_final))

    def largest_f_score(self, accesible_hanois, g_score):
        accesible_states = sorted(accesible_hanois, key=lambda x: g_score[x.stable_state] + self.h_score(x))
        return accesible_states[-1]

    def play(self):
        closed_set = []
        open_set = [self.hanoi]

        came_from = dict()
        g_score = dict()

        g_score[self.hanoi.stable_state] = 0

        while open_set:
            current = self.largest_f_score(open_set, g_score)
            # print(current)
            if current.end():
                return current #reconstruct

            open_set.remove(current)
            closed_set.append(current)

            for neighbor in getAccesibleStates(current, []):
                if neighbor.state in [hanoi.state for hanoi in closed_set]:
                    continue
                
                tentative_g_score = g_score[current.stable_state] + 1

                if neighbor.state not in [hanoi.state for hanoi in open_set]:
                    open_set.append(neighbor)
                else:
                    continue

                came_from[neighbor.stable_state] = current.stable_state
                g_score[neighbor.stable_state] = tentative_g_score
                


hanoi = Hanoi(3, 5)
astar = AStar(hanoi)

hanoi = astar.play()

print(len(hanoi.moves_history))
