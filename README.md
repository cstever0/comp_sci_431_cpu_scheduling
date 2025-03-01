# Comp-Sci 431 CPU Scheduling

This is an assignment from my class Computer Science 431 - Introduction to Operating Systems. It is my own attempt to create an accurate representation of how different CPU Scheduling Algorithms handle the simultaneous execution of processes.

My class and I created the function for Shortest Remaining Time Scheduling Algorithm together. I created my own interpretations of Shortest Job First and Round Robin Scheduling Algorithms. Each is located in its own .py file with the appropriate name.

If you would like to run this code. Simply clone the repository and run the print_results.py with your preferred code runner.

## Section 1: Outputs

This section includes the screenshots of the inputs and outputs from testing the algorithms. The Shortest Remaining Time and Shortest Job First Scheduling Algorithms use the inputs for processes shown in Figure 1. The Round Robin Scheduling Algorithm uses the inputs shown in Figure 2.

![image](resources/figure_1.PNG)

![image](resources/shortest_remaining_time_demo.PNG)

![image](resources/shortest_job_first_demo.PNG)

![image](resources/figure_2.PNG)

![image](resources/round_robin_demo.PNG)


## Section 2: Implementation Details

While I was creating the code to represent the way that these scheduling algorithms handle processes, I drew a lot of inspiration from the code we developed together in class. However, I made a few changes that I think simplifies the code for me personally to understand. I am not a huge fan of having a bunch of helper functions to accomplish simple tasks, so I attempted to remove the helper functions and condense the code into its main scheduling loop.

The biggest challenge I had with using this implementation is how I thought about and used the Ready Queue. When processes were supposed to be added to the ready queue, when the ready queue was supposed to be sorted and when to remove processes were all challenges that I had to consider in the implementation process. Another challenge that I had was updating the Gantt Chart properly so it would display the information on process execution that was necessary. I stumbled over this a couple times as I have never used a Gantt Chart specifically and it was particularly difficult when implementing the Round Robin Scheduling Algorithm.

I overcame these challenges by creating a flow chart on my whiteboard that I thought would be an accurate representation of how the Algorithms should execute processes. I then used that to compare to the output I was getting from my code and make changes as necessary to reflect the correct information. I also drew inspiration from the code that we had previously developed as a class. It was an incredibly useful example of how to implement a queue and use it as the basis for managing process execution. I used that code as a starting point for the basic implementation of a Scheduling Algorithm and then customized it to implement both the Shortest Job First and Round Robin Algorithms.

There were many valuable observations I made during the implementation process. One was reaffirming the effectiveness of whiteboarding a coding challenge. Having a reference to what you want your code to do before you actually try implementing the code is like having a lighthouse in the distance. You may not know how to get from where you are in the dark to the lighthouse, but it gives you a direction to head in. Another valuable insight is that when the code that you are writing continues to grow and grow it often becomes more difficult to read and understand. I found that separating each of the functions into their own files made reading, understanding, and debugging the code much simpler.
