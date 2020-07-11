#Programming for the Puzzled -- Srini Devadas
#The Best Time to Party
#Given a list of intervals when celebrities will be at the party
#Output is the time that you want to go the party when the maximum number of
#celebrities are still there.
#Clever algorithm that will work with fractional times

sched = [(6.0, 8.0, 2), (6.5, 12.0, 1), (6.5, 7.0, 2), (7.0, 8.0, 2), (7.5, 10.0, 3), (8.0, 9.0, 2),
          (8.0, 10.0, 1), (9.0, 12.0, 2), (9.5, 10.0, 4), (10.0, 11.0, 2), (10.0, 12.0, 3), (11.0, 12.0, 7)]

def bestTimeToPartySmart(schedule):

    max_count = 0
    time = 0
    # Count how many celebs with me
    for (start, _, _) in schedule:
        count = 0
        for (other_start, other_end, weight) in schedule:
            if start >= other_start and start < other_end: count=count + weight
        if count > max_count:
            max_count, time = count, start
    
    #Output best time to party
    print ('Best time to attend the party is at', time,\
           'o\'clock', ':', max_count, 'celebrities will be attending!')


bestTimeToPartySmart(sched)
        
 
                
            
        
