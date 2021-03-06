"""
File to save decorators for study purposes
@author: Marco Boaretto
from: https://realpython.com/primer-on-python-decorators/#functions
"""
import functools
import time


## Old examples
# def do_twice(func):
#     def wrapper:
#         func()
#         func()
#     return wrapper
#
# def do_twice_with_args(func):
#     """
#     do_twice decorator that allows arguments input
#     """
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return wrapper_do_twice

def do_twice(func):
    @functools.wraps(func)
    # this allow introspection for the function
    # that uses this decorator.
    # Introspection ability of an object to know about
    # its own attributes at runtime
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
        # this makes sure the wrapper function returns
        # the return value of the decorated function
    return wrapper_do_twice

## Good template for decorators
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

## Timer function
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

# Debbuger decorator
def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

# Decorator to slow down function, useful when you want to rate-limit the function
def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down\

## Registering Plugins
