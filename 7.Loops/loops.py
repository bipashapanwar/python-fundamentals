#Two types of loops: 1.For   2.While
for i in range(1,8):
    print('#'*i)

print('-----------------------------------------------')

language=['python','java','javascript','html','css']
for i in language:
    print(i)

print('-----------------------------------------------')

table=8
for i in range(1,11):
    print(f'{table}X{i}={table*i}')

print('-----------------------------------------------')
for i in range(51):
    if i%2==0:
        print(i)

sum=0
for i in range(51):
    sum+=i
print('Sum:',sum)