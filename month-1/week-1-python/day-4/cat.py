#loop
#while
i=3
while i!=0:
    print("meow")
    i=i-1 #assighment operator copies the value from right to left.

while i<3:
    print("meow")
    i+=1
#for
#list
for i in [0,1,2]:
    print("meow")
for i in range(3):
    print("meow")
#In order to use a variable which is just the need of the feature you can use _ (underscore )for it,if you don't want to name it.  for_ in range()
print("meow\n" * 3,end="")

#infinite loop
while True:
    n=int(input("What's n?"))
    if n<0:
        continue
    else:
        break

#calling meow using function
def main():
    number= get_number()
    meow(number)
def get_number():
    while True:
        n=int(input("What's n?"))
        if n>0:
            break
    return n
def meow(n):
    for _ in range(n):
        print ("meow")
main()     
