numbers = []
readingNumbers = True
while readingNumbers:
    strInput = input("Anna luku: ")
    if strInput == "":
        readingNumbers = False
    else:
        numbers.append(int(strInput))
numbers.sort(reverse=True)
for number in numbers[:5]:
 print(number)
