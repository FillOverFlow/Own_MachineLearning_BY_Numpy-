import numpy as np 

#init variable 
x = 10 
alpha = 0.01 #learning_rate 
n_itear = 1000 
J = [] #thera


def compute_cost(x):  #x^2-4x
	J = x**2-4*x
	return J

def compute_grad(x): #2x-4
	grad = 2*x-4
	return grad 


for  i  in range(n_itear):   				#x = x-(alpha*grad)

	x = x -(alpha * compute_grad(x))
	J.append(compute_cost(x))


print("Resutl final X:",x)
print("Resutl final J",J[-1])




	
