dict1=dict() #creates an empty dictionary
dict1={'key1':'value1','key2':'value2','key3':'value3'}
print(dict1) #{'key1':'value1','key2':'value2','key3':'value3'}
print(len(dict1))  #o/p- 3
print(dict1['key1'])  #value1

#a dict value can also contain list or another dictionary
resume={'name':'Bipasha Panwar','skills':['java','python','javascript','sql'],'address':{'house':15,'street':'jane street'}}
print(resume['skills'][1])  #python
print(resume['address']['street'])  #jane street

#accessing an item by keyname raises error if it doesnt exist in the dict
#use get instead as it returns None if key is not their
print(resume.get('name')) #Bipasha Panwar
print(resume.get('job'))  #None

#Items in dictionary are modifyable
resume['name']='Manvi Panwar'
print(resume)

#Checking keys in dictionary
print('key4' in dict1)   #False

#pop(key): removes the item with the specified key name:
#popitem(): removes the last item
#del: removes an item with specified key name

del dict1['key3']
del resume
print(dict1)   #{'key1': 'value1', 'key2': 'value2'}
#print(resume) - gives NameError

#The items() method changes dictionary to a list of tuples.
print(dict1.items())  #dict_items([('key1', 'value1'), ('key2', 'value2')])
#getting keys as list
dict_keys=dict1.keys()
print(dict_keys)   #dict_keys(['key1', 'key2'])
dict_values=dict1.values()
print(dict_values) #dict_values(['value1', 'value2'])



