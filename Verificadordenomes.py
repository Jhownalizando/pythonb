print("__________________________________")
print("Digite o seu nome")
nome=input()
op1=0
op2=0
print(" ")
print("Seja bem vindo a verificacao de nomes LTDA!!")
print(" ")
print("O sistema serve para verificacao da existencia de alguma certa letra no seu nome, ou a sua quantidade")
print(" ")
while op1 != 3:
    print("MENU:")
    print(" 1 - VERIFICAR LETRAS EXISTENTES")
    print(" 2 - CONTAR TAMANHO E CONTAR LETRAS ESPECIFICAS")
    print(" 3 - SAIR")
    print(" ")
    op1=int(input())
    if (op1==1):
        print("Digite a letra que quer procurar:" )
        letra=input()
        if (letra in nome):
            print("__________________________________")
            print("Essa letra EXISTE no nome!")
            print("__________________________________")
            print(" ")
        else:
            if(letra not in nome):
                print("__________________________________")
                print("Essa letra NÃO existe nome")
                print("__________________________________")
                print(" ")
        
    else:
        if(op1==2):
            print("__________________________________")
            print(" ")
            print("A quantidade de caracteres(com espaços) do nome é: ")
            print(len(nome))
            print(" ")
            print("__________________________________")
            print(" ")
            while op2 != 2:
                print("1 - CONTADOR DE CARACTERES. TECLE 1")
                print("2 - VOLTAR AO MENU ANTERIOR. TECLE 2")
                print(" ")
                op2=int(input())
                print("__________________________________")
                print(" ")
                if op2 == 1 :
                    print("Digite a letra que quer pesquisar")
                    let=input()
                    if nome.count(let) >= 1:
                        print(" ")
                        print("A quantia de vezes que a letra aparece:")
                        print(nome.count(let))
                    else:
                        print(" ")
                        print("Não contem essa letra no nome!")
                else:
                    if op2 == 2:
                        print(" ")
                        print("Retornando ao primeiro menu")
                    else:
                        if (op2 != 1 & 2) :
                            print(" ")
                            print("Das duas uma, você é um engracadinho e quer burlar o sistema ou digitou errado, então tente novamente!")
                            print("__________________________________")
                            print(" ")
                
                    

            
