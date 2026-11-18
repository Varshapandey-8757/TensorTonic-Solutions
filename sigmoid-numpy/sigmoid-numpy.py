import numpy as np

def sigmoid(x):
    x = np.asarray(x,dtype=float)
    result = 1/(1+np.exp(-x))
    if x.ndim == 0:
        return float(result)
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    
    return result