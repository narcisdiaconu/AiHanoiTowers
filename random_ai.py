from generic_ai import *
from base import *
import random

class RandomAI(GenericAI):
    def choose(self, hanoi, valid_moves):
        return valid_moves[random.randint(0, len(valid_moves) - 1)]