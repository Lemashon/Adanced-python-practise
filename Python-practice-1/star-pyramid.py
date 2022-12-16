def starPyramid(r):
    for x in range(r):
        print('  '*(r-x-1)+ '*'*(2*x+1))
starPyramid(500)