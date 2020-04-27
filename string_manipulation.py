## Strings manipulations

first_name = "Anoop"
last_name = "Singh"

full_name = first_name +" "+ last_name

print(full_name)

## number must me chages first in string to add, concatenation both in one string

number = '5'

print(full_name + " "+ number)

print(full_name *3)

print(full_name[0:5])
print(full_name[::-1])

print(full_name[-5:-1])

###input function

name = input("Enter your name please")
print(name)
print("Hello "+name)

age = input("Please enter you age")
print("Your age is " + age)
number_one = int(input("Please enter your first number"))

number_two = int(input("please enter your second number"))

total = number_one + number_two

print("your total is ",total)

# how to declare multiple variables in one line

name, age = "Anoop", "37"
print("Hello "+name+ " your age is " + age)

name, age = input("enter your name and age ").split(",")
print(name)
print(age)



###String formating

name = "Anoop"

age = 37

print(f"Hello {name} your age is {age}")


## step agrument

print("Anoopsingh"[0:6])


name = input("Enter your name please")
reverse = name[::-1]
print(f"reverse of your name is {reverse}")


#### methods in string

#len() function, lower(), upper(), title() and count() mehtods
# methods we normally use dot

print(len(name))

print(name.lower())
print(name.upper())

print(name.title())

print(name.count("o"))# count letters in you string

name, char = input("enter comma separated name and character : ").split(",")

print(f"length of your name is {len(name)}")
print(f"character count : {name.lower().count(char.lower())}")

