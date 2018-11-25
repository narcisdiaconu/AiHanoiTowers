import random
from base import *

class RandomAI:
    def __init__(self, hanoi):
        self.hanoi = hanoi

    def choose(self, valid_moves):
        return valid_moves[random.randint(0, len(valid_moves) - 1)]

    def play(self, moves_count = 100):
        while moves_count > 0 and not self.hanoi.end():
            valid_moves = self.hanoi.valid_moves(new_states_only=True)
            if valid_moves:
                chosen_move = self.choose(valid_moves)
                self.hanoi.transition(chosen_move[0], chosen_move[1])
            else:
                 return False
            moves_count -= 1
        return self.hanoi.end()

    def solution(self, iterations=100):
        moves_count = (2 ** self.hanoi.disks_count - 1) * 3
        for i in range(iterations):
            self.hanoi.init()
            result = self.play(moves_count)
            if result:
                return True
        return False


string = ""

for i in range(3, 6):
    for j in range(3, 6):
        h = Hanoi(i, j)
        rai = RandomAI(h)

        iterations = 1000
        moves_sum = 0
        success_count = 0

        for k in range(iterations):
            result = rai.solution()
            if result:
                moves_sum += len(h.moves_history)
                success_count += 1
        
        string += "towers: " + str(i) + " disks: " + str(j) + "\n"
        string += "avg: " + str(moves_sum / success_count) + "\n"
        string += "failed: " + str(iterations - success_count) + "\n\n"

fd = open("random-stats.txt", "w")   
fd.write(string)
fd.close()