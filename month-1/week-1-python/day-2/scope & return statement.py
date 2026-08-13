#Variable defined in any function can be used in that particular function-->scope
#return statement 
def main():
    x=int(input("What's x?"))
    print("x squared is",square(x))
def square(n):
    return n*n #pow(n,2)
                #n ** 2

main()
