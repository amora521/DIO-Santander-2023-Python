#quando as variaveis tem valores iguais, entende-se que ocupam a mesma região de memoria
saldo = 1000
limite = 1000

print(saldo is limite)
print(saldo is not limite)

#nesse caso, como os valores são diferentes, entende-se que não estão na mesma região de memoria
saldo = 1000
limite = 100

print(saldo is limite)
print(saldo is not limite)