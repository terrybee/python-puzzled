#Programming for the Puzzled -- Srini Devadas
#The Best Time to Party
#Given a list of intervals when celebrities will be at the party
#Output is the time that you want to go the party when the maximum number of
#celebrities are still there.
#Clever algorithm that will work with fractional times

sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
            (9, 10), (10, 11), (10, 12), (11, 12)]
sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
          (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]

def bestTimeToPartySmart(schedule):

    max_count = 0
    time = 0
    # Count how many celebs with me
    for (start, _) in schedule:
        count = 0
        for (other_start, other_end) in schedule:
            if start >= other_start and start < other_end: count=count+1
        if count > max_count:
            max_count, time = count, start
    
    #Output best time to party
    print ('Best time to attend the party is at', time,\
           'o\'clock', ':', max_count, 'celebrities will be attending!')


##bestTimeToPartySmart(sched)
bestTimeToPartySmart(sched2)
        
 
                
            
        
