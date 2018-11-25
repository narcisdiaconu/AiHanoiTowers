from base import *
import hillclimbing_ai
import random_ai
import avg_calculator

avg_calculator.calculate(6, 6, hillclimbing_ai.HillClimbingAI(None), "avg/hillclimb_ai - avg.txt", 1000)
avg_calculator.calculate(6, 6, random_ai.RandomAI(None), "avg/random_ai - avg.txt", 1000)