import MaxEnt

import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

### Define function to get lambda
get_lambda = MaxEnt.get_lambda(4)
lambda_1 = fsolve(get_lambda, [1])
print("*"*50)
print(f'The value fo lambda_1 = {lambda_1}')
print("-"*50)

### Calcule Z
_, Z = MaxEnt.P_ME(4, lambda_1)
print(f"the value of Z = {Z}")
print("-"*50)


### Calcule so MaxEnt probabilities
P_1, _ = MaxEnt.P_MaxEnt(4, lambda_1)

print(f'the probability of find a taxicab in {1} minute is {P_1}')
print("-"*50)

i = np.arange(10)
P, Z = MaxEnt.P_MaxEnt(i, lambda_1)
print(i)
print(P)

plt.plot(i,P)
plt.savefig("taxicab.png")
plt.show()