def hello():
    print("Hello, my name is somchai.")

# hello()

def helloName(name):
    print("Hello, my name is {}".format(name))

# helloName("Pimon")
# helloName("Somchai")
    
def helloNameAge(name, age):
    print("Hello, my name is %s. My age is %d." % (name, age))

helloNameAge("Somchai", 24)


def addNumber(x, y):
    return x + y

sum = addNumber(4,1)
def calculate(z):
    return sum * z


result = calculate(5)

print(result)