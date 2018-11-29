from base import *
from iterativeDeepeningSearch import getAccesibleStates
from hillclimbing_ai import fitness
class AStar():
    def __init__(self, hanoi):
        self.hanoi = hanoi

    def h_score(self, hanoi):
        return len(hanoi.tower(hanoi.poz_final))

    def largest_f_score(self, accesible_hanois, g_score):
        accesible_states = sorted(accesible_hanois, key=lambda x: g_score[x.stable_state] + self.h_score(x))
        return accesible_states[-1]

    def reconstruct(self, came_from, current):
        current = current.stable_state
        path = [current]
        while current in came_from.keys():
            current = came_from[current]
            path.append(current)
        path.reverse()
        # for i in range(len(path)-1, 0, -1):
        #     for j in range(0, i - 1):
        #         hanoi = self.hanoi.copy()
        #         hanoi.state = list(path[j])
        #         if path[i] in [hanoi.stable_state for hanoi in getAccesibleStates(hanoi,[])]:
        #             print(str(i) + " <- " + str(j))

        return path

    def solution(self):
        closed_set = []
        open_set = [self.hanoi]
        self.evaluated_states_count = 1

        came_from = dict()
        g_score = dict()

        g_score[self.hanoi.stable_state] = 0

        while open_set:
            current = self.largest_f_score(open_set, g_score)
            if current.end():
                return self.reconstruct(came_from, current)

            open_set.remove(current)
            closed_set.append(current)
            self.evaluated_states_count += 1

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