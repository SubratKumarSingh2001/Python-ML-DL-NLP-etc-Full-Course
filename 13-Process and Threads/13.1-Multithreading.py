## Multithreading 
## When we need the multithreading

## I/O Bound tasks: Tasks that spend more time waiting for I/O operations like (file operations, network request)
## Concurrent Executions: When you want to improve the throughput(amount of data being send/receive over network over a period of time) of your application by performing multiple operations concurrently

import threading
import time 

def print_num(n) :
    for i in range(n) :
        time.sleep(2)
        print(f"Number: {i}")

def print_letters(string) :
    for letter in string :
        time.sleep(2)
        print(f"Letter: {letter}")


#create two different thread
t1 = threading.Thread(target=print_num, args=(5,))
t2 = threading.Thread(target=print_letters, args=("abcde",))

start_time = time.time()
#Here we have start t1 and t2 both means t1 and t2 concurrently 
t1.start()
t2.start()

#wait the threads to complete 
t1.join()
t2.join()
finished_time = time.time() - start_time
print(finished_time)



# #right now both the functions executes sequentially 
# start_time = time.time()
# print_num()
# print_letters()
# finished_time = time.time() - start_time
# print(finished_time)
