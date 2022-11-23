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
#Pt2 Aula 2 
'''
#Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "Você é bichão, mesmo..."

nome = input("Digite seu nome: ")
nota = int(input("Digite sua nota: "))

if (nota == 10):
  print("Você é o bixão mesmo")
elif (nota >= 6 and nota < 10):
    print("Deu pro gasto")
else:
  print("Burro, não tirou dez...")
  '''
#Exemplo de laço

'''#Se eu quisesse exibir números de 1 a 10?
print("Aqui mostramos de maneira 'rústica'")
print("1")
print("2")
print("3")
print("4")
print("5")
print("6")
print("7")
print("8")
print("9")
print("10")

print("Aqui é do jeito certo...")
numero = 1
print(numero)
numero = numero + 1
print(numero)
'''
# Aula 3 ---------------------------------------------------------
'''
contador = 1

while(contador <= 10):
  print(contador)
  contador = contador+1

#Lista
frutas = ["morango", "laranja", "pêra"]
print(frutas[2])

print(len(frutas))

frutas.append("manga")

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
#print(frutas[4])

i=0
while(i<4):
  print(frutas[i])
  i = i + 1

for fruta in frutas:
  pass
print(fruta)

#Criação de funções

preco = 1999.90

#Calcular apenas 5% de imposto, guardar na variavel imposto e exibir na tela
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#Criar uma função calcular_imposto() que calcular um imposto de 5% e retorna a quem pediu...
#Isso é a declaração da função (Como ela funciona)
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

#Aqui é o uso... aqui é imposto a calcular.. e exibir na tela
preco = 299
imposto = calcular_imposto(preco)
print(imposto)'''

#Aula 4 Pt 1 -----------------------------------------------------

'''
#1o. passo: importar a biblioteca sqlite3
import sqlite3

#2o. passo: Vamos estabelecer uma 
#conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3o. passo: criar um objeto do tipo cursor
cursor = conexao.cursor()

#4o. passo: comando para inserir um herói/vilão
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

#5o. passo: Executar o comando SQL
cursor.execute(sql)

#6o. passo: Confirmar o INSERT com commit() e fechar o banco
conexao.commit()
conexao.close()'''

#Aula 4 Pt 2 -----------------------------------------------------

'''
import aula4_2022_11_16c as bd

con, cur = bd.conectar()

nome = input("Informe o nome do herói/vilão: ")
nome_civil = input("Informe o nome civil do herói/vilão (sua identidade secreta): ")
tipo_numerico = input("Tecle 1 para Herói(na) ou 2 para Vilã(o): ")

#Consulta aqui a tabela grupos e exibe na tela, pedindo para o usuário digitar o grupo_id


#Consulta para o valor máximo usado no banco
sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cur.execute(sql)
pessoa_id = cur.fetchone()[0]

if tipo_numerico == "1":
  tipo = "Herói(na)"
else:
  tipo = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cur.execute(sql)

#Insert pessoas_grupos
#INSERT INTO pessoas_grupos (pessoa_id, grupo_id) VALUES (X, X)

con.commit()
con.close()'''

#Aula 5 ----------------------------------------------------------
