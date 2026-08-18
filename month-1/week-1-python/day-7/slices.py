import sys
if len(sys.argv)<2:
   sys.exit("Too few arguments")
for arg in sys.argv[1:]:#to take slice of the list
   print("hello,my name is", arg)
#[1:-1],prints till the second last  items
