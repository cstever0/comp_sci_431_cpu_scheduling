from Process import Process

# Implement the SJF (SJN) function
def shortest_job_first(process_data):
    # Convert the input data into Process objects
    # Sort them by arrival time first then cpu time second
    processes = [Process(*p) for p in process_data]
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))

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


        # sort the ready queue by shortest cpu time
        ready_queue.sort(key=lambda x: x.burst_time)

        if not ready_queue:
            # no processes are ready
            # get the arrival time for processes that are in the future
            # assign the next arrival based on the earliest arrival time
            next_arrival = min([p.arrival_time for p in processes if p not in completed_processes], default=float('inf'))

            if current_time < next_arrival:
                gantt_chart.append(['IDLE'])
                current_time = next_arrival
            continue

        # get the shortest job from the ready queue
        # calculate the completion time based on start time + required cpu time
        current_process = ready_queue.pop(0)
        start_time = max(current_time, current_process.arrival_time)
        completion_time = start_time + current_process.burst_time

        # update the process metrics
        # calculate turnaround time (completion time - arrival time)
        # calculate waiting time (turnaround time - cpu time)
        current_process.completion_time = completion_time
        current_process.turnaround_time = completion_time - current_process.arrival_time
        current_process.waiting_time = current_process.turnaround_time - current_process.burst_time

        # update the current time
        current_time = completion_time

        # update the ganntt chart with process information
        # move process to completed processes
        gantt_chart.append([current_process.pid, start_time, completion_time])
        completed_processes.append(current_process)

    return completed_processes, gantt_chart
