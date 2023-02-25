def mayorDiferencia(arr):
    if arr == None or len(arr) == 0:
        return 0
    menor = 1000000
    mayor = -1
    for e in arr:
        if e < menor:
            menor = e 
        if e > mayor:
            mayor = e 
    return mayor - menor


if __name__ == '__main__':
  print(mayorDiferencia( [ 1, 1, 4 ]) )
  print(mayorDiferencia( [ 9, 8 ]) )
  print(mayorDiferencia( [ 6, 22, 16, 29, 23 ]) )
  print(mayorDiferencia( [ 28, 16, 28, 11, 14, 26, 23, 25, 17, 3, 22, 23, 23, 10 ]))
