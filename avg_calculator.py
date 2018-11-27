from base import *

def average(towers_count, disks_count, ai, sample_size=1000, number_of_attempts=1000, tolerance=4, return_fails=False):
    hanoi = Hanoi(towers_count, disks_count)
    ai.hanoi = hanoi

    moves_sum = 0
    success_count = 0

    for k in range(sample_size):
        result = ai.solution(number_of_attempts=number_of_attempts, tolerance=tolerance)
        if result:
            moves_sum += len(hanoi.moves_history)
            success_count += 1
    
    avg = moves_sum / success_count if success_count > 0 else -1
    fails = sample_size - success_count
    return (avg, fails) if return_fails else avg

def calculate(towers_max_count, disks_max_count, ai, filename, sample_size=1000, number_of_attempts=1000, tolerance=4):
    string = ""

    for i in range(3, towers_max_count):
        for j in range(3, disks_max_count):
            avg, fails = average(i, j, ai, sample_size=sample_size, number_of_attempts=number_of_attempts, return_fails=True)

            string += "towers: " + str(i) + " disks: " + str(j) + "\n"
            string += "avg: " + str(avg) + "\n"
            string += "failed: " + str(fails) + "\n\n"

    fd = open(filename, "w")   
    fd.write(string)
    fd.close()