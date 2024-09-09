def greet():
    print("hi there")
    print("Welcome home")


greet()

# --------------------------------------------------------------------------------------------


def greet(first_name, last_name):  # parameter = fisrt_name, last_name
    print(f"Hi {first_name} {last_name}")
    print("Welcome home")


greet("Shafiul", "Alam")  # argumant = shafiul, alam
# --------------------------------------------------------------------------------------------
# 2 types of function
# 1- Perform a task
# 2- return a value [round(1.9)]


def greet(name):
    print(f"Hi {name}")


greet("Faysal")
# --------------------------------------------------------------------------------------------


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Faysal")

print(message)
file = open("content.txt", "w")
file.write(message)
# ---------------------------Keyward arguments-----------------------------------------------------------------


def increment(number, by):
    return number + by


result = increment(number=5, by=3)

print(result)


# ---------------------------Optional Parameters-----------------------------------------------------------------
def increment(number, by=1):
    return number + by


print(increment(number=5, by=3))
print(increment(number=5))


# ---------------------------Number of arguments-----------------------------------------------------------------
def multiply(x, y):
    return x * y


multiply(2, 3)
# multiply((2, 3, 4, 5))


def multiplyx(*numbers):
    print(numbers)


multiplyx(2, 3, 4, 5)


def multiplyy(*numbers):
    for number in numbers:
        print(number)


multiplyy(2, 3, 4, 5)


def multiplya(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiplya(2, 3, 4, 5))


def save_id(**id):
    print(id)
    print(id["name"])


save_id(id=1, name="Faysal", age=25)  # get dictionary

# ---------------------------scope-----------------------------------------------------------------


def name(first_name):
    last_name = "Alam"
    print(f"Hi {first_name} {last_name}")


name("Shafiul")
# print(first_name)
# print(last_name)
