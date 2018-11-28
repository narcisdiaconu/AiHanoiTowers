from base import *
import hillclimbing_ai
import random_ai
import avg_calculator
import time

# avg_calculator.calculate(7, 7, hillclimbing_ai.HillClimbingAI(None), "avg/hillclimb_ai - avg1.txt", 1000)
# avg_calculator.calculate(7, 7, random_ai.RandomAI(None), "avg/random_ai - avg1.txt", 1000)

ai = hillclimbing_ai.HillClimbingAI(None)
#ai = random_ai.RandomAI(None)
start = time.perf_counter()
avg = avg_calculator.average(3, 6, ai, sample_size=100, number_of_attempts=500, tolerance=4, return_fails=True)
elapsed = time.perf_counter() - start
print("avg: {}  time: {}".format(avg, elapsed)) 