# Decorator - A function that extends the behaviour of another function without modifying the base function
# for example @pytest.fixture()

# Basic format of decorator function
# def function_name(func):
#     def wrapper():                 # we need to add this wrapper otherwise the base function will get called without calling it
#         code
#         func()
#     return wrapper()

def add_sprinkles(func):
    def wrapper(*args,**kwargs):   # You will need to add args and kwargs so that your base function can have multiple arguments like flavour
        print("You have added Sprinkles to your icecraem 🪄")
        func(*args,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("You have added fudge 🍫")
        func(*args,**kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_icecream(flavour):
    print(f"Here is your {flavour} icecream 🍦🍦🍦🍦🍦🍦")

get_icecream("chocolate")