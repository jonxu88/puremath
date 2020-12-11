#Given choice of n,k, and T \subseteq \{1,2, ..., k\}, it gives a bound
#for the size of a T-coclique in the Johnson scheme J(n,k)
#This bound is given in Theorem 3.8.2 of Godsil-Meagher


from scipy.special import comb
import math
import numpy as np
from numpy.linalg import inv
from pulp import *

#Compute the ps
def p(n,k,j,i):
    pkji = 0
    for h in range(j+1):
        pkji += (-1)**(j-h) * comb(k-h, j-h) * comb(k-i, h) * comb(n-k+h-i, h)
    return float(pkji)

#Define the matrix P (the indexing needs to be moved by 1 since Python counts from 0)
def P(n,k):
    Pnk = np.zeros((k+1,k+1))
    for i in range(k+1):
        for j in range(k+1):
            Pnk[i][j] = p(n,k,j,i)
    return Pnk

#Define the matrix Q 
def Q(n,k): 
    return v * inv(P(n,k))


#Compute the qs
def q(n,k,j,i): 
    return Q(n,k)[i][j]

#Compute the ms
def m(n,k,i):
    return float(comb(n,i) - comb(n,i-1))

#Turn a string "{t_1, t_2, ..., t_p}" into a set {t_1, t_2, ..., t_p}
def turn_into_set(T):
    T = T.replace('{', '')
    T = T.replace('}', '')
    T = T.split(',')
    for i in range(len(T)): 
        T[i] = int(T[i])
    T = set(T)
    return T

#Program starts here
n = input("Enter the integer n: ")
n = int(n)
k = input("Enter the integer k: ")
k = int(k)
T = input("Enter the subset T (in the form {i1, i2, ..., it}): ")
T = turn_into_set(T)
v = comb(n,k)
v = int(v)

prob = LpProblem("JSBound", LpMinimize)


# Define variables lambda1, lambda2, ..., lambdak and declare that all these are bounded below by 0
lambdas = LpVariable.dicts("lambda", range(1,k + 1), lowBound = 0)

# Equation to minimise goes here
prob += 1 + lpSum((lambdas[i] * m(n,k,i)) for i in range(1,k+1))

# For all j in \{1,2,...,d\} - T include the equations \sum_{i=0}^d ... to the problem and force them to equal zero
Tc = set(range(1, k+1)) - T
for j in Tc:
    prob += q(n,k,0,j)/v + lpSum((lambdas[i] * q(n,k,i,j) /v ) for i in range(1,k+1)) == 0

prob

status = prob.solve()
LpStatus[status]

value(prob.objective)

print(prob)
print("---")
print("Optimality of the solution:")
print(LpStatus[status])
print("---")
print("The upper bound is " + str(value(prob.objective)))
