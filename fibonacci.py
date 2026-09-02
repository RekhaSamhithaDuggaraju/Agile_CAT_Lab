# Fibonacci Series Program
# Fibonacci Series Program
# I am Rekha Samhitha Duggaraju (24MIS0418)
# Making a small change to the code

print("Welcome to the Fibonacci Series Generator")
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