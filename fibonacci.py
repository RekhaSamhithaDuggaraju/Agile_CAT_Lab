# Fibonacci Series Program

n = int(input("Enter the number of terms: "))

first = 0
second = 1

print("\nFibonacci Series:")

for i in range(n):
    print(first, end=" ")

    next_number = first + second
    first = second
    second = next_number

print("\n\nProgram executed successfully!")