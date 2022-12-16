# *args  = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple arguments
#     * unpacking operator
#     1.positional 2.default 3.keyword 4.arbitrary


def add(*nums):
    total = 0
    
    for num in nums:
        total += num
        
    return total
    

print(add(2,4,3,5,6,5,5,5))

def display_name(*args):
    for arg in args:
        print(arg, end="")
        
display_name("Dr.", "Spongebob", "Herals", "Calvin", "III")
 
def print_address(**kwargs):     
    for key,value in kwargs.items():
        print(f"{key}:{value}")
 
print_address(street="100 Penn avenues",
              apt = "100",
              city= "Washington",
              state= "New York",
              zip= "100")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end="")
    print()
    
    
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}")

shipping_label("Dr.", "Spongebob", "Herals", "Calvin", "III",
                street="100 Penn avenues",
                apt = "100",
                city= "Washington",
                state= "New York",
                zip= "100")