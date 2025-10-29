from functools import wraps

def uppercase_decorator(func):
    @wraps(func)
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def say_hello():
    """This function returns a greeting."""
    return "hello world"

print(say_hello())
print(say_hello.__name__)  # preserves original name
print(say_hello.__doc__)
