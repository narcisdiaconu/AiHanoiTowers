class Hanoi:
    def __init__(self, towers_count, disks_count, poz_init = 0, poz_final = -1):
        self.towers_count = towers_count
        self.disks_count = disks_count
        self.poz_init = poz_init;
        self.poz_final = poz_final - 1;
        if poz_final == -1:
            self.poz_final = towers_count - 1;
        self.init()

    def init(self):
        self.state_history = []
        self.moves_history = []
        self.state = [self.poz_init - 1] * self.disks_count

    def tower(self, tower_index):
       return [disk for disk in range(self.disks_count) if self.disk_position(disk) == tower_index][::-1]

    def disk_position(self, disk_index):
        return self.state[disk_index]

    def transition(self, pos_from, pos_to):
        self.state_history += [self.state_copy()]
        self.moves_history += [(pos_from, pos_to)]
        if self.is_valid_move(pos_from, pos_to):
            for i in range(len(self.state)):
                 if self.state[i] == pos_from:
                    self.state[i] = pos_to
                    break
        return self

    def valid_moves(self, new_states_only=False):
            valid_moves = [(i, j) for i in range(self.towers_count) for j in range(self.towers_count) if self.is_valid_move(i,j)]
            if new_states_only:
                for (i, valid_move) in enumerate(valid_moves):
                    hanoi_copy = self.copy()
                    hanoi_copy.transition(valid_move[0], valid_move[1])
                    if hanoi_copy.state in self.state_history:
                        del valid_moves[i]
            return valid_moves
    
    def is_valid_move(self, pos_from, pos_to):
        if pos_from == pos_to:
            return False
        elif not (0 <= pos_from < self.towers_count) or not (0 <= pos_to < self.towers_count):
            return False
        else:
            found = False
            for disk_pos in self.state:
                if disk_pos == pos_from:
                    found = True
            if found == False:
                return False

            if self.top_disk(pos_to) == -1:
                return True

            if self.top_disk(pos_from) > self.top_disk(pos_to):
                return False
        return True

    def top_disk(self, pos):
        for i, disk_pos in enumerate(self.state):
            if disk_pos == pos:
                return i
        return -1

    def end(self):
        if self.state[0] != self.poz_final:
            return False
        else :
            for i in range(self.disks_count-1):
                if self.state[i] != self.state[i+1]:
                    return False
        return True

    def copy(self):
        copy = Hanoi(self.towers_count, self.disks_count, self.poz_init + 1, self.poz_final + 1)
        copy.state = self.state_copy()
        copy.state_history = [i for i in self.state_history]
        return copy

    def state_copy(self):
        return [i for i in self.state]

    def __str__(self):
        s = ""
        for tower in range(self.towers_count):
            s += str(tower + 1) + ": " + str(self.tower(tower)) + "\n"
        return s