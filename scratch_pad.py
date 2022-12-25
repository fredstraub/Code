print("Hello World")

print("Hello Amazing", end=" ")
print("World")

print("Add then subtract two numbers.")
x = int(input())
y = int(input())
print(x + y)
print(x - y)

print("Is this number even?")
x = int(input())
if x % 2 == 0:
    print("yay")
else:
    print("nay")

n = x
for i in range(n+1):
	print(i)

class doesNothing:
	pass

#String to list
yourString =  "2 0 1 7 22 2"

def stringToList(string):
	myList = list(yourString.split(" "))
	return myList

print(stringToList(yourString))

print(sorted(set(stringToList(yourString))))