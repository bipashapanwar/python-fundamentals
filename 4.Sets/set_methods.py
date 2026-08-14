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
print(popped_item)
print(fruits)

#Clearing a set
fruits.clear()
print(fruits) #0/p-- set()

#Deleting a set
del fruits
#print(fruits) - gives NameError