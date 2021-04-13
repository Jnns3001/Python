import math

from tabulate import tabulate

#const
a_g = 30            #overall goal acceleration
r = 5               #radius of turn
t = 0.05            #timestep in seconds
epsilon = 0.02      #tolerance
u = 430             #Voltage Source
m = 200             #Mass of the accelerating Object

#vars
a_z = 0             #resulting zentripetal acceleration
a_o = 0             #current input acceleration
a_n = 0             #calculated goal input acceleration
v_c = 0             #current speed
time = 0            #Current Time
f = 0               #Force needed for v_n
p = 0               #Power needed for Force
i_max = 0           #Max Current
p_max = 0           #Max Power
i = 0               #Current for specific power
output = [["timestamp: ", "Goal Input acc: ", "Current Velocity: ", "Applied Force: ", "Current Powercomsumption: ", "Current Current: "]]         #Output list



#[["timestamp: "], ["Goal Input acc: "], ["Current Velocity: "], ["Applied Force: "], ["Current Powercomsumption: "], ["Current Current: "]]         #Output list


while True:
    tempout = []
    
    #calc goal input acc
    k = (a_o*t + v_c)
    k2 = k*k
    x = (k2/r)*(k2/r)
    try:
        a_n = math.sqrt(float(900-x))
    except ValueError:
        break
    
    #Set output values
    tempout.append(round(time, 3))
    tempout.append(round(a_n,3))
    tempout.append(round(v_c,3))
    tempout.append(round(f,3))
    tempout.append(round(p,3))
    tempout.append(round(i, 3))
    output.append(tempout)

    #Update Acceleration
    a_o = a_n
    #calc current velocity
    v_c = v_c + a_o * t
    #calc applied force
    f = m * a_n
    #calc Powerconsumption at specific time and max power
    p = f * v_c
    if p > p_max:
        p_max = p
        i_max = p_max / u
    #calc Current
    i = p / u
    #Update Timestamp
    time = time + t

print("Done, speed goal reached")
print(tabulate(output))
print("Max Power: " + str(round(p_max, 3))+ ", Max Current: " + str(round(i_max, 3)))