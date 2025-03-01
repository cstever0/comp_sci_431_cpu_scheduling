from Process import Process

# Implement the SRT function
def shortest_remaining_time(processes_data):

  # Convert the input data into Process objects
  # Sort them by arrival time
  processes = [Process(*p) for p in processes_data]
  processes.sort(key=lambda x: x.arrival_time)

  # Initialize scheduling variables
  current_time = 0 # Track current time in simulation
  completed_processes = [] # Store processes that have finished running
  ready_queue = [] # Store processes that have arrived but not completed
  gantt_chart = [] # Store the execution timeline

  # check and add any newly arrived process to the ready queue
  def update_ready_queue():
    for process in processes:
      if(process.arrival_time <= current_time and
         process not in ready_queue and
         process not in completed_processes):
        ready_queue.append(process)

  # Find out when the next process will arrive
  def get_next_arrival_time():
    # get all processes that are in the ready queue
    # who's arrival time is in the future
    future_arrivals = [p.arrival_time for p in processes
                       if p.arrival_time > current_time and
                       p not in completed_processes]

    # return the earliest arrival time, or infinity if no more arrivals
    return min(future_arrivals) if future_arrivals else float('inf')


  # Main scheduling loop - continue until all processes are completed
  while len(completed_processes) < len(processes):

    # Step 1: Update the ready queue with any newly arrived process
    update_ready_queue()

    # Step 2: Handle case when no processes are ready to execute
    if not ready_queue:
      # Find the next process arrival time
      next_arrival = get_next_arrival_time()
      if current_time < next_arrival:
        # System will be idle
        gantt_chart.append(['IDLE'])
        current_time = next_arrival
      continue

    # Step 3: Select the process with the shortest remaining time
    # If tie, we will use arrival time as the arbitration rule
    current_process = min(ready_queue,
                          key=lambda p: (p.remaining_time, p.arrival_time))

    # Step 4: Calculate the time slice
    next_arrival = get_next_arrival_time()
    time_slice = min(
        current_process.remaining_time,
        next_arrival - current_time
    )

    # Step 5: Execute processes for the calculated time slice
    start_time = current_time # record the start time
    current_time += time_slice # advance the system clock
    current_process.remaining_time -= time_slice # update remaining time

    # update Gantt chart
    if not gantt_chart or gantt_chart[-1][0] != current_process.pid:
      # start a new entry if different process or first entry
      gantt_chart.append([current_process.pid, start_time, current_time])
    else:
      # update end time of current entry if same process
      gantt_chart[-1][2] = current_time

    # Step 6: Check if process has completed
    if current_process.remaining_time == 0:
      # update completion metrics
      current_process.completion_time = current_time

      # Turnaround time = completion time - arrival
      current_process.turnaround_time = (current_process.completion_time -
                                         current_process.arrival_time)

      # waiting time
      current_process.waiting_time = (current_process.turnaround_time -
                                      current_process.burst_time)

      # terminate the process
      # move it from the ready queue to the completed queue
      completed_processes.append(current_process)
      ready_queue.remove(current_process)

  return completed_processes, gantt_chart
