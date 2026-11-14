import time
print("press enter to start the time stopwatch")
input()#user ne enter dbaya -start
start_time=time.time()#takes start time


print("again press enetr to stop stopwatch")
input()#user ne enter dbaya- stop
end_time=time.time()
elapsed_time=end_time-start_time
print("elapsed time=",round(elapsed_time,2),"seconds")


# round ki help se readable hoga jaise wowh time ko 2 decimal places tk round off krdega isliye hum round ka use krte hai,