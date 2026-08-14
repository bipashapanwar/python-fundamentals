#que 1:legal driving age or not
age=17
if age<18:
    print(f"You need to wait {18-age} years")
else:
    print("You can drive")

#que 2: check fruit in fruits else add
fruits=['apple','mango','pineapple','lime','banana']
fruit='cherry'
if not fruit in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print(f"{fruit} already in fruits")

#que 3: marks and grade
marks=92
if marks<50 and marks>0:
    print('grade C')
elif marks>=50 and marks<70:
    print('grade B')
elif marks>=70 and marks<=100:
    print('grade A')
else:
    print("Invalid marks")