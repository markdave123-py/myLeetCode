number = int(input('Enter number: '))
factors = []

for numbers in range(1, number+1):
    if number % numbers == 0:
        factors.append(numbers)

if len(factors) == 2:
    print(f'{number} is a prime number')

else:
    print(f'{number} is not a prime number and the factor are {factors}')