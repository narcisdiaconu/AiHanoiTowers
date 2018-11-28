from generic_ai import *
from base import *
import random


def fitness(hanoi):
    sum = 0
    for (disk_index, disk) in enumerate(hanoi.tower(hanoi.poz_final)):
        if (hanoi.disks_count - disk_index - 1) == disk:
            sum += 1
    return sum

class HillClimbingAI(GenericAI):
    def choose(self, hanoi, valid_moves):
        random.shuffle(valid_moves)
        best_fitness = -1

        for valid_move in valid_moves:
            hanoi_copy = hanoi.copy().transition(valid_move[0], valid_move[1])
            current_fitness = fitness(hanoi_copy)
            if current_fitness > best_fitness:
                best_move = valid_move
                best_fitness = current_fitness

        if best_fitness < fitness(hanoi):
            raise ZeroAvailableMoves()
        else:
            return best_move