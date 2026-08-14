#Modulo
def main():
    x=int(input("What's x?"))
    print(parity(x))
    print(is_even(x))
    print(even(x))

def parity(x):
    if x%2==0:
        return "even"
    else:
        return "odd"
#bool
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
def even(n):
    return n%2 ==0

main()