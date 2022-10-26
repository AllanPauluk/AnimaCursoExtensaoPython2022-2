#Projeto Python Curso de Extensão

#Aula 1 ----------------------------------------------------------

'''
Comentário em bloco
'''

'''
print("Hello Word!")

#Não é necessário declarar o tipo de variável
nome = "Allan Medeiros"
idade = 18

#print(f"Meu nome é " + nome, "\nE eu tenho " + {idade}, "anos")
#print("Meu nome é {} anos".format(idade))
#print("Meu nome é {} \nE eu tenho {} anos".format(nome, idade))
print("Meu nome é " + nome, "\nE eu tenho " + str(idade), "anos")
#print("meu nome é {0}, e eu tenho {1}".format(nome, idade)) 
'''
#Aula 2 ----------------------------------------------------------

#comando input(): quero permitir que o usuário digite algo 

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
dobro = idade * 2

#comando de saída.. exibir na tela

#print("O seu nome é " + nome, "e sua idade é " + idade, "anos")
print("O seu nome é {0}, sua idade é {1} anos. \nE o dobro de sua idade é {2}".format(nome, idade, dobro))