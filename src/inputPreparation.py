import sys
import random

k = sys.argv[1]
m = sys.argv[2]

numbers = [str(random.randint(1, int(m))) for _ in range(int(m))]

with open("input.txt", "w") as f:
    f.write(f"{k} {m}\n" + " ".join(numbers))