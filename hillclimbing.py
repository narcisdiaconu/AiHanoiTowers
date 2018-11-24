from base import *
import random

#PLACEHOLDER
class HanoiWrapper(Hanoi):
    def init(self):
        super().init()
        self.state_history = []
        self.moves_history = []

    def tower(self, tower_index):
       return [disk for disk in range(self.disks_count) if self.disk_position(disk) == tower_index][::-1]

    def disk_position(self, disk_index):
        return self.state[disk_index]

    def valid_moves(self, new_states_only=False):
        valid_moves = [(i, j) for i in range(self.towers_count) for j in range(self.towers_count) if self.is_valid_move(i,j)]
        if new_states_only:
            for (i, valid_move) in enumerate(valid_moves):
                hanoi_copy = self.copy()
                hanoi_copy.transition(valid_move[0], valid_move[1])
                if hanoi_copy.state in self.state_history:
                    del valid_moves[i]
        return valid_moves

    def copy(self):
        copy = HanoiWrapper(self.towers_count, self.disks_count)
        copy.state = self.state_copy()
        return copy

    def state_copy(self):
        return [i for i in self.state]

    def transition(self, pos_from, pos_to):
        self.state_history += [self.state_copy()]
        self.moves_history += [(pos_from, pos_to)]
        super().transition(pos_from, pos_to)

    def __str__(self):
        s = ""
        for tower in range(self.towers_count):
            s += str(tower) + ": " + str(self.tower(tower)) + "\n"
        return s

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
            hanoi_copy = self.hanoi.copy()
            hanoi_copy.transition(valid_move[0], valid_move[1])
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
                self.hanoi.transition(chosen_move[0], chosen_move[1])
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
        
          
h = HanoiWrapper(3, 6)
hc = HillClimbing(h)

iterations = 1000
moves_sum = 0
success_count = 0
for i in range(iterations):
    result = hc.solution()
    if result:
        moves_sum += len(h.moves_history)
        success_count += 1

print("avg: " + str(moves_sum / success_count))
print("failed: " + str(iterations - success_count))

print(h.state)