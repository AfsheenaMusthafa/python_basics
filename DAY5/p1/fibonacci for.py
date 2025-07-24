num = int(input("Enter how many numbers to print: "))

num1 = 0
num2 = 1

print("Fibonacci series:")
print(num1, num2, end=" ")

for _ in range(num): 
    result = num1 + num2
    print(result, end=" ")
    num1 = num2
    num2 = result

