def condition(parameter):
    if parameter > 5:
        return True
    else :
        return False

result = condition(6)

print(result)


print("--------------------------------------------------------")

name = "Fara"

def tryCondition2():
    if name in ["Fara", "fff"]:
       return "Your name must be either Fara or fff"

print(tryCondition2())


print("--------------------------------------------------------")

statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

