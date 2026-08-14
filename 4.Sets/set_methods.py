#Creating a set
s1=set()  #empty set 
#{} cannot use this because it will create a empty dictionary

fruits={'apple','mango','orange','banana'}
#will give o/p in different order each time, bcs sets are unordered and unindexed
print(fruits)  #o/p-- {'orange', 'apple', 'banana', 'mango'}

#Adding items to the set
fruits.add('kiwi') #for single item
print(fruits) #o/p-- {'kiwi', 'orange', 'mango', 'banana', 'apple'}
fruits.update(('plum','peach')) #for multiple items, it takes a list or tuple argument
print(fruits) #o/p-- {'peach', 'plum', 'kiwi', 'orange', 'mango', 'banana', 'apple'}

#Removing elements
fruits.remove('banana') #raises error if it doesnt exist
fruits.discard('banana') #doesnt raise error in such case
print(fruits)
popped_item=fruits.pop() #removes random item and returns it
print(popped_item)  #peach
print(fruits)       #{'apple', 'kiwi', 'plum', 'mango', 'orange'}

#Clearing a set
fruits.clear()
print(fruits) #0/p-- set()

#Deleting a set
del fruits
#print(fruits) - gives NameError

#Update a set
num1={1,2,3,4,5}
num2={6,7,8,9,10}
num1.update(num2)     #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(num1)

#Union (|) and Intersection (&)
city1={'delhi','bombay','pune','portofino'}
city2={'indore','jabalpur','nyc','delhi'}
print(city1.union(city2))  #{'bombay', 'jabalpur', 'pune', 'nyc', 'portofino', 'indore', 'delhi'}
print(city1.intersection(city2))  #{'delhi'}

#Check subset and superset
whole_numbers={0,1,2,3,4,5,6,7,8,9,10}
even_numbers={2,4,6,8,10}
print(whole_numbers.issuperset(even_numbers)) #True
print(whole_numbers.issubset(even_numbers)) #False bcs its super set

#Disjoint set - if two sets dont have anything in common they are disjoint
print(city1.isdisjoint(city2)) #False