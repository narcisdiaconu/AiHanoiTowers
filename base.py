class Hanoi:
    def __init__(self, towers_count, disks_count):
        self.towers_count = towers_count
        self.disks_count = disks_count
        self.init()

    def init(self):
        self.state = [0] * self.disks_count

    def transition(self, pos_from, pos_to):
        if self.is_valid_move(pos_from, pos_to):
            for i in range(len(self.state)):
                 if self.state[i] == pos_from:
                    self.state[i] = pos_to
                    break


    def is_valid_move(self, pos_from, pos_to):
        if pos_from == pos_to:
            return False
        elif not (0 <= pos_from < self.disks_count) or not (0 <= pos_to < self.disks_count):
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
        if self.state[0] == 0:
            return False
        else :
            for i in range(self.disks_count-1):
                if self.state[i] != self.state[i+1]:
                    return False
        return True

    def copy(self):
        return [i for i in self.state]