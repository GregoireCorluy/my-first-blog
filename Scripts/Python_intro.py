print("Hello Djangogirls")

if 3>2:
    print("it works!")

if(5<6):
    print("it works too")

if(5>2):
    print("five is greater than two")
else:
    print("five is not greater than two")

#test of the if elif else statements with a comment
myName = "Grégoire"
if(myName=="Aymeric"):
    print("I am Aymeric")
elif(myName=="Grégoire"):
    print("I am Grégoire")
else:
    print("I am someone else")


def hi():
    print("Hi there!")
    print("How are you?")



hi()

def hi2(name):
    if name=='ola':
        print("hi ola")
    elif(name=='George'):
        print("hi George")
    else:
        print('hi unknown')

hi2("Gregoire")

def hiComplex(name):
    print("Hi "+name+"!")

hiComplex("Grégoire")

girls = ["Hortense","Constantine","Juliette","Claire"]

for name in girls:
    hiComplex(name)
    print("\nNext Girl please...\n")

for i in range(1,100,10):
    print(i)

for j in range(1,6):
    print(j) #6 is not included!!!