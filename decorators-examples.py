# Decorator that prints a "sprinkles" message before calling the wrapped function.
def add_sprinkles(func):
    # wrapper accepts any positional/keyword args so it can decorate any function signature
    def wrapper(*args, **kwargs):
        print("You add sprinkles!")
        func(*args, **kwargs)  # call the original function with its arguments
    return wrapper  # return the wrapper so it replaces the original function

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge!")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream!")

get_ice_cream("chocolate")

get_ice_cream("vanilla")
