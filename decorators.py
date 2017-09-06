import time

#determines the time a function takes to execute.
def timing_function(thing_being_timed):


    def wrapper():
        t1 = time.time()
        thing_being_timed()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper

#this is the function being timed (adds together all the numbers from 1-whatever)
@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))


print(my_function())