# function = a block of code which is executed only when it is called

def hello(first_name,last_name,age):
    print('Hello! '+first_name+' '+last_name+' ''\nYou are '+str(age)+' Years old')
    print('Have a nice day')

my_name = 'Niko'
last_name = 'Tossavainen'
age = 21
#hello('Bro')
hello(my_name,last_name,age)