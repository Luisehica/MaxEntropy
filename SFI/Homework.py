import MaxEnt

import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

### Give the maximum entropy distribution PMaxEnt (x) that constrains an mean of 7

### Define function to get lambda
get_lambda = MaxEnt.get_lambda(7)
lambda_1 = fsolve(get_lambda, [1])
print("*"*50)
print(f'The value of lambda_1 = {lambda_1}')
print("-"*50)
### Calcule Z
_, Z = MaxEnt.P_ME(4, lambda_1)
print(f"the value of Z = {Z}")
print("-"*50)