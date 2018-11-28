from base import *
import time

class SampleStats:
    def __init__(self, avg_length, avg_attempts, fails, duration):
        self.avg_length = avg_length
        self.avg_attempts = avg_attempts
        self.fails = fails
        self.duration = duration

def average(towers_count, disks_count, ai, sample_size=1000, number_of_attempts=1000, tolerance=4):
    hanoi = Hanoi(towers_count, disks_count)
    ai.hanoi = hanoi

    moves_sum = 0
    attempts_sum = 0
    success_count = 0

    start = time.perf_counter()

    for k in range(sample_size):
        attempts = ai.solution(number_of_attempts=number_of_attempts, tolerance=tolerance)
        if attempts >= 0:
            moves_sum += len(hanoi.moves_history)
            attempts_sum += attempts
            success_count += 1

    duration = time.perf_counter() - start
    avg_len = moves_sum / success_count if success_count > 0 else -1
    avg_attempts = attempts_sum / success_count if success_count > 0 else -1
    fails = sample_size - success_count
    return SampleStats(avg_len, avg_attempts, fails, duration)


def calculate(towers_max_count, disks_max_count, ai, filename, sample_size=1000, number_of_attempts=1000, tolerance=4):
    big_string = "sample_size: {}  number_of_attempts: {}  tolerance: {}\n\n".format(
        sample_size, number_of_attempts, tolerance)

    for i in range(3, towers_max_count + 1):
        for j in range(3, disks_max_count + 1):
            stats = average(i, j, ai, sample_size=sample_size, number_of_attempts=number_of_attempts)

            string = ""
            string += "towers: {}  disks: {}\n".format(i, j)
            string += "avg length: {}\n".format(stats.avg_length)
            string += "avg attempts: {}\n".format(stats.avg_attempts)
            string += "fails: {}\n".format(stats.fails)
            string += "duration: {}\n\n".format(stats.duration)

            print(string)
            big_string += string


    fd = open(filename, "w")
    fd.write(big_string)
    fd.close()
