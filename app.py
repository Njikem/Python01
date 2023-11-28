
#print formating
name = 'Bright'
welcome_message = "Hello {} welcome to python 101" . format(name)
print(welcome_message)

name1 = 'Alice'
message = f"Hello {'Alice'} welcome to python101"

print(message)

# comparison operators
teacher = "Kalob"
if teacher == "Kalob":
    print("Welcome Kalob")
else:
    print("you are a student, welcome to python101")  

name = input("What is your name")
if name == "Bob":
    print("welcome Bob")
else:
    print("you are not Bob")

names = input("What is your name")
if names == "Bright":
    print("Welcome Bright")
   
else: 
    print("you are not Bright")
   

age = 18
if age == 18:
    print("Get access")
 
else:
    print("access denied")

#multiple comparison operator

age = 30
name = 'John'
if age == 30 and name == 'John':
    print("you can now marry")

else:
    print("Don't do anything")


# Loops

food = ['Tacos', 'Pizza', 'Salmon']
for food in food:
    print(food)
    print(f"My favorite food is{food}") 


if food == 'pizza': 
    size = input("What size would you like")
    print(f"you odered a {size} pizza") 


person = {
    "name" : "Alex",
    "twitter" : "@alexy",
    "instagram" : "@alexy.inno",
}

for key, value in person.items ():
    print(key)
    print(value)
    print(f"The key is{key} and the value is {value}")


items = ['one' 'two', 'three' 'four', 'five', 'six']
for item in items:
    if item == 'two' or item == 'four':
        continue
    print(item)

for item in items:
    if item == 'three':
        break
    print(item) 



# Function

def names (name, food):
    print(f"hello{name}. Let's eat some {food}")

    names('Kalob', 'Pizza')   