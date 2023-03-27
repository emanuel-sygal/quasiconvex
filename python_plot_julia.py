import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the function for the iteration
def f(z, c):
    return z**2 + c

# Define the parameters
c = 0.26
xmin, xmax, ymin, ymax = -1.5,1.5,-1.5,1.5 # 0.48, 0.7, -0.15, 0.15
npoints = 2000
maxiter = 50

# Generate the grid of complex numbers
x = np.linspace(xmin, xmax, npoints)
y = np.linspace(ymin, ymax, npoints)
X, Y = np.meshgrid(x, y)
Z = X + 1j*Y

# Initialize the array to store the iteration count
count = np.zeros((npoints, npoints))

# Iterate the function and count the number of iterations until divergence
for i in range(maxiter):
    Z = f(Z, c)
    count[np.abs(Z) > 2] = i+1

# Plot the Julia set
plt.figure(figsize=(8,8))
plt.imshow(count, cmap='Blues', extent=(xmin, xmax, ymin, ymax))
#plt.axis('off')

# Plot the equipotentials
levels = np.arange(0, maxiter+1, 5)
#plt.contour(x, y, count, levels=levels, colors='red', linewidths=0.5)

plt.savefig("julia_026.png")
plt.show()