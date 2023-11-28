x = 5
print(x)
num = [1,2,3]
print(num)
y = 'Hey there'
print(y)

if(10 < 5):
    print("Math is broken")
else:
    print("Math works!")


    item = 15
    price = 12.5
    total = item * price
    print(total)
#print formating
name = 'Bright'
welcome_message = "Hello {} welcome to python 101" . format(name)
print(welcome_message)

name1 = 'Alice'
message = f"Hello {'Alice'} welcome to python101"

print(message)

for i in range (10):
    print(i)
# comparison operators
teacher = "Kalob"
if teacher == "Kalob":
    print("Welcome Kalob")
else:
    print("you are a student, welcome to python101")  

    nums = [1, 2, 3, 5, 6, 7, 8, 9, 10]
    for num in nums:
        print(num)
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

list = [1, 2, 3, 'string', ['new item'], 'kalob']
for item in list:
    print(item)
#multiple comparison operator

list.append('Mary')
list.remove('kalob')
age = 30
name = 'John'
if age == 30 and name == 'John':
    print("you can now marry")

# A dictionary
person = {
    "key": "value",
    "name": "Alex", 
    "twitter": "@alex",
}
else:
    print("Don't do anything")

print(['twitter'])

person['integram'] = "@alext.forme"
print(person)
# Loops

del person['twitter']
print(person)
food = ['Tacos', 'Pizza', 'Salmon']
for food in food:
    print(food)
    print(f"My favorite food is{food}") 

# A turple

food = ('yam', 'rice', 'tomatoes', 'pasta')
for i in food:
    print(i)
    print('The food items are good', i)
    print('the food item is', i)
if food == 'pizza': 
    size = input("What size would you like")
    print(f"you odered a {size} pizza") 

#set are like list

s = {'item', 'item1' 'item2' 'item3'}    
print(s)
for i in s:
    print(i)
person = {
    "name" : "Alex",
    "twitter" : "@alexy",
    "instagram" : "@alexy.inno",
}

for key, value in person.items ():
    print(key)
    print(value)
    print(f"The key is{key} and the value is {value}")

list = ['one', 'two', 'three', 'four', 'five']
print(list[0])
print(list[1 : : 2])
print(list[1: 2 : 3])
print(list[-2 ::])
print(list[0 :: 3])
print(list[0 : : 4])

# Accepting input
name = input("What is you name")
print('My name is', 'Nunti')
items = ['one' 'two', 'three' 'four', 'five', 'six']
for item in items:
    if item == 'two' or item == 'four':
        continue
    print(item)

age = input("What is your age")
dog_age = int(age)*7 
print(dog_age)
for item in items:
    if item == 'three':
        break
    print(item) 


name = "Bright"
welcome_message = "Hello {} welcome to python 101" . format(name)


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



