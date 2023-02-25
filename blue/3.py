def mismaDiferencia(arr):
    if arr == None or len(arr) == 0:
      return False

    for i in range(len(arr) - 3):
       diff1 = round(abs(arr[i+1] - arr[i]), 1)
       diff2 = round(abs(arr[i+3] - arr[i+2]), 1)
       if diff1 != diff2:
          return False
    return True

if __name__ == '__main__':
  print(mismaDiferencia([ 1, 3, 5 ]))
  print(mismaDiferencia([ 194, 54, 23, 7, 3, 6, 8 ]))
  print(mismaDiferencia([44, 37, 30, 23 ]))
  print(mismaDiferencia([ -2.3, -1.1, 0.1, 1.3, 2.5, 3.7 ]))
  print(mismaDiferencia([ 1, 8 ]))
  print(mismaDiferencia([ 3, 2, 1, 2, 3, 4, 3]))