
def celsius_para_fahrenheit(celsius):
    return(celsius * 9 / 5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return(fahrenheit - 32) * 5 / 9

def main():
    while True:
        print("\nEscolha o tipo de conversão:")
        print("1: Celsius para Fahrenheit")
        print("2: Fahrenheit para Celsius")
        print("3: Sair")

        escolha = int(input("Digite 1, 2 ou 3 "))
        if escolha == 1:
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = celsius_para_fahrenheit(celsius)
            print(f"{celsius}°C é igual a {fahrenheit:.2}°F")
        elif escolha == 2:
            fahrenheit= float(input("Digite a temperatura em Fahrenheit: "))
            celsius = fahrenheit_para_celsius(fahrenheit)
            print(f"{fahrenheit}°F é igual a {celsius:.2}°C")
        elif escolha == 3:
            print("Saindo do programa...")
            break
        else:
            print("Escolha inválida! Por favor, tente novamente.")

if __name__=="__main__":
    main()