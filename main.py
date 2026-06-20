import os
from menu import *

def menu():
    while True:
        titulo("LOCAÇÃO DE RESTAURANTES")
        print("\n1. Cadastrar Restaurante\n2. Listar Restaurante\n3. Status do Restaurante\n4. Ajustar Restaurante\n5. Sair\n")
        menu_escolha_cliente = input ("Escolha uma opção: ")
        match menu_escolha_cliente:
            case "1" | "um":
                cadastrar_restaurante()

            case "2" | "dois":
                listagem_restaurante()

            case "3" | "tres" | "três":
                status_restaurante()

            case "4" | "quatro":
                configurar_restaurante()

            case "5" | "cinco":
                os.system("clear")
                break

            case _:
                input("\nOpção inválida, tente novamente!\n")
                os.system("clear")

#def main():
#    os.system("clear")
#    menu()

#main()
menu()

