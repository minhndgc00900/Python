my_list = [13,56,88,451]
print(list(filter(lambda x: x != 13, my_list)))

print("------------------------------------------")

print((lambda x: x * 5)(4))

print("------------------------------------------")

print([x for x in my_list if x != 13])