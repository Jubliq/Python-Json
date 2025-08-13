import os
import json
nome_arquivo = "teste.json"
os.system('cls')

def Imprime_Dados_Arquivo(nome):
    with open (nome,'r') as arquivo:
        conteudo_arquivo = json.load(arquivo)
    os.system('cls')
    for linha in conteudo_arquivo:
        print("CPF:",linha["CPF"])
        print("Nome:",linha["Nome"])
        print("Nickname:",linha["Nickname"])
        print()
        
def Cria_Novo_Arquivo(nome):
    os.system('cls')
    lista = []
    while True:
        pal1 = "s"
        if pal1 == "s":
            pessoa = {}
            pessoa["CPF"] = input("Digite o CPF da pessoa: ")
            pessoa["Nome"] = input("Digite o Nome da pessoa: ")
            pessoa["Nickname"] = input("Digite o nickname da pessoa: ")
            lista.append(pessoa)
        pal1 = input("Gostaria de cadastrar outra pessoa(s/n)? ")
        if pal1.lower() == "n":
            break
    with open (nome,'w') as arquivo:
        json.dump(lista,arquivo,indent=4)


def Adiciona_ao_Arquivo(nome):
    with open (nome,'r') as arquivo:
        conteudo_arquivo = json.load(arquivo)
    os.system('cls')
    while True:
        pal1 = "s"
        if pal1 == "s":
            pessoa = {}
            pessoa["CPF"] = input("Digite o CPF da pessoa: ")
            pessoa["Nome"] = input("Digite o Nome da pessoa: ")
            pessoa["Nickname"] = input("Digite o nickname da pessoa: ")
            conteudo_arquivo.append(pessoa)
        pal1 = input("Gostaria de cadastrar outra pessoa(s/n)? ")
        if pal1.lower() == "n":
            break
    with open (nome,'w') as arquivo:
        json.dump(conteudo_arquivo,arquivo,indent=4)


def Procura_CPF(nome):
    os.system('cls')
    with open (nome,'r') as arquivo:
        conteudo_arquivo = json.load(arquivo)
    cpf_proc = input("Digite o CPF que deseja procurar: ")
    for pessoa in conteudo_arquivo:
        if pessoa["CPF"] == cpf_proc:
            os.system('cls')
            print("Dados da pessoa procurada:")
            print("CPF:",pessoa["CPF"])
            print("Nome:",pessoa["Nome"])
            print("Nickname:",pessoa["Nickname"])
            print()
            break
        
def Exclui_Pessoa(nome):
    os.system('cls')
    with open (nome,'r') as arquivo:
        conteudo_arquivo = json.load(arquivo)
    cpf_proc = input("Digite o CPF que deseja excluir: ")
    for pessoa in conteudo_arquivo:
        if pessoa["CPF"] == cpf_proc:
            conteudo_arquivo.remove(pessoa)
            break
    print()
    print("Pessoa removida com sucesso")
    print()
    with open (nome,'w') as arquivo:
        json.dump(conteudo_arquivo,arquivo,indent=4)

def Atualiza_Cadastro(nome):
    os.system('cls')
    with open (nome,'r') as arquivo:
        conteudo_arquivo = json.load(arquivo)
    cpf_proc = input("Digite o CPF que deseja atualizar: ")
    for pessoa in conteudo_arquivo:
        if pessoa["CPF"] == cpf_proc:    
            pessoa["Nome"] = input("Digite o novo nome da pessoa: ")
            pessoa["Nickname"] = input("Digite o novo nickname da pessoa: ")
    with open (nome,'w') as arquivo:
        json.dump(conteudo_arquivo,arquivo,indent=4)

# MENU PARA TESTES DAS FUNÇÕES
while True:
    opcao = input(f"O que deseja fazer?\n\n1 = Reescrever arquivo do zero\n2 = Adicionar ao final do arquivo\n3 = Ler arquivo\n4 = Procurar por CPF\n5 = Atualizar por CPF\n6 = Excluir por CPF\n9 = Sair\n")
    if opcao == "1":
        Cria_Novo_Arquivo(nome_arquivo)
    if opcao == "2":
        Adiciona_ao_Arquivo(nome_arquivo)
    if opcao == "3":
        Imprime_Dados_Arquivo(nome_arquivo)
    if opcao == "4":
        Procura_CPF(nome_arquivo)
    if opcao == "5":
        Atualiza_Cadastro(nome_arquivo)
    if opcao == "6":
        Exclui_Pessoa(nome_arquivo)
    if opcao == "9":
        break
    
