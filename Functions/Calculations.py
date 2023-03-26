def solve(a, b, operator):
    if operator == "multiply":
        return a * b
    if operator == "divide":
        return a / b
    if operator == "add":
        return a + b
    if operator == "subtract":
        return a - b


input_op = input()
num1 = int(input())
num2 = int(input())
print(solve(num1, num2, input_op))
