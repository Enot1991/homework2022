import time
import numpy as np



f1 = open("input.txt", "r")
f2 = open("output2.txt", "w")
puzzle_input = int(f1.read())



start = time.time()
houses = np.zeros((puzzle_input//10,), dtype=int)



for i in range(1, puzzle_input//10):
    number = i * 11
    houses[i:50*i+1:i] += number
it = np.nditer(houses, flags=['f_index'])
while not it.finished:
    if it[0] >= puzzle_input:
        f2.write(str(it.index))
        break
    it.iternext()


f1.close
f2.close
