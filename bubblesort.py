def bubbleSort(a):
    b = len(a)- 1
    for x in range(b):
        for y in range(b-x):
            if a[y] > a[y+1]:
                a[y], a[y+1] = a[y+1], a[y]
    return a
a=[1,2,7,1,3,5,2,21,90,3]
bubbleSort(a)
                