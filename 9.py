
 


def maxSequence(list1): # the function sums all the elements of a list and prints the elements in row with the biggest sum
	i=0
	j=0
	max=0
	sum=0
	start=0
	list2=[]
	maxlist=[]
	for j in range(len(list1)): 
		
		
		
		 
		for start in range(j+1): #second 'for' loop to set the start of the sum
			for i in range(start,j+1): #third 'for' loop to set the length of the sum
				list2.append(list1[i])#we put the elements in new list in order to sum them
				sum+= list1[i]
				if sum>max: #find the maximum sum 
					max=sum
					maxlist=list2
			sum=0
			list2=[]
	print max,":",maxlist
	#end of the program
			 
	
maxSequence([-2,1,-3,4,-1,2,1,-5,4])
