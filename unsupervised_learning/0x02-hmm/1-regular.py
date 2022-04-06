#!/usr/bin/env python3
def regular(P):
  n= P.shape[0]
  d=P.shape[1]
  if type(P) is not np.ndarray or P.ndim!=2 or n!= d :
    return None
  if not np.allclose(np.sum(P, axis=1), 1):
        return None
    
  #1/compute eigenvector,eigenvalue
  evalue,evector= np.linalg.eig(P.T) 
  one= np.argwhere(np.isclose(evalue,1))
     
  #2/compute eigenvector where eigenvalue=1
  if len(one)!=1: 
    return None
  steady_state_vector=evector[:,one[0]]/np.sum(evector[:,one[0]]) 
  if 0 in steady_state_vector : 
    return None
  return steady_state_vector.T
