value1=int(input("Insert the value 1"))
value2=int(input("Insert the value 2"))

user=int(input("Press 1 for adding, 2 for subtracting, 3 for multiplying, 4 for division"))
addition=0
subtracting=0
multiplying=0
dividing=0

if user==1:
    addition=value1+value2
    print(addition)
elif user==2:
    subtracting=value1-value2
    print(subtracting)
elif user==3:
    multiplying=value1*value2
    print(multiplying)
elif user==4:
    dividing=value1/value2
    print(dividing)

