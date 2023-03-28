2**3

print(2**3)

print("Grégoire")

'Grégoire'

'greg'*3
'Hi there'+' Greg'

print("Using the ' symbol")

'or like \' this'

print('Greg'.upper()) #belongs to an object, it is a method

len("Greg")

len(str(304243))

#print(int("Greg"))


print(int("100100001",2))

name = 'Gregoire'

print("my name is "+name)

print(len(name))

a=7
b=10
print(a*b)

[]

lottery = [3,8,90,17,84,65,25]

print("the length of the lottery is "+ str(len(lottery)))

print(f"other way len {len(lottery)}")

sortedList = sorted(lottery)
lottery.sort() #op object zelf toepassen

print(lottery)
print(sortedList)

print(lottery.reverse())
print("still reversed? "+ str(lottery))

lottery.append(199)

print(lottery)

print('Hello')

print(lottery[0])

print(lottery[1])

lottery.pop(0)

print(lottery)

print(lottery)
print(lottery[-1])

print(lottery[-len(lottery)])
#print(lottery[-len(lottery)-1]) out of range

{}  #dictionaries

testProgrammer = {'name':'Greg','country': 'Belgium','age':23,'Favourite numbers':[7,23]}

print("my age is "+str(testProgrammer['age']))

print(len(testProgrammer))

testProgrammer['hobby']='Chess'

print(testProgrammer['hobby'])

testProgrammer.pop('Favourite numbers')
print(testProgrammer)


testProgrammer['country']='Germany'

print(testProgrammer['country'])

5<2
3<2*2
1==1
5!=2
len([1,2,3])>len([4,5])

6>=12/2
3<=2

True and False

print(False or 1)

print(False or 7)

print("Greg"<"Constantine") #g (8) is greater than C (3)

print('a'>'b')
print('a'=='b')

a= True

b = 2>5
print(str(b)+"\n\nSpace \n")