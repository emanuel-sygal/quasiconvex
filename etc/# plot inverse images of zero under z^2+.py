# plot inverse images of zero under z^2+c
from matplotlib import pyplot as plt 

c = 0.24
cur_points = [0]
iter = 0
while True:
    iter += 1
    new_points = []
    for p in cur_points:
        for new_p in [(p-c)**.5, -(p-c)**.5]:
            new_points.append(new_p)
            plt.scatter(new_p.real, new_p.imag)
    cur_points = new_points.copy()
    print(iter)
    if iter >= 11: plt.show()
