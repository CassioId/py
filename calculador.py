 #calculadora simples

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operador = input("Digite o operador (+, -, *, /): ")
if operador == '+':
    resultado = num1 + num2
    print(resultado)
elif operador == '-':
    resultado = num1 - num2
    print(resultado)
elif operador == '*':
    resultado = num1 * num2
    print(resultado)
elif operador == '/':
    resultado = num1 / num2
    print(resultado)
else:
    print("Erro: divisão por zero.")
