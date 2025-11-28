def greek():
    return "Hello from greet function"
print(greek()) 

def add_numbers(a, b):
    return a + b
result = add_numbers(5, 19)
print("sum", result)


def multiply_numbers(x, y):
    return x * y
product = multiply_numbers(4, 6)
print("product:", product)

def greet_user():
    name = input("Enter yoour name:")
    print("Hello,", name)
greet_user() 

def greet_user(name="Guest"):
    print("Hello,", name)

greet_user("shobha rani") 
greet_user() 

def calculate_area(a, b):
    return a + b, a - b, a * b, a / b 
area_sum, area_diff, area_product, area_division = calculate_area(10, 5)
print("Sum:", area_sum, "Difference:", area_diff, "Product:", area_product, "Division:", area_division) 


def prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            print(i, "is a factor of ", n)
        else :
            print(i, "is not a factor of", n)
result = prime_number(11)
if result:
    print("11 is a prime number")
else:
    print("11 is not a prime number") 
prime_number(15)