import random
import time

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

print("Insertion Sort:")
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
