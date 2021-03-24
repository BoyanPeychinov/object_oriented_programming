import functools


# class cache:
#     def __init__(self, func):
#         self.func = func
#         self.internal_cache = {}
#
#     def __call__(self, *args, **kwargs):
#         def wrapper(*args, **kwargs):
#             cache_key = args + tuple(kwargs.values())
#             if cache_key not in wrapper.internal_cache:
#                 wrapper.internal_cache[cache_key] = func(*args, **kwargs)
#             return wrapper.internal_cache[cache_key]
#
#         wrapper.internal_cache = {}
#         return wrapper


class loger:
    log_file_path = "./log.txt"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        args_str = ", ".join(args)
        kwargs_str = ", ".join(f"{key}={value}" for (key, value) in kwargs.items())
        result = self.func(*args, **kwargs)
        with open(self.log_file_path, "a") as file:
            file.write(f"{self.func.__name__}({args_str}, {kwargs_str}) returned {result}")


class uppercase:
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, self.func)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs).upper()



@uppercase
def get_message():
    return "Hello"


print(get_message())
