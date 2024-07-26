# Round Robin CPU Scheduling algorithm
# Input: process list, time quanta


def rr_algo(process_list,time_quanta):
    t = 0
    gantt = []
    completed = {}
    process_list.sort() # Sorted the process list according to arrival time

    
    burst_times = {}
    for p in process_list:
        pid = p[2]
        burst_time = p[1]
        burst_times[pid] = burst_time

    print("Burst Time of every process: ",burst_times)


    while process_list != []:
        available =[]
        for p in process_list:
            at = p[0] # Here i took every element Arrival time
            if p[0] <=t:
                available.append(p)
        if available == []:
            gantt.append("Idle")
            t += 1
            continue
        else:
            process = available[0]
            gantt.append(process[2]) #Here i appending process in gantt
            process_list.remove(process) #Removing the process from process list
            rem_burst = process[1] #Remaining burst time 

            if rem_burst <= time_quanta:
                t += rem_burst
                ct = t #Complition Time
                pid = process[2]
                arrival_time = process[0]
                burst_time = burst_times[pid]
                tt = ct - arrival_time # Turn-around time
                wt = tt - burst_time # Waiting Time

                completed[process[2]] = [ct,tt,wt]
                continue
            else:
                t += time_quanta
                process[1] -= time_quanta
                process_list.append(process) #Here i re-appending the process on process list

    print("The Gantt Chart of the algo:",gantt)
    print("The Array is showing ComplitionTime,Turn-aroundTime,WaitingTime: ",completed)


process_list = [[2,6,'p1'],[5,2,'p2'],[1,8,'p3'],[0,3,'p4'],[4,4,'p5']] #Arrival Time, Burst Time, Process
time_quanta = 2

rr_algo(process_list,time_quanta)




