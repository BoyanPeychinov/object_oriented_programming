import functools
from time import time


def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"{func.__name__} executed in {end - start} milliseconds")
        return result

    return wrapper


def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


def debug(func):
    """print func name with args, kwargs and result"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(args)
        kwargs_str = ", ".join(f"{key}={value}" for (key, value) in kwargs.items())
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args_str}, {kwargs_str}) returned {result}")
        return result

    return wrapper


def cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.values())
        if cache_key not in wrapper.internal_cache:
            wrapper.internal_cache[cache_key] = func(*args, **kwargs)
        return wrapper.internal_cache[cache_key]

    wrapper.internal_cache = {}
    return wrapper


def repeat(count):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(count):
                func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def print_hello_message(name):
    print(get_hello_message(name))


@cache
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n - 2)


@debug
@uppercase
def get_hello_message(name):
    return f"Hello, I am {name}"


@measure_time
def big_loop():
    x = 0
    for _ in range(100000):
        x += 1


# big_loop()
msg = get_hello_message("Boko")

print(fibonacci.internal_cache)

print_hello_message("Gosho")