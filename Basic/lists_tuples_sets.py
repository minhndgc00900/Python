grades = [44,5,51]

orderList = [x for x in range(6)] #[0, 1, 2, 3, 4, 5]

tuple_grades = (44,5,51) #immutable

set_grades = {44,5,51,5} #unordered and unique

grades.append(2)
for x in grades:
    print(x)

print("--------------------------------")

tuple_grades = tuple_grades + (19,24)

for x in tuple_grades:
    print(x)    
# print(set_grades)

print("--------------------------------")

print(orderList)