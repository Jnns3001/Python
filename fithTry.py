
def list(stop,start=0,step=1,y=None):
    if y is None:
        y = []
    for i in range(start, stop, step):
        y.append(i)
    return y


print(list(100,2, 2,[100]))
