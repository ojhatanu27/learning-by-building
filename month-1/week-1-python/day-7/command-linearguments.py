#sys
#sys.argv --->argument vector
"""import sys
#one way to avoid error
try:
   print("hello,my name is",sys.argv[1]) #at location 0 it stores the name of the file or path of the script
except IndexError:
   print("Too few arguments")

#another way with whoch we can avoid error
if len(sys.argv)<2:
   print("Too few arguments")
elif len(sys.argv)>2:
   print("Too many arguments") #we can have multiple elif statements but not multiple else statements.
else:
   print("hello,my name is",sys.argv[1]) #if we give space between name and surname then it will be counted as two and will not be printed but if we type the name in double quotes then it will be accepted

#sys.exit
if len(sys.argv)<2:
   sys.exit("Too few arguments")
elif len(sys.argv)>2:
   sys.exit("Too many arguments")

print("hello,my name is",sys.argv[1])"""

######
import sys
if len(sys.argv)<2:
   sys.exit("Too few arguments")
for arg in sys.argv:
   print("hello,my name is", arg)
   

