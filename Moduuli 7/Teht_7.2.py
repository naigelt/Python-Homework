Names = set()
Name = input("Give name")
while Name != "":
    if Name in Names:
        print("The name entered earlier")
        Name = input("Give name")
        if Name == "":
            break
    else:
        Names.add(Name)
        print("New name")
        if Name == "":
            break
    Name = input("Give a name")
for x in Names:
    print(x)