from iterativeDeepeningSearch import *
from uniformCost import *
import time

instances = []

file = open("instante.txt", 'r')

for i in range(25):
    inst = file.readline()
    n = int(inst[0])
    m = int(inst[2])
    instances.append((n, m))

file.close()

file_write = open("./avg/ids_ai - avg.txt", 'w')

def compute_height(n, m):
    if n == m:
        return m*2
    if n == 3:
        return 2**m - 2
    if n == 4:
        return ( 2 + m - n) * 4 - 1
    return 2*m-2

count_moves = 0
count_time = 0

for inst in instances:
    n = inst[0]
    m = inst[1]
    hanoi = Hanoi(n, m)
    ids = IterativeDeepeningSearch(hanoi, compute_height(n, m))
    
    start = time.perf_counter()
    result = ids.getResult()
    end = time.perf_counter() - start
    
    count_moves += result[2]
    count_time += end

    string = "towers: " + str(n) + " disks: " + str(m) + '\n' + "len: " + str(result[1]) + "\n" + "number of states until reach final: " + str(result[2]) + "\n" + "time: " + str(end) + " seconds" +"\n\n"
    print(string)
    file_write.write(string)
string = "Average:" + "\n" + " - moves: " + str(count_moves / 25) + "\n" + " - time: " + str(count_time / 25)
file_write.write(string)
file_write.close()

file_write = open("./avg/uniformcost_ai - avg.txt", 'w')

count_moves = 0
count_time = 0

for inst in instances:
    n = inst[0]
    m = inst[1]

    hanoi = Hanoi(n, m)
    uc = UniformCost(hanoi)
    
    start = time.perf_counter()
    uc.run()
    end = time.perf_counter() - start
    
    count_moves += uc.no_transitions
    count_time += end
    string = "towers: " + str(n) + " disks: " + str(m) + '\n' + "len: " + str(uc.result[0][1]) + "\n" + "number of states until reach final: " + str(uc.no_transitions) + "\n" + "time: " + str(end) + " seconds" + "\n\n"
    print(string)
    file_write.write(string)
string = "Average:" + "\n" + " - moves: " + str(count_moves / 25) + "\n" + " - time: " + str(count_time / 25)
file_write.write(string)
file_write.close()