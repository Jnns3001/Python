import time

bit = ["0","1"]


for four in bit:
    for three in bit:
        for two in bit:
            for one in bit:
                y = four + three +two +one
                print(y)
                time.sleep(0.1)

print("\nfinish")