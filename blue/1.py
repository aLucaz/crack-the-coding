
def contiene(arr, n, times):
    if arr == None or len(arr) == 0:
        return False
    if times <= 0:
        return True
    for _ in range(times):
        print(arr)
        try:     
          idx = arr.index(n)
          arr.pop(idx)
        except:
          return False
    return True
    

if __name__ == '__main__':
  arreglo = [4, 5, 2, 4, 5, 9, 9, 4, 4]
  print(contiene(arreglo, 4, 5))
  arreglo = [4, 5, 2, 4, 5, 9, 9, 4, 4]
  print(contiene(arreglo, 4, 4))
  arreglo = [4, 5, 2, 4, 5, 9, 9, 4, 4]
  print(contiene(arreglo, 4, 3))
  arreglo = [4, 5, 2, 4, 5, 9, 9, 4, 4]
  print(contiene(arreglo, 9, 2))
