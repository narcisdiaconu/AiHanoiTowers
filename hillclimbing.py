from base import *

#PLACEHOLDER
class HanoiWrapper(Hanoi):
    def tower(self, tower_index):
        return [(self.towers_count - disk_size) for disk_size, disk_pos in enumerate(reversed(self.state)) if disk_pos == tower_index]

    def disk_position(self, disk_index):
        return self.state[disk_index]

    def valid_moves(self):
        return [(i, j) for i in range(self.towers_count) for j in range(self.towers_count) if self.is_valid_move(i,j)]

def fitness(hanoi):
    big_disk_position = hanoi.disk_position(hanoi.disks_count - 1)
    if big_disk_position == 0:
        return 0
    else:
        return sum(hanoi.tower(big_disk_position))

class HillClimbing:
    def __init__(self, hanoi):
        self.hanoi = hanoi

h = HanoiWrapper(4,5)
h.transition(0, 2)

print(h.valid_moves())