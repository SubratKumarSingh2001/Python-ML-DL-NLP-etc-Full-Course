## Multiple Process: Process which runs parallel

## When we use Multiprocessing 
## CPU Bound Tasks: Tasks that are heavy on CPU usage(ex: Mathematical Computation, data processing, etc)
## Parallel Processing: Using Multiple cores of CPU

import multiprocessing
import time

def print_square() :
    for i in range(5) :
        time.sleep(1)
        print(f"Square: {i * i}")

def print_cube() :
    for i in range(5) :
        time.sleep(1.5)
        print(f"Cube: {i * i * i}")


if __name__ == "__main__" :
    #Now we need to create two process and each process have separate memory and they dont interfere each other
    p1 = multiprocessing.Process(target=print_square)
    p2 = multiprocessing.Process(target=print_cube)

    start_time = time.time()
    #start the process
    p1.start()
    p2.start()

    #wait until all the process is completed 
    p1.join()
    p2.join()

    finished_time = time.time() - start_time
    print(finished_time)

