# Largest Prime Factor

def calculateLargestPrimeFactor(n):
	# http://stackoverflow.com/questions/15347174/python-finding-prime-factors

	i = 2

	while i * i < n:
	    while n%i == 0:
	        n = n / i
	    i = i + 1

	print n

calculateLargestPrimeFactor(600851475143)