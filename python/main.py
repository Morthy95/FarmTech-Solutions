#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def menu():
    while True:
        print("\n=== FarmTech Solutions (Python) ===")
        print("1) Inserir dados")
        print("2) Listar dados")
        print("3) Atualizar por índice")
        print("4) Deletar por índice")
        print("5) Exportar CSV para R")
        print("0) Sair")

        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                print(">> Inserir dados (em breve)")
            case "2":
                print(">> Listar dados (em breve)")
            case "3":
                print(">> Atualizar dados (em breve)")
            case "4":
                print(">> Deletar dados (em breve)")
            case "5":
                print(">> Exportar CSV (em breve)")
            case "0":
                print("Saindo... até logo!")
                break
            case _:
                print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()