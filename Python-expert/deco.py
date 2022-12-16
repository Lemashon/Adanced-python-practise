from time import time

def multiply(x, y):
    return x*y

before = time()
print('time before', before)
print('add(10)', multiply(1989878690089709876543287678012345678900987654,1234567890987654321))
after = time()
print('time after', after)
print('time taken', after - before)
