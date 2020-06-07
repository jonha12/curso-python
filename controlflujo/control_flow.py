
for i in range(0,5):
  if i <3:
    print(f"{i}<3 verdadero")
  else:
    print(f"{i}<3 falso")
"""


print("************  menu  *************")

print("1.- depositar")
print("2.- retirar")
print("3.-consulta de saldo")
print("4.- retiro sin tarjeta")

numero = int(input("escribe un numero: "))
print(numero)


if numero == 1:
  print("depositaste mil pesos")
elif numero == 2:
  print("retiraste mil pesos")
elif numero == 3:
  print("susaldo es de mil pesos")
elif numero == 4:
  print("su retiro fue de mil pesos")
else:
  print("opcion invalida")
"""


