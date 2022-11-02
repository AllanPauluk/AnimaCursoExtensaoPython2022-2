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
#print("Meu nome é " + nome, "\nE eu tenho " + str(idade), "anos")
#print("meu nome é {0}, e eu tenho {1}".format(nome, idade)) 
'''
#Aula 2 ----------------------------------------------------------
'''
#comando input(): quero permitir que o usuário digite algo
#comando de saída.. exibir na tela

#Variáveis
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
#dobro = idade * 2

#print("O seu nome é " + nome, "e sua idade é " + idade, "anos")
#print("O seu nome é {0}, sua idade é {1} anos. \nE o dobro de sua idade é {2}".format(nome, idade, dobro))

#Estrutura condicional (if)

print("O seu nome é {0}, sua idade é {1} anos.".format(nome, idade))

if (idade>=18):
  print("Você é maior de idade! Já pode beber e dirigir.")
else:
  print("Você é menor de idade! E não pode beber nem dirigir")
if (sexo=M):
  print("Você deve prestar o serviço militar obrigatório")
else: 
  print("Você não precisa prestar o serviço")
  '''
#Pt2 Aula 2 ------------------------------------------------------]

#Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "Você é bichão, mesmo..."

nome = input("Digite seu nome: ")
nota = int(input("Digite sua nota: "))

if (nota == 10):
  print("Você é o bixão mesmo")
elif (nota >= 6 and nota < 10):
    print("Deu pro gasto")
else:
  print("Burro, não tirou dez...")