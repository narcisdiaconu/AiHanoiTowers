from base import *
import time

def calculate(ai, read_filename, write_filename):
    big_string = ""

    with open(read_filename, "r") as fd:
        instances = fd.readlines()

    for instance in instances:
        try:
            towers_count, disks_count, pos_start, pos_end = [int(x) for x in instance.split(" ")]
            ai.hanoi = Hanoi(towers_count, disks_count, pos_start, pos_end)

            start = time.perf_counter()
            result = ai.solution()
            duration = time.perf_counter() - start

            string = ""
            string += "towers: {}  disks: {}  start: {}  end: {}\n".format(towers_count, disks_count, pos_start, pos_end)
            string += "solution length: {}\n".format(len(result))
            string += "evaluated states: {}\n".format(ai.evaluated_states_count)
            string += "duration: {}\n\n".format(duration)

            print(string)
            big_string += string
        except:
            print("invalid instance:\n {}".format(instance.split(" ")))
            print()


    fd = open(write_filename, "w")
    fd.write(big_string)
    fd.close()
