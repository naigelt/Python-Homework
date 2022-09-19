# tuple = collection which is ordered and unchangeable
# used to group together realted data

student = ("Niko",21,"Male")

print(student.count("Niko"))
print(student.index("Male"))

for x in student:
    print(x, end=", ")

if "Niko" in student:
    print("\nNiko is here")