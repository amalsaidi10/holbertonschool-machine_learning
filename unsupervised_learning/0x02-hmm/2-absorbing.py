import numpy as np

def absorbing(P):
    """absorbing markov chain"""
    if type(P) is not np.ndarray:
        return False
    if P.ndim != 2 or P.shape[0] != P.shape[1]:
        return False
    if not np.allclose(np.sum(P, axis=1), 1):
        return False

    n = P.shape[0]
    #case1:each state is an absorbing state in the markov(all terme in diagonal are 1) 
    
    i = 0
    while P[i][i] == 1:
        i += 1
        if i == len(P):
            return True
    #case2: at least one absorbing stat and it is possible to go from any state to an absorbing state   
    if i == 0:
        return False
    if (1 in np.max(P[i:, :], axis=0)) or (np.sum(P[:i, i:]) != 0):
        return False
    Q = P[i:, i:]
    R = P[i:, :i]
    t = Q.shape[0]
    IQ = np.eye(t) - Q
    if np.linalg.det(IQ) == 0:# it is not inversible
        return False
    N = np.linalg.inv(IQ)
    B = np.matmul(N, R)
    if np.any(N * R == 0):
        return True

    return False
