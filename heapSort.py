import time
import random

def heapsort( aList ):
  # convert aList to heap
  length = len( aList ) - 1
  leastParent = int(length / 2)
  for i in range ( leastParent, -1, -1 ):
    moveDown( aList, i, length )
 
  # flatten heap into sorted array
  for i in range ( length, 0, -1 ):
    if aList[0] > aList[i]:
      swap( aList, 0, i )
      moveDown( aList, 0, i - 1 )
 
 
def moveDown( aList, first, last ):
  largest = 2 * first + 1
  while largest <= last:
    # right child exists and is larger than left child
    if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
      largest += 1
 
    # right child is larger than parent
    if aList[largest] > aList[first]:
      swap( aList, largest, first )
      # move down to largest child
      first = largest;
      largest = 2 * first + 1
    else:
      return # force exit
 
 
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp


print("Heap Sort:")
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
    heapsort(unsortedList)
    endTime = time.time()
    deltaTime = endTime - startTime
    tiemposEjecucion[i] = deltaTime
    print("Iteracion "+str(i+1)+": "+str(deltaTime))
  print("Tiempos = "+str(tiemposEjecucion))
