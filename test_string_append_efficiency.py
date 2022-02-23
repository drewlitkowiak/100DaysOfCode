import time



# O(n^2) growth - quadratic growth
def python_append_string(size):
    x = ''
    for _ in range(size):
        x += 'Hello'
    return x

# O(n) growth - linear growth
def python_append_list(size):
    x = []
    for _ in range(size):
        x.append('Hello')
    return ''.join(x)

# O(n) < O(n^2)
# Smaller is better for runtime!


if __name__ == '__main__':
    start_size  =   1
    # WARNING! THIS WILL TAKE A FEW MINUTES TO RUN!
    end_size    =   1000000

    # current_size == number of appends to the list/string
    current_size = start_size
    while (current_size := current_size * 10) <= end_size:
        
        append_string_begin = time.time()
        runtimes_string = []
        for i in range(100):

            # get runtime of python_append_string
            start = time.time()
            python_append_string(current_size)
            end = time.time()

            runtimes_string.append(end-start)
        append_string_end = time.time()

        append_list_begin = time.time()
        runtimes_list = []
        for i in range(100):

            # get runtime of python_append_list
            start = time.time()
            python_append_list(current_size)
            end = time.time()

            runtimes_list.append(end-start)
        append_list_end = time.time()


        print( "====================================================================")
        print(f"Average runtime for append_string with string size {current_size}: {sum(runtimes_string) / len(runtimes_string)}")
        print(f"Total runtime for append_string is {append_string_end - append_string_begin}")
        print(f"Average runtime for append_list with string size {current_size}: {sum(runtimes_list) / len(runtimes_list)}")
        print(f"Total runtime for append_list is {append_list_end - append_list_begin}")
        print( "====================================================================")



