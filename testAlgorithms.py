from iterativeDeepeningSearch import *
from uniformCost import *

file = open("instante.txt", 'r')
file_write = open("./avg/ids_ai - avg.txt", 'w')

def compute_height(n, m):
    if n == m:
        return m*2
    if n == 3:
        return 2**m - 2
    if n == 4:
        return ( 2 + m - n) * 4 - 1
    return 2*m-2

for i in range(16):
    instanta = file.readline()
    n = int(instanta[0])
    m = int(instanta[2])

    hanoi = Hanoi(n, m)
    ids = IterativeDeepeningSearch(hanoi, compute_height(n, m))
    result = ids.getResult()
    string = "towers: " + str(n) + " disks: " + str(m) + '\n' + "len: " + str(result[1]) + "\n" + "number of states until reach final: " + str(result[2]) + "\n\n"
    print(string)
    file_write.write(string)

file.close()
file_write.close()

# file = open("instante.txt", 'r')
# file_write = open("./avg/uniformcost_ai - avg.txt", 'w')

# for i in range(16):
#     instanta = file.readline()
#     n = int(instanta[0])
#     m = int(instanta[2])

#     hanoi = Hanoi(n, m)
#     uc = UniformCost(hanoi)
#     uc.run()
#     string = "towers: " + str(n) + " disks: " + str(m) + '\n' + "len: " + str(uc.result[0][1]) + "\n" + "number of states until reach final: " + str(uc.no_transitions) + "\n\n"
#     print(string)
#     file_write.write(string)

# file_write.close()