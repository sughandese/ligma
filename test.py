# Initial file for testing purposes

def fibonacci(n):
	if ((n == 0) | (n == 1)):
		return n
	return (fibonacci(n-1) + fibonacci(n-2))

print("Hello world!")
print(fibonacci(6))