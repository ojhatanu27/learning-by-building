name=input("what's your name?").strip().title()
print(name)
#strip rmeoves spaces from the beginning and end of the string
#title() capitalizes the first letter of each word
#capitalize() capitalizes the first letter of the string
name=name.capitalize()
print(name)
#split user's name into first and last name
myname=input("what is your name?")
first,last=myname.split(" ")
print(first)
#python code can be written in interactive mode or in a script file
