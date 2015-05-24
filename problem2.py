# Even Fibonacci numbers

def isEven(n):
	if (n % 2 == 0):
		return True
	else:
		return False

def calculateEvenSumFibonacci(num1, num2):
	sum = 0
	num3 = 0
	if (isEven(num1)):
		sum += num1
	if (isEven(num2)):
		sum += num2

	while (num2 < 4000000):
		num3 = num1 + num2
		if (num3 < 4000000 and isEven(num3)):
			sum += num3
		num1 = num2
		num2 = num3

	print sum

calculateEvenSumFibonacci(1,2)