from base import *
import hillclimbing_ai
import random_ai
import avg_calculator
import time

avg_calculator.calculate(hillclimbing_ai.HillClimbingAI(None), "instante - Copy.txt", "avg/hillclimb_ai - avg4.txt", sample_size=1000, number_of_attempts=100, tolerance=4)
avg_calculator.calculate(random_ai.RandomAI(None), "instante - Copy.txt", "avg/random_ai - avg4.txt", sample_size=1000, number_of_attempts=100, tolerance=4)
