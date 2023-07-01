#   Operating System : Threading
#   Activity 2
#
#   [Group 3]
#       Calulang, Mary Jane
#       Barrios, Armand Angelo
#       Oloroso, Andrew

class Process:
    def __init__(self, process_id, arrival_time, burst_time, priority):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.completion_time = None


def round_robin_sched(r_processes, r_time_quantum):
    queue = []
    timeElapsed = 0
    remainingTime = [p.burst_time for p in r_processes]

    for r_process in r_processes:
        queue.append(r_process)

    # sort by burst time
    queue.sort(key=lambda p: p.arrival_time)

    while queue:
        c_process = queue.pop(0)

        if remainingTime[c_process.process_id - 1] > r_time_quantum:
            timeElapsed += r_time_quantum
            remainingTime[c_process.process_id - 1] -= r_time_quantum
            queue.append(c_process)
        else:
            timeElapsed += remainingTime[c_process.process_id - 1]
            c_process.completion_time = timeElapsed
            remainingTime[c_process.process_id - 1] = 0

    calculate_metrics(r_processes)


def shortest_job_first_sched(sjf_processes):
    queue = []
    timeElapsed = 0

    for sjf_process in sjf_processes:
        queue.append(sjf_process)

    # sort by burst time
    queue.sort(key=lambda p: p.burst_time)

    while queue:
        c_process = queue.pop(0)
        timeElapsed += c_process.burst_time
        c_process.completion_time = timeElapsed

    calculate_metrics(sjf_processes)


def preemptive_priority_sched(preemp_processes):
    queue = []
    timeElapsed = 0

    for preemp_process in preemp_processes:
        queue.append(preemp_process)

    # sort by burst time
    queue.sort(key=lambda p: p.priority)

    while queue:
        c_process = queue.pop(0)
        timeElapsed += c_process.burst_time
        c_process.completion_time = timeElapsed

    calculate_metrics(preemp_processes)


def calculate_metrics(cal_processes):
    # Calculate and print performance metrics for the processes
    n = len(cal_processes)
    print("Process\t\tTurnaround time\t\tWaiting Time")
    total_waitingTime = 0
    total_turnaroundTime = 0

    for p in cal_processes:
        turnaround_time = p.completion_time - p.arrival_time
        waitingTime = p.completion_time - p.arrival_time - p.burst_time
        total_waitingTime += waitingTime
        total_turnaroundTime += turnaround_time
        print(f"\t{p.process_id}\t\t\t{turnaround_time}\t\t\t\t\t{waitingTime}")

    cpuUtilization = total_turnaroundTime / cal_processes[-1].completion_time
    systemThroughput = n / cal_processes[-1].completion_time
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

print("\n---ROUND ROBIN---")
round_robin_sched(processes, time_quantum)

print("\n---SJF---")
shortest_job_first_sched(processes)

print("\n---PREEMPTIVE PRIORITY---")
preemptive_priority_sched(processes)