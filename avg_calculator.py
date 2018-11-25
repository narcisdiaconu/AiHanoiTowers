from base import *

def calculate(towers_max_count, disks_max_count, ai, filename, iterations=1000):
    string = ""

    for i in range(3, towers_max_count):
        for j in range(3, disks_max_count):
            hanoi = Hanoi(i, j)
            ai.hanoi = hanoi

            moves_sum = 0
            success_count = 0

            for k in range(iterations):
                result = ai.solution()
                if result:
                    moves_sum += len(hanoi.moves_history)
                    success_count += 1
            
            avg = moves_sum / success_count if success_count != 0 else -1

            string += "towers: " + str(i) + " disks: " + str(j) + "\n"
            string += "avg: " + str(avg) + "\n"
            string += "failed: " + str(iterations - success_count) + "\n\n"

    fd = open(filename, "w")   
    fd.write(string)
    fd.close()