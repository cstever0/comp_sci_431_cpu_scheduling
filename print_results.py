from Process import Process
from shortest_remaining_time import shortest_remaining_time
from shortest_job_first import shortest_job_first
from round_robin import round_robin

def print_results(completed_processes, gantt_chart):
    """Print formatted scheduling results and metrics."""
    # Print Gantt chart showing execution order
    print("\nProcess Execution Order (Gantt Chart):")
    print("-" * 50)
    for entry in gantt_chart:
        if entry[0] == "IDLE":
            # Show idle time periods
            print(f"IDLE: {entry[1]} -> {entry[2]}")
        else:
            # Show process execution periods
            print(f"P{entry[0]}: {entry[1]} -> {entry[2]}")

    # Print detailed process metrics
    print("\nProcess Scheduling Details:")
    print("-" * 65)
    print("PID  Arrival  Burst  Completion  Turnaround  Waiting")
    print("-" * 65)

    # Print metrics for each process, sorted by PID
    for p in sorted(completed_processes, key=lambda x: x.pid):
        print(f"{p.pid:<5}{p.arrival_time:<9}{p.burst_time:<7}"
              f"{p.completion_time:<12}{p.turnaround_time:<12}"
              f"{p.waiting_time}")

    # Calculate and print average metrics
    avg_turnaround = sum(p.turnaround_time for p in completed_processes) / len(completed_processes)
    avg_waiting = sum(p.waiting_time for p in completed_processes) / len(completed_processes)

    print("-" * 65)
    print(f"Average Turnaround Time: {avg_turnaround:.2f}")
    print(f"Average Waiting Time: {avg_waiting:.2f}")


# process_id, arrival_time, burst_time, priority
processes_srt_sjf = [[1, 0, 3, 1],
             [2, 2, 6, 1],
             [3, 4, 4, 1],
             [4, 6, 5, 1],
             [5, 8, 2, 1]]

processes_rr = [[1, 0, 2, 2],
             [2, 1, 1, 1],
             [3, 2, 8, 4],
             [4, 3, 4, 2],
             [5, 4, 5, 3]]

completed_processes_srt, gantt_chart_srt = shortest_remaining_time(processes_srt_sjf)
completed_processes_sjf, gantt_chart_sjf = shortest_job_first(processes_srt_sjf)
completed_processes_rr, gantt_chart_rr = round_robin(processes_rr)

# print(completed_processes)
print("\nShortest Remaining Time Demonstration")
print("-" * 50)
print_results(completed_processes_srt, gantt_chart_srt)
print("\nShortest Job First Demonstration")
print("-" * 50)
print_results(completed_processes_sjf, gantt_chart_sjf)
print("\nRound Robin Demonstration")
print("-" * 50)
print_results(completed_processes_rr, gantt_chart_rr)
