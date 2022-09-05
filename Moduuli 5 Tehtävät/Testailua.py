numbers = []
number = 0
while number!="":
    number = input(str("Give a number or press enter to exit: "))
    if number !="":
        numbers.append(number)
        eva = [eval(i) for i in numbers]
        if number == "":
            break
eva.sort(reverse=True)
f1 = eva[0:5]
print(f"{f1}")