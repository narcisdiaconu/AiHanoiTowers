from base import *
import hillclimbing_ai
import random_ai
import avg_calculator

# avg_calculator.calculate(7, 7, hillclimbing_ai.HillClimbingAI(None), "avg/hillclimb_ai - avg.txt", 1000)
# avg_calculator.calculate(7, 7, random_ai.RandomAI(None), "avg/random_ai - avg.txt", 1000)

hanoi = Hanoi(3, 5)
hc = hillclimbing_ai.HillClimbingAI(hanoi)
print(hc.solution())
print(hanoi)