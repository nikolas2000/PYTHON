#exercise 1
print "the last sum is the right"
def sumIntervals(list1):
   
    data = []#create new list
    for interval in list1:
	    data.append((interval[0], 0))
	    data.append((interval[1], 1))
    data.sort()
    sum=0
    merged = []
    stack = [data[0]]
    for i in xrange(1, len(data)):
	    d = data[i]
	    if d[1] == 0:
            
	        stack.append(d)
	    elif d[1] == 1:
	        if stack:
		        start = stack.pop()
	        if len(stack) == 0:
               
		        merged.append( (start[0], d[0]))
				
    for i in merged: #for loop to sum the intervals
		
		sum+=i[1]-i[0]
		print sum #it appears all the sums because there is a problem and i cannot put the "print sum" out of loop!
		
	
sumIntervals([[1,2], [6,10],[11,15]])
	#end of the program			
			
		
