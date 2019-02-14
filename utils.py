# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
import scipy.integrate as integrate
import scipy.special as special

def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	results=1
	if n<0:
		raise ValueError()
	else:

		for x in range(n):
			results = results * (x+1)
		return results

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	o = b**2 - 4*a*c 
	p = (-b + o**(0.5))/2*a
	q = (-b - o**(0.5))/2*a
	if p==q:
		return(p,)
	else:
		return (p,q)


def integrate(function, lower, upper):
	a= scipy.eval(fucntion)
	print(a)
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	pass

if __name__ == '__main__':
	print(fact(1))
	print(roots(2, -3,9/8))
	print(integrate('x ** 2 - 1', -1, 1))
