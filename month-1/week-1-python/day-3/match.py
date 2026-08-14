#match=switch in other languages
name= input("Enter your name: ")
if name=="Harry":
    print("Hello Harry")
elif name =="Hermione":
    print("Gryffindor")
elif name =="Ron":
    print("Gryffindor")
elif name =="Draco":
    print("Slytherin")
else:
    print("Who?")

#..........
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
