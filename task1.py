def factor(x):
    if x<2:
        return 1
    else:
        return (x * factor(x-1))

num = int(input("Enter a number: "))

print(f"Factorial of {num} is:",factor(num))