from base import *
import time

class SampleStats:
    def __init__(self, avg_length, avg_attempts, fails, duration):
        self.avg_length = avg_length
        self.avg_attempts = avg_attempts
        self.fails = fails
        self.duration = duration

def average(ai, sample_size=1000, number_of_attempts=1000, tolerance=4):
    moves_sum = 0
    attempts_sum = 0
    success_count = 0

    start = time.perf_counter()

    for k in range(sample_size):
        ai.hanoi.init()
        attempts = ai.solution(number_of_attempts=number_of_attempts, tolerance=tolerance)
        if attempts >= 0:
            moves_sum += len(ai.hanoi.moves_history)
            attempts_sum += attempts
            success_count += 1

    duration = (time.perf_counter() - start) / sample_size
    avg_len = moves_sum / success_count if success_count > 0 else -1
    avg_attempts = attempts_sum / success_count if success_count > 0 else -1
    fails = sample_size - success_count
    return SampleStats(avg_len, avg_attempts, fails, duration)


def calculate(ai, read_filename, write_filename, sample_size=1000, number_of_attempts=1000, tolerance=4):
    big_string = "sample_size: {}  number_of_attempts: {}  tolerance: {}\n\n".format(
        sample_size, number_of_attempts, tolerance)

    with open(read_filename, "r") as fd:
        instances = fd.readlines()

    for instance in instances:
        try:
            towers_count, disks_count, pos_start, pos_end = [int(x) for x in instance.split(" ")]
            ai.hanoi = Hanoi(towers_count, disks_count, pos_start, pos_end)

            stats = average(ai, sample_size=sample_size, number_of_attempts=number_of_attempts)

            string = ""
            string += "towers: {}  disks: {}  start: {}  end: {}\n".format(towers_count, disks_count, pos_start, pos_end)
            string += "avg length: {}\n".format(stats.avg_length)
            string += "avg attempts: {}\n".format(stats.avg_attempts)
            string += "avg duration: {}\n".format(stats.duration)
            string += "fails: {}\n\n".format(stats.fails)

            print(string)
            big_string += string
        except:
            print("invalid instance:\n {}".format(instance.split(" ")))
            print()


    fd = open(write_filename, "w")
    fd.write(big_string)
    fd.close()
