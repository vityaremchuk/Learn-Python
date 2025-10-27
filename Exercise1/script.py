num1 = int(input("Enter your first number: "));
num2 = int(input("Enter your second number: "));

multiplication = num1 * num2;
addition = num1 + num2;

if multiplication <= 1000:
    print(multiplication)
else:
    print(addition)