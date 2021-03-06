#%% Import Libraries

import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

""" Using numpy """
#%% Manual computation
# the list of numbers
z = [1, 2, 3]

# compute the softmax result
num = np.exp(z)
den = np.sum( np.exp(z) )
sigma = num / den

print(sigma)

# Output:
# [0.09003057 0.24472847 0.66524096]

#%% Repeat with some random integers and Plot data
z = np.random.randint(-5, high=15, size=50)
print(z)

# compute softmax result
num = np.exp(z)
den = np.sum( np.exp(z) )
sigma = num / den
print(sigma)

# Plot data
plt.figure(figsize=(6, 4))
plt.plot(z, sigma, 'ro')
plt.xlabel('Original number (z)')
plt.ylabel('Softmaxified $\sigma$')
# plt.yscale('log')
plt.title('$\sum\sigma$ = %g' %np.sum(sigma))
plt.savefig("plots/Softmax.svg", dpi=150)
# plt.savefig("plots/Softmax_log.svg", dpi=150)
plt.show()

""" Using PyTorch """
# %% Computation using nn.Softmax activation class

# create an instance of the softmax activation class
softfunc = nn.Softmax(dim=0)

# apply previously created data to the function
sigmaT = softfunc( torch.Tensor(z) )

# print the result
print(sigmaT)

# Compare plots
plt.figure(figsize=(6, 4))
plt.plot(sigma, sigmaT, 'ro')
plt.xlabel('"Manual" Softmax')
plt.ylabel('PyTorch nn.Softmax')
plt.title(f'The two methods correlate at r = {np.corrcoef(sigma, sigmaT)[0, 1]}')
plt.savefig("plots/Softmax_compare.svg", dpi=150)
plt.show()