


###################
while True:
    try:  
        x=int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")
###############
while True:
    try:
        x=int(input("What's x?"))
        break
    except ValueError:
        print("x is not an integer")
print(f"x is {x}")
############
def main():
    x=get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:  
            x=int(input("What's x?")) #we can also return here directly instead of using break
            #return int(input("What's x?")) #we can also return here directly instead of using break
        except ValueError:
            print("x is not an integer")
        else:
            break # this break can also be replaced with return x
    return x
main()