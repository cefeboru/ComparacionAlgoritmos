import random
import time

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

print("Selection Sort:")
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
    selectionSort(unsortedList)
    endTime = time.time()
    deltaTime = endTime - startTime
    tiemposEjecucion[i] = deltaTime
    print("Iteracion "+str(i+1)+": "+str(deltaTime))
  print("Tiempos = "+str(tiemposEjecucion))
