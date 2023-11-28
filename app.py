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



for i in range (10):
    print(i)

    nums = [1, 2, 3, 5, 6, 7, 8, 9, 10]
    for num in nums:
        print(num)

list = [1, 2, 3, 'string', ['new item'], 'kalob']
for item in list:
    print(item)

list.append('Mary')
list.remove('kalob')

# A dictionary
person = {
    "key": "value",
    "name": "Alex", 
    "twitter": "@alex",
}

print(['twitter'])

person['integram'] = "@alext.forme"
print(person)

del person['twitter']
print(person)

# A turple

food = ('yam', 'rice', 'tomatoes', 'pasta')
for i in food:
    print(i)
    print('The food items are good', i)
    print('the food item is', i)

#set are like list

s = {'item', 'item1' 'item2' 'item3'}    
print(s)
for i in s:
    print(i)


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

age = input("What is your age")
dog_age = int(age)*7 
print(dog_age)


name = "Bright"
welcome_message = "Hello {} welcome to python 101" . format(name)



       