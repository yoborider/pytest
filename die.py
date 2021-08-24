import random as rd
import time

class Die:
    sides: int
    def roll(self):
        return rd.randint(1, self.sides)
    def __init__(self, sides=6):
        self.sides = sides

if __name__ == "__main__":
    tic = time.perf_counter()
    for i in range(0,100000-1):
        Die(6).roll()
    toc = time.perf_counter()
    print(f"Updated in {toc - tic:0.4f} seconds")
    time_elapsed_ms = (toc-tic)*1000
    print(f"Elapsed time in milliseconds: {int(round(time_elapsed_ms))} ms")
