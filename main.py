from decorators import do_twice, timer, slow_down, debug
import math

@do_twice
def say_hello():
    print("Hello")

@do_twice
def greet(name):
    print(f"Hey There {name}")

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

# This is how to apply a decorator to a standard library function
math.factorial = debug(math.factorial)

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

if __name__ == '__main__':
    # say_hello()
    # greet("General Kenobi")
    # waste_some_time(1)
    countdown(3)
