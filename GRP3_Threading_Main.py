#   Operating System : Threading
#   Activity 3
#
#   [Group 3]
#       Calulang, Mary Jane
#       Barrios, Armand Angelo
#       Oloroso, Andrew 

import time
import threading
import os
import random

class Fibonacci:
    def run (self, n):
        if n < 0:
            raise ValueError("\n n must be non-negative integer.")
        elif n < 2:
            return n
        else:
            return self.run(n-1) + self.run(n-2)
        
class Square:
    def run (self, n):
        if n < 0:
            raise ValueError("\n n must be non-negative integer.")
        elif n < 1:
            return n
        else:
            return n * n

class SortNumbers:
    def run (self, sort_num):
        return sorted(sort_num)



class SingleThreaded:
    def __init__ (self, fib, sqr, sort):
        self.fib = fib
        self.sqr = sqr
        self.sort = sort


    def run (self):
        print("\n---STARTING SINGLE-THREADED SYSTEM---")
        while running:
            #Fibonacci
            n = random.randint(0, 20)
            print("\nSINGLE-THREADED: n = ", n)
            try:
                fib_num = self.fib.run(n)
                print("\nSINGLE-THREADED: FIBONACCI NUMBER IS: ", fib_num)
            except ValueError as e:
                print("\nERROR: ", e)
            
            #Square
            try:
                sqr_num = self.sqr.run(n)
                print("\nSINGLE-THREADED: SQUARED NUMBER IS: [ ", sqr_num, " ]")
            except ValueError as e:
                print("\nERROR: ", e)

            #SortNumber
            sort_num = []
            for _ in range (5):
                sort_num.append(random.randint(0, 100))
            print("\nSINGLE-THREADED: sort_num = ", sort_num)
            
            try:
                sorted_num = self.sort.run(sort_num)
                print("\nSINGLE-THREADED: SORTED NUMBERS: ", sorted_num)
            except ValueError as e:
                print("\nERROR: ", e)
            
            time.sleep(2)

class MultiThreaded:
    def __init__ (self, fib, sqr, sort):
        self.fib = fib
        self.sqr = sqr
        self.sort = sort

    
    def run (self):
        print("\n---STARTING MULTI-THREADED SYSTEM---")
        while running:
            threads = []
            for i in range (5):
                sort_num = []
                for _ in range (5):
                    sort_num.append(random.randint(0, 100))
                n = random.randint(0, 20)
                
                t1 = threading.Thread(target=self.print_fib, args=(n,))
                t2 = threading.Thread(target=self.print_sqr, args=(n,))
                t3 = threading.Thread(target=self.print_sort, args=(sort_num,))


                # Append the threads to the list
                threads.append(t1)
                threads.append(t2)
                threads.append(t3)

                # Start the threads
                t1.start()
                t2.start()
                t3.start()

                # Print threads and PIDs
                print("\nTHREAD [ ", t1.name, " ] HAS PID OF : ", os.getpid())
                print("\nTHREAD [ ", t2.name, " ] HAS PID OF : ", os.getpid())
                print("\nTHREAD [ ", t3.name, " ] HAS PID OF : ", os.getpid())

            for t in threads:
                t.join

            time.sleep(1)

    def print_fib (self, n):
        try:
            fib_num = self.fib.run(n)
            print("\nMULTI-THREADED: FIBONACCI NUMBER IS: ", fib_num)
        except ValueError as e:
            print("\nERROR: ", e)
    
    def print_sqr (self, n):
        try:
            sqr_num = self.sqr.run(n)
            print("\nMULTI-THREADED: SQUARED NUMBER IS: [ ", sqr_num, " ]")
        except ValueError as e:
            print("ERROR: ", e)
    
    def print_sort (self, sort_num):
        try:
            sorted_num = self.sort.run(sort_num)
            print("\nMULTI-THREADED: SORTED NUMBERS: ", sorted_num)
        except ValueError as e:
            print("\nERROR: ", e)

running = True

fib = Fibonacci()
sqr = Square()
sort = SortNumbers()

single_threaded = SingleThreaded(fib, sqr, sort)
multi_threaded = MultiThreaded(fib, sqr, sort) 

# Single-Threaded
single_threaded_thread = threading.Thread(target=single_threaded.run)
single_threaded_thread.start()
print("\nSINGLE-THREADED SYSTEM PID: ", os.getpid())

# Multi Threaded System
multi_threaded_thread = threading.Thread(target=multi_threaded.run)
multi_threaded_thread.start()
print("\nMULTI-THREADED SYSTEM PID: ", os.getpid())

# End of program
input("\nPRESS ENTER KEY TO TERMINATE...\n")
running = False

single_threaded_thread.join()
multi_threaded_thread.join()
print("\nPROGRAM TERMINATED...")
'''

import threading
import random

class Fibonacci(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        fib_sequence = []
        for i in range(self.n):
            if i < 2:
                fib_sequence.append(i)
            else:
                fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        print("Fibonacci sequence:", fib_sequence)

class Square(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        square = self.n * self.n
        print("Square of", self.n, "is", square)

class SortNumbers(threading.Thread):
    def __init__(self, numbers):
        super().__init__()
        self.numbers = numbers

    def run(self):
        sorted_numbers = sorted(self.numbers)
        print("Sorted numbers:", sorted_numbers)

# Main method
if __name__ == '__main__':
    fibonacci_thread = Fibonacci(10)
    square_thread = Square(random.randint(1, 10))
    sort_thread = SortNumbers([random.randint(1, 100) for _ in range(5)])

    fibonacci_thread.start()
    square_thread.start()
    sort_thread.start()

    fibonacci_thread.join()
    square_thread.join()
    sort_thread.join()

    print("Program terminated.")
'''