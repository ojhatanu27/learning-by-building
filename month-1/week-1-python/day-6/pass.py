def main():
    x=get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:  
            x=int(input("What's x?")) #we can also return here directly instead of using break
            #return int(input("What's x?")) #we can also return here directly instead of using break
        except ValueError:
            pass
        else:
            break # this break can also be replaced with return x
    return x
main()
#we can use raise keywords to raise an exception
