def main():
    hello("world")
    goodbye("world")
def hello(name):
    print(f"hello,{name}")
def goodbye(name):
    print(f"goodbye,{name}")
# main()

#whenever this file is loaded by python main is getting to be called
#to avoid this unitentional calling of the main function we can add  aline her
if __name__=="__main__":
   main()
