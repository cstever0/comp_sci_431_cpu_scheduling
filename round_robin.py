from Process import Process

# Implement the SJF (SJN) function
def round_robin(process_data, quantum=2):
    # Convert the input data into Process objects
    # Sort them by arrival time first then cpu time second
    processes = [Process(*p) for p in process_data]
    processes.sort(key=lambda x: x.arrival_time)

    # Initialize scheduling variables
    current_time = 0 # Track current time in simulation
    completed_processes = [] # Store processes that have finished running
    ready_queue = [] # Store processes that have arrived but not completed
    gantt_chart = [] # Store the execution timeline

    # Main scheduling loop - continue until all processes are completed
    while len(completed_processes) < len(processes):
        # check and add any newly arrived process to the ready queue
        for process in processes:
            if process.arrival_time <= current_time and process not in completed_processes and process not in ready_queue:
                ready_queue.append(process)

        # no processes are ready
        # get the arrival time for processes that are in the future
        # assign the next arrival based on the earliest arrival time
        if not ready_queue:
            next_arrival = min([p.arrival_time for p in processes if p not in completed_processes], default=float('inf'))

            if current_time < next_arrival:
                gantt_chart.append(['IDLE'])
                current_time = next_arrival
            continue

        # get the next process from the ready queue
        # calculate the amount of time a process will run based on time quantum and remaining time
        current_process = ready_queue.pop(0)
        start_time = current_time
        run_time = min(quantum, current_process.remaining_time)
        current_time += run_time
        current_process.remaining_time -= run_time

        # update the ganntt chart with process information
        gantt_chart.append([current_process.pid, start_time, current_time])

        # Check if process has completed and update the process metrics
        # calculate turnaround time (completion time - arrival time)
        # calculate waiting time (turnaround time - cpu time)
        # move process to completed processes or to the back of the ready queue
        if current_process.remaining_time == 0:
            current_process.completion_time = current_time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            completed_processes.append(current_process)
        else:
            ready_queue.append(current_process)

    return completed_processes, gantt_chart
