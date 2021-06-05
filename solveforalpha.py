import math
import matplotlib.pyplot as plt

r_1 = 6000
r_2 = 1400
r_3 = 1000

ang = []
res = []

for i in range(2000, 7000, 10):
    y = i/100
    ang.append(y)
    a = math.radians(y)
    x = r_1 - r_3 - math.sqrt((r_1)**2 - (math.sin(a)* r_2)**2) + math.sqrt((r_2)**2 - (math.sin(a)* r_2)**2)
    res.append(x)
    print(y , x)

plt.plot(ang, res)
plt.xlabel('Angel')
plt.ylabel('Distance')
plt.show()