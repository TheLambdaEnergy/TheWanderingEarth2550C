with open("dir.txt","r") as f:
    lines = f.readlines()
    res = []
    for line in lines:
        line = line.strip()[26:]
        res.append(line)

import time
import random
time.sleep(15)

random.shuffle(res)

a = 1

for i in res:
    # proc = int(a/1500)

    print(a, str(a/1500)[2:4]+r"% GENERATING " + i.lstrip())
    time.sleep(0.02)
    a += 1
    if a == 1500:
        break
    else:pass

print("550C Report: Basic Operating System Generation Complete!")

