from base import *
import time


def average(towers_count, disks_count, ai, sample_size=1000, number_of_attempts=1000, tolerance=4):
    hanoi = Hanoi(towers_count, disks_count)
    ai.hanoi = hanoi

    moves_sum = 0
    success_count = 0

    start = time.perf_counter()

    for k in range(sample_size):
        result = ai.solution(
            number_of_attempts=number_of_attempts, tolerance=tolerance)
        if result:
            moves_sum += len(hanoi.moves_history)
            success_count += 1

    duration = time.perf_counter() - start
    avg = moves_sum / success_count if success_count > 0 else -1
    fails = sample_size - success_count
    return avg, fails, duration


def calculate(towers_max_count, disks_max_count, ai, filename, sample_size=1000, number_of_attempts=1000, tolerance=4):
    string = "sample_size: {}  number_of_attempts: {}  tolerance: {}".format(
        sample_size, number_of_attempts, tolerance)

    for i in range(3, towers_max_count + 1):
        for j in range(3, disks_max_count + 1):
            avg, fails, duration = average(i, j, ai, sample_size=sample_size, number_of_attempts=number_of_attempts)

            string += "towers: {}  disks: {}\n".format(i, j)
            string += "avg: {}\n".format(avg)
            string += "failed: {}\n".format(fails)
            string += "duration: {}\n".format(duration)

    fd = open(filename, "w")
    fd.write(string)
    fd.close()
