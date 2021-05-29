import numpy as np
from scipy.optimize import fsolve

def get_lambda(avg):
    """Functional form to get lambda for Max ENT with avg constrain

    Input: 
    avg: Mean of experimental data

    Output: 
    lambda function: to calcule lambda for Max Ent
    """
    return lambda x : np.exp(-x)/(1-np.exp(-x))-avg
    
def P_ME(x, lambda_1):
    """Probability of waiting time x
    """
    Z = 1/(1-np.exp(-lambda_1))
    P = np.exp(-lambda_1*x)/Z
    return P, Z