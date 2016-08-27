import random
import time

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

sizesArray = [10,100,1000,10000,100000,1000000]
print("Bubble Sort")

for size in sizesArray:
  aList = [0]*size
  #Creamos la lista de elementos aleatorios
  for i in range(0,size):
    aList[i] = random.randint(1,10000)

  tiemposEjecucion = [0.0]*10
  print("Ordenando "+str(len(aList))+" elementos:")

  for i in range(0,10):
    unsortedList = aList[:]
    startTime = time.time()
    bubbleSort(unsortedList)
    endTime = time.time()
    deltaTime = endTime - startTime
    tiemposEjecucion[i] = deltaTime
    unsortedList = []
    print("Iteracion "+str(i+1)+": "+str(deltaTime))
  print("Tiempos = "+str(tiemposEjecucion))
