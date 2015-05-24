# Multiples of 3 and 5

multiples = set()
sum = 0

def is_multiple(n):
	if (n % 3 == 0 or n % 5 == 0):
		return True
	else:
		return False

for x in range(1000):
	if (is_multiple(x)):
		multiples.add(x)
		sum += x

print sum
