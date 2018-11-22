from decorators import do_twice, timer


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

if __name__ == '__main__':
    say_hello()
    greet("General Kenobi")
    waste_some_time(1)
