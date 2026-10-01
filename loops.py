# print all odd numbers between 1-20

i = 1
for i in range(1,21,2):  # range(start,stop,steps)
    print(i)


# print the table of 57

i = 57
for i in range(11):
    print(i * 57)


# print all multiples of 3 from 1-50 but skip 15

for i in range(1,51):
    if i % 3 == 0:
        if i == 15 :
            continue
        else:
            print(i)


# Take two integer inputs a and b and find the 1st number between 1-1000 which is divided by both numbers

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))

for i in range(1,1000):
    if(i % a == 0 and i % b == 0):
        print(i)
        break
    else:
        i += 1
        
