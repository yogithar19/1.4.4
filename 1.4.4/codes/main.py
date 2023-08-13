import numpy as np
import matplotlib.pyplot as plt
 
def line_intersect(n1,A1,n2,A2):
  N=np.vstack((n1,n2))
  p = np.zeros(2)
  p[0] = n1@A1
  p[1] = n2@A2
  #Intersection
  P=np.linalg.inv(N)@p
  return P
  
def dir_vec(A,B):
  return B-A

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
  
# enter vectors A,B & C
A=np.array([1,-1])
B=np.array([-4,6])
C=np.array([-3,-5])
# direction vector along line joining A & B
AB = dir_vec(A,B)
# direction vector along line joining A & C
AC = dir_vec(A,C)
# midpoint of A & B is F
F = (A+B)/2
# midpoint of A & C is E
E = (A+C)/2
# O is the point of intersection of perpendicular bisectors of AB and AC
O = line_intersect(AB,F,AC,E)
print(O)


OA= A-O
OB=B-O
OC=C-O

print("OA=" ,OA)
print("OB=",OB)
print("OC=",OC)

#norms
n_OA= np.linalg.norm(OA)
print("Norm(OA):", n_OA)
n_OB= np.linalg.norm(OB)
print("Norm(OB):", n_OB)
n_OC= np.linalg.norm(OC)
print("Norm(OC):", n_OC)


