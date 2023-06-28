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
    def run(self, n):
        if n < 0:
            raise ValueError("N MUST BE NON-NEGATIVE INTEGER.")
        elif n < 2:
            return n
        else:
            return self.run(n - 1) + self.run(n - 2)


class Square:
    def run(self, n):
        if n < 0:
            raise ValueError("N MUST BE NON-NEGATIVE INTEGER.")
        elif n < 1:
            return n
        else:
            return n * n


class SortNumbers:
    def run(self, sort_num):
        return sorted(sort_num)


class SingleThreaded:
    def __init__(self, s_fib, s_sqr, s_sort):
        self.fib = s_fib
        self.sqr = s_sqr
        self.sort = s_sort

    def run(self):
        print("\n\n---STARTING SINGLE-THREADED SYSTEM---")
        # Fibonacci
        n = random.randint(0, 20)
        try:
            # fib_num = self.fib.run(n)
            fib_num = [self.fib.run(i) for i in range(n + 1)]
            print("[SINGLE-THREADED]\t n: ", n)
            print("[SINGLE-THREADED]\t FIBONACCI NUMBER IS: ", fib_num, "\n")
        except ValueError as e:
            print("\nERROR: ", e)

        # Square
        try:
            sqr_num = self.sqr.run(n)
            print("[SINGLE-THREADED]\t n: ", n)
            print("[SINGLE-THREADED]\t SQUARED NUMBER IS: [", sqr_num, "]\n")
        except ValueError as e:
            print("\nERROR: ", e)

        # SortNumber
        sort_num = []
        for _ in range(5):
            sort_num.append(random.randint(0, 100))

        try:
            sorted_num = self.sort.run(sort_num)
            print("[SINGLE-THREADED]\t UNSORTED NUMBERS: ", sort_num)
            print("[SINGLE-THREADED]\t SORTED NUMBERS: ", sorted_num, "\n")
        except ValueError as e:
            print("\nERROR: ", e)


class MultiThreaded:
    def __init__(self, m_fib, m_sqr, m_sort):
        self.fib = m_fib
        self.sqr = m_sqr
        self.sort = m_sort

    def run(self):
        print("\n\n---STARTING MULTI-THREADED SYSTEM---")
        threads = []
        for i in range(5):
            sort_num = []
            for _ in range(5):
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
            print("[MULTI-THREADED]\t THREAD [", t1.name, "] HAS PID OF : ", os.getpid())
            print("[MULTI-THREADED]\t THREAD [ ", t1.name, " ] HAS THREAD ID OF : ", threading.get_ident())
            t2.start()
            print("[MULTI-THREADED]\t THREAD [ ", t2.name, " ] HAS PID OF : ", os.getpid())
            print("[MULTI-THREADED]\t THREAD [ ", t2.name, " ] HAS THREAD ID OF : ", threading.get_ident())
            t3.start()
            print("[MULTI-THREADED]\t THREAD [ ", t3.name, " ] HAS PID OF : ", os.getpid())
            print("[MULTI-THREADED]\t THREAD [ ", t3.name, " ] HAS THREAD ID OF : ", threading.get_ident())

            t1.join()
            t2.join()
            t3.join()

            for t in threads:
                t.join()

    def print_fib(self, n):
        try:
            fib_num = [self.fib.run(i) for i in range(n + 1)]
            print("[MULTI-THREADED]\t n: ", n)
            print("[MULTI-THREADED]\t FIBONACCI NUMBER IS: ", fib_num, "\n")
            time.sleep(1)
        except ValueError as e:
            print("\nERROR: ", e)

    def print_sqr(self, n):
        try:
            sqr_num = self.sqr.run(n)
            print("[MULTI-THREADED]\t n: ", n)
            print("[MULTI-THREADED]\t SQUARED NUMBER IS: [", sqr_num, "]\n")
            time.sleep(2)
        except ValueError as e:
            print("ERROR: ", e)

    def print_sort(self, sort_num):
        try:
            sorted_num = self.sort.run(sort_num)
            print("[MULTI-THREADED]\t UNSORTED NUMBERS: ", sort_num)
            print("[MULTI-THREADED]\t SORTED NUMBERS: ", sorted_num, "\n")
            time.sleep(3)
        except ValueError as e:
            print("\nERROR: ", e)


fib = Fibonacci()
sqr = Square()
sort = SortNumbers()

single_threaded = SingleThreaded(fib, sqr, sort)
multi_threaded = MultiThreaded(fib, sqr, sort)

# Single-Threaded
single_threaded = threading.Thread(target=single_threaded.run)
single_threaded.start()
print("[SINGLE-THREADED]\t SYSTEM PID: ", os.getpid())
single_threaded.join()

# Multi Threaded System
multi_threaded = threading.Thread(target=multi_threaded.run)
multi_threaded.start()
print("[MULTI-THREADED]\t SYSTEM PID: ", os.getpid())
single_threaded.join()
