import numpy as np

archivo = open('prueba1.txt', 'r')
mensaje = archivo.read()

mensaje = mensaje.split("\n")

numeros = mensaje[0].split(" ")
fila = int(numeros[0])
columnas = int(numeros[1])

mensaje.pop(0)

tablero=[]
mina='*'

for s in range(len(mensaje)):
  tablero.append(list(mensaje[s]))

for i in range(len(tablero)):
    for j in range (len(tablero[i])):
        if('.' == tablero[i][j]):
            tablero[i][j] = 0


for i in range(len(tablero)):
    for j in range (len(tablero[i])):
        if(mina == tablero[i][j]):
            if (j+1) < columnas and (tablero[i][j+1]) != mina: 
                tablero[i][j+1] += 1 
            if (j-1) >= 0 and (tablero[i][j-1]) != mina:
                tablero [i][j-1] += 1 
            if (i+1) < fila and  (tablero[i+1][j]) != mina: 
                tablero[i+1][j] += 1 
            if (i-1) > 0 and  (tablero[i-1][j]) != mina:
                tablero[i-1][j] += 1 

            if (i-1) > 0 and (j+1) < columnas and (tablero[i-1][j+1]) != mina:
                tablero[i-1][j+1] +=1 
            if (i-1) >= 0 and (j-1) >= 0 and (tablero[i-1][j-1]) != mina:
                tablero[i-1][j-1] +=1 
            if (i+1) < fila and (j-1) >= 0 and (tablero[i+1][j-1]) != mina:
                tablero[i+1][j-1] +=1 
            if (i+1) <= fila and (j+1) < columnas and (tablero[i+1][j+1]) != mina:
                tablero[i+1][j+1] +=1 



for i in range(len(tablero)):
  for j in range (len(tablero[i])):
    print(tablero[i][j], end=" ")
  print("\n")
