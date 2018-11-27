from base import *
import hillclimbing_ai
import random_ai
import avg_calculator

# avg_calculator.calculate(7, 7, hillclimbing_ai.HillClimbingAI(None), "avg/hillclimb_ai - avg1.txt", 1000)
# avg_calculator.calculate(7, 7, random_ai.RandomAI(None), "avg/random_ai - avg1.txt", 1000)

ai = hillclimbing_ai.HillClimbingAI(None)
#ai = random_ai.RandomAI(None)
print(avg_calculator.average(5, 3, ai, sample_size=1000, number_of_attempts=2000, tolerance=8, return_fails=True))