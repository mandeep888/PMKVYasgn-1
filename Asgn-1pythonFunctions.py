#String functions
str = "MANDEEP"
str.casefold()
str.capitalize()
str.count("e")
str.isalpha()
str.index("e")
str.istitle()
str.lstrip()
str.upper()

#List functions
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
fruits.clear()
x = fruits.copy()  #print(x)
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)   #can add whole list

#sets functions
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

x = fruits.copy()  #returns copy of the set
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)   #returns a set that are present in both sets
print(z)

fruits.pop()  #remove random item from set
print(fruits)

fruits.remove("banana") # removes specified element

#dictionary functions
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)  #create dictionary with 3 keys and value 0
print(thisdict)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"}) #add new key value pair in the dictionary
print(car)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()  #returns all the values in the dictionary
