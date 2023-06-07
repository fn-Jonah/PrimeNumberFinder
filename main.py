import sys
import time

factors = 0
theprime = 0
additionrange = 1

numbercalc = int(input("How Many Calculations?\n:"))

stdoutOrigin=sys.stdout 
sys.stdout = open("primenumbers.txt", "w")

tic = time.perf_counter()
for notppn in range(numbercalc): 
    ppn = notppn + 1 

    for notprimedivider in range(additionrange):
        primedivider = notprimedivider + 1 
        fact = ppn % primedivider

        if fact == 0: 
            factors += 1
    if factors == 2:
        theprime += 1
        print(theprime, ":", ppn)

    factors = 0 
    additionrange += 1
toc = time.perf_counter()
print(f"\nFinished In: {toc - tic:0.4f} seconds")

