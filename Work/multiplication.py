import numpy as np
from numpy import linalg as LA
a=np.array([[0.25,-0.75,0.25,0.25],[-1.5,-0.5,0.5,1.5]])
b=a.transpose()
x=np.matmul(a,b)
print(x)
w, v = LA.eig(x)
print(v)
print(w)
v=([0.116,0.9933])
x=np.matmul(b,v)
x