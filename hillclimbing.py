from base import *
import random

def fitness(hanoi):
    big_disk_position = hanoi.disk_position(hanoi.disks_count - 1)
    if big_disk_position == 0:
        return 0
    else:
        sum = 0
        for (disk_index, disk) in enumerate(hanoi.tower(big_disk_position)):
            if (hanoi.disks_count - disk_index - 1) == disk:
                sum += 1
        return sum

class HillClimbing:
    def __init__(self, hanoi):
        self.hanoi = hanoi

    def choose(self, valid_moves):
        random.shuffle(valid_moves)
        best_fitness = -1
        for valid_move in valid_moves:
            hanoi_copy = self.hanoi.copy().transition(valid_move[0], valid_move[1])
            current_fitness = fitness(hanoi_copy)
            if current_fitness > best_fitness:
                best_move = valid_move
                best_fitness = current_fitness
        return best_move

    def play(self, moves_count=100):
        while moves_count > 0 and not self.hanoi.end():
            valid_moves = self.hanoi.valid_moves(True)
            if valid_moves:
                chosen_move = self.choose(valid_moves)
                hanoi_copy = self.hanoi.copy().transition(chosen_move[0], chosen_move[1])
                if fitness(hanoi_copy) >= fitness(self.hanoi):
                    self.hanoi.transition(chosen_move[0], chosen_move[1])
                else:
                    return False
                moves_count -= 1
            else:
                return False
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

for i in range(3, 7):
    for j in range(3, 7):
        h = Hanoi(i, j)
        hc = HillClimbing(h)

        iterations = 1000
        moves_sum = 0
        success_count = 0

        for k in range(iterations):
            result = hc.solution()
            if result:
                moves_sum += len(h.moves_history)
                success_count += 1
        
        string += "towers: " + str(i) + " disks: " + str(j) + "\n"
        string += "avg: " + str(moves_sum / success_count) + "\n"
        string += "failed: " + str(iterations - success_count) + "\n\n"

fd = open("hillclimb-stats.txt", "w")   
fd.write(string)
fd.close()