# Process class to represent a single process
class Process:
  def __init__(self, pid, arrival_time, burst_time, priority):
    self.pid = pid # unique process id
    self.arrival_time = arrival_time # time at which the process arrives
    self.burst_time = burst_time # total cpu time required by the process
    self.priority = priority # priority of the process
    self.completion_time = 0
    self.turnaround_time = 0
    self.waiting_time = 0
    self.remaining_time = burst_time
