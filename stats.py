from base import *
import hillclimbing_ai
import random_ai
import a_star

import avg_calculator
import a_star_testing

#avg_calculator.calculate(hillclimbing_ai.HillClimbingAI(None), "instante - Copy.txt", "avg/hillclimb_ai - avg4.txt", sample_size=1000, number_of_attempts=100, tolerance=4)
#avg_calculator.calculate(random_ai.RandomAI(None), "instante - Copy.txt", "avg/random_ai - avg4.txt", sample_size=1000, number_of_attempts=100, tolerance=4)
a_star_testing.calculate(a_star.AStar(None), "instante - Copy.txt", "avg/a_star_ai - avg.txt", sample_size=1000)