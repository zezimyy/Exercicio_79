continuar = True
parar = "n"
numero = 0
lista = []

while continuar == True:
  numero = int(input("Digite um numero: "))
  if numero not in lista:
    lista.append(numero)
  parar = input("Deseja parar o loop? ")
  print()
  
  if parar == "s":
    continuar = False
    
  elif parar == "n":
    continuar = True

lista.sort()
for c in lista:
  print("{}, ".format(c), end="")