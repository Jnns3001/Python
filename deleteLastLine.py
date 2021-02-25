import time
timer = 1

print("huhu")
while True:
    timer += 1
    print("timer: " + str(timer)+ "\r" + "hi")
    time.sleep(1)
print("\033[A\033[A")