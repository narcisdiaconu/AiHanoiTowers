from base import *
import hillclimbing_ai
import random_ai
import avg_calculator
import time

# avg_calculator.calculate(5, 5, hillclimbing_ai.HillClimbingAI(None), "avg/hillclimb_ai - avg.txt", sample_size=100, number_of_attempts=100, tolerance=4)
# print("done")
# avg_calculator.calculate(5, 5, random_ai.RandomAI(None), "avg/random_ai - avg.txt", sample_size=100, number_of_attempts=100, tolerance=4)
# print("done")

ai = hillclimbing_ai.HillClimbingAI(None)
#ai = random_ai.RandomAI(None)
for i in range(3, 8): 
    metrics = avg_calculator.average(3, 6, ai, sample_size=100, number_of_attempts=100, tolerance=i)
    print("avg: {}  attempts: {}  fails: {}  time: {}".format(metrics.avg_length, metrics.avg_attempts, metrics.fails, metrics.duration))
