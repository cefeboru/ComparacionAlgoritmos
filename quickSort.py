import random
import time

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

#Tamaños de prueba
sizesArray = [10,100,1000,10000,100000,1000000]
print("Quick Sort")

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
    quickSort(unsortedList)
    endTime = time.time()
    deltaTime = endTime - startTime
    tiemposEjecucion[i] = deltaTime
    unsortedList = []
    print("Iteracion "+str(i+1)+": "+str(deltaTime))
  print("Tiempos = "+str(tiemposEjecucion))
