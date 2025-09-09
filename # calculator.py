# calculator
'''
def sum(a,b):
    return (a+b)
a = float(input('Enter 1st number: '))
b = float(input('Enter 2nd number: '))
print(f"Sum of {a} and {b} is {sum(a,b)}")
'''
while loop==0:

    def add(x,y):
        return x+y
    def subtract(z,y):
        return z-y
    def multiply(x,y):
        return x*y
    def divide(x,y):
        if y!=0:
            return x/y
        else:
            return "Error, Cannot divide by zero."
    print('Select operation:')
    print('1.Add')
    print('2.Subtract')
    print('3.Multiply')
    print('4.Divide')
    choice = input('Enter choice (1,2,3,or 4):')
    num1= float(input('Enter first number:'))
    num2= float(input('Enter second number:'))
    if choice == "1":
        print(f'{num1}+ {num2} = {add(num1,num2)}')
    elif choice == "2":
        print(f'{num1} - {num2} = {subtract(num1,num2)}')
    elif choice == "3":
        print(f'{num1} * {num2} = {multiply(num1,num2)}')
    elif choice == "4":
        print(f'{num1} / {num2} = {divide(num1,num2)}')
    elif choice == 'End' or "end":
        loop= loop + 1
        break
    else:
        print("Invaid input.")
