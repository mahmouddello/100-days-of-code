import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_func():
        # before - actions
        start_time = time.time()
        function()
        # after - actions
        end_time = time.time()
        print(f"{function.__name__} took {end_time - start_time} to finish")

    return wrapper_func()


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i
