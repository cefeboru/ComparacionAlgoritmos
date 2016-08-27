import time
import random

def radixsort( aList ):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1

  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range( RADIX )]

    # split aList between lists
    for  i in aList:
      tmp = i / placement
      buckets[int(tmp % RADIX)].append( i )
      if maxLength and tmp > 0:
        maxLength = False

    # empty lists into aList array
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1

    # move to next digit
    placement *= RADIX

print("Radix Sort:")
sizesArray = [10,100,1000,10000,100000,1000000]
for size in sizesArray:
  aList = [0]*size
  for i in range(0,size):
    aList[i] = random.randint(1,1000)

  tiemposEjecucion = [0.0]*10
  print("Ordenando "+str(size)+" elementos:")
  for i in range(0,10):
    #Guardamos la lista en un arreglo temporal
    unsortedList = aList[:]

    startTime = time.time()
    radixsort(unsortedList)
    endTime = time.time()
    deltaTime = endTime - startTime
    tiemposEjecucion[i] = deltaTime
    print("Iteracion "+str(i+1)+": "+str(deltaTime))
  print("Tiempos = "+str(tiemposEjecucion))
