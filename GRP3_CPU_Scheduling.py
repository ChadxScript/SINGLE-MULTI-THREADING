from collections import deque
import heapq


class Process:
    def __init__(self, process_id, arrival_time, burst_time, priority):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.completion_time = 0


def round_robin_sched(processes, time_quantum):
    queue = []
    timeElapsed = 0
    n = len(processes)
    remainTime = [p.burst_time for p in processes]

    while True:
        allEnded = True

        for i in range(n):
            if remainTime[i] > 0:
                allEnded = False

                if remainTime[i] <= time_quantum:
                    timeElapsed += remainTime[i]
                    remainTime[i] = 0
                    processes[i].completion_time = timeElapsed
                else:
                    timeElapsed += time_quantum
                    remainTime[i] -= time_quantum

        if allEnded:
            break


def shortest_job_first_sched(processes):
    # Shortest Job First (SJF) CPU scheduling algorithm
    time_elapsed = 0
    n = len(processes)
    remaining_time = [p.burst_time for p in processes]

    while True:
        all_ended = True

        remaining_processes = [i for i in range(n) if remaining_time[i] > 0]

        if not remaining_processes:
            break

        min_index = min(
            remaining_processes,
            key=lambda i: remaining_time[i]
        )

        if remaining_time[min_index] > 0:
            all_ended = False
            time_elapsed += remaining_time[min_index]
            remaining_time[min_index] = 0
            processes[min_index].completion_time = time_elapsed

        if all_ended:
            break

    return processes


def preemptive_priority_sched(processes):
    queue = []
    timeElapsed = 0
    n = len(processes)

    while True:
        allEnded = True
        highest_priority = float('inf')
        highestIndex = -1

        for i in range(n):
            if processes[i].arrival_time <= timeElapsed and processes[i].priority < highest_priority and processes[i].burst_time > 0:
                allEnded = False
                highest_priority = processes[i].priority
                highestIndex = i

        if allEnded:
            break

        timeElapsed += 1
        processes[highestIndex].burst_time -= 1

        # Check if the process is completed
        if processes[highestIndex].burst_time == 0:
            processes[highestIndex].completion_time = timeElapsed

        # Update the highest priority if a new process with higher priority arrives
        highest_priority = float('inf')
        for i in range(n):
            if processes[i].arrival_time <= timeElapsed and processes[i].priority < highest_priority and processes[i].burst_time > 0:
                highest_priority = processes[i].priority
                highestIndex = i

    return processes



def calculate_metrics(processes):
    # Calculate and print performance metrics for the processes
    n = len(processes)
    print("\nProcess\t\tTurnaround time\t\tWaiting Time")
    total_waitingTime = 0
    total_turnaroundTime = 0

    for p in processes:
        turnaround_time = p.completion_time - p.arrival_time
        waitingTime = p.completion_time - p.arrival_time - p.burst_time
        total_waitingTime += waitingTime
        total_turnaroundTime += turnaround_time
        print(f"\t{p.process_id}\t\t\t{turnaround_time}\t\t\t\t\t{waitingTime}")

    cpuUtilization = total_turnaroundTime / processes[-1].completion_time
    systemThroughput = n / processes[-1].completion_time
    avg_waitingTime = total_waitingTime / n
    avg_turnaroundTime = total_turnaroundTime / n

    print(f"\nCPU UTILIZATION:\t {cpuUtilization}")
    print(f"SYSTEM THROUGHPUT:\t {systemThroughput}")
    print(f"AVERAGE TURNAROUND TIME:  {avg_turnaroundTime}s")
    print(f"AVERAGE WAITING TIME:  {avg_waitingTime}s")


def get_valid_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Input must be a positive integer. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


# Get user input for process details
processes = []
num_processes = get_valid_integer_input("Enter the number of processes: ")

for i in range(1, num_processes + 1):
    print(f"\nProcess {i}:")
    process_id = i
    arrival_time = get_valid_integer_input("Enter the arrival time: ")
    burst_time = get_valid_integer_input("Enter the burst time: ")
    priority = get_valid_integer_input("Enter the priority: ")

    process = Process(process_id, arrival_time, burst_time, priority)
    processes.append(process)

# Run scheduling algorithms
time_quantum = get_valid_integer_input("\nEnter the time quantum for Round Robin scheduling: ")

round_robin_sched(processes, time_quantum)
calculate_metrics(processes)

shortest_job_first_sched(processes)
calculate_metrics(processes)

preemptive_priority_sched(processes)
calculate_metrics(processes)

print("\nProgram terminated.")
