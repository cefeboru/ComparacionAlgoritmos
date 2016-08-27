import time

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

numberElements = [10,100,1000,10000,1000000]
aList = []
startTime = time.time()
radixsort(aList)
endTime = time.time()
print("Se ordeno la lista en "+ str(endTime - startTime) )
