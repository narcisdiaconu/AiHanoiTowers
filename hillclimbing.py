from base import *
import random

#PLACEHOLDER
class HanoiWrapper(Hanoi):
    def tower(self, tower_index):
       return [disk for disk in range(self.disks_count) if self.disk_position(disk) == tower_index][::-1]

    def disk_position(self, disk_index):
        return self.state[disk_index]

    def valid_moves(self):
        return [(i, j) for i in range(self.towers_count) for j in range(self.towers_count) if self.is_valid_move(i,j)]

    def copy(self):
        copy = HanoiWrapper(self.towers_count, self.disks_count)
        copy.state = self.state_copy()
        return copy

    def state_copy(self):
        return [i for i in self.state]

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
        
        iterations = 100
        while iterations > 0 and not hanoi.end():
            valid_moves = self.hanoi.valid_moves()
            fitnesses = [] 
            for valid_move in valid_moves:
                hanoi_copy = self.hanoi.copy()
                hanoi_copy.transition(valid_move[0], valid_move[1])
                fitnesses += [fitness(hanoi_copy)]
            random.shuffle(fitnesses)
            chosen_move = valid_moves[self.choose(fitnesses)]
            self.hanoi.transition(chosen_move[0], chosen_move[1])
            print(self.hanoi)
            iterations -= 1

    def choose(self, fitnesses):
        maxarg = 0
        maxval = fitnesses[0]
        for i, fitness in enumerate(fitnesses):
            if fitness > maxval:
                maxarg = i
                maxval = fitness
        return maxarg
            

h = HanoiWrapper(5,5)

HillClimbing(h)