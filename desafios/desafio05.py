print("| CALCULOS DIVERSOS |")
print("-"*30)

num1 = float(input("Digite o #1 número: "))
num2 = float(input("Digite o #2 número: "))

soma = num1+num2
sub = num1-num2
mult = num1*num2
div = num1/num2
pot = num1**num2
divint = num1//num2
resdiv = num1%num2

print(f"{num1} + {num2} = {soma}")
print(f"{num1} - {num2} = {sub}")
print(f"{num1} * {num2} = {mult}")
print(f"{num1} / {num2} = {div}")
print(f"{num1} ** {num2} = {pot}")
print(f"{num1} // {num2} = {divint}")
print(f"{num1} % {num2} = {resdiv}")