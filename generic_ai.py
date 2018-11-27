import base

class ZeroAvailableMoves(Exception):
    pass

class GenericAI:
    def __init__(self, hanoi):
        self.hanoi = hanoi

    def choose(self, hanoi, valid_moves):
        raise NotImplementedError()

    def play(self, moves_count=1):
        while moves_count > 0 and not self.hanoi.end():
            valid_moves = self.hanoi.valid_moves(new_states_only=True)
            if valid_moves:
                try:
                    chosen_move = self.choose(self.hanoi, valid_moves)
                    self.hanoi.transition(chosen_move[0], chosen_move[1])
                except ZeroAvailableMoves:
                    return False
                moves_count -= 1
            else:
                return False
        return self.hanoi.end()

    def solution(self, number_of_attempts=1000, tolerance=7):
        moves_count = (2 ** self.hanoi.disks_count - 1) * tolerance
        for i in range(number_of_attempts):
            self.hanoi.init()
            result = self.play(moves_count)
            if result:
                return True
        return False
