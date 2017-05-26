import time
print("time is %s " %time.time() )

print("clock time is %s " %time.clock())

print("local time is %s " %str(time.localtime())) #-- convert seconds since Epoch to local time tuple

#time.sleep(1) #-- delay for a number of seconds given as a float

print("time is %s " %time.asctime(time.localtime()))

#making change 

#time.ctime() #-- convert time in seconds to string
#time.mktime(A) #-- convert local time tuple to seconds since Epoch
#time.strftime(A) #-- convert time tuple to string according to format specification


