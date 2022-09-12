#logical operatos (and,or,not) = used to check if two or more conditional are true

temp = int(input("What is the temprature outside?: "))

if  temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("Go outside!")
elif temp < 0 or temp >30:
    print("The temperature is bad today!")
    print("Stay inside")
