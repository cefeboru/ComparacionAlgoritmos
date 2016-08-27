import random
import time

def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)

#Tamaños de prueba
sizesArray = [10,100,1000,10000,100000,1000000]
print("Merge Sort")

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
    mergeSort(unsortedList)
    endTime = time.time()
    deltaTime = endTime - startTime
    tiemposEjecucion[i] = deltaTime
    unsortedList = []
    print("Iteracion "+str(i+1)+": "+str(deltaTime))
  print("Tiempos = "+str(tiemposEjecucion))
