f = open("keimeno.txt", "r")

keimeno=f.read()
list1=list(keimeno)

list_peza=[] #lower all the letters of the text
for x in list1:
	list_peza.append(x.lower())


num=0

a=list1.count("a") 
b=list1.count("b")
c=list1.count("c")
d=list1.count("d")
e=list1.count("e")
f=list1.count("f")
g=list1.count("g")
h=list1.count("h")
i=list1.count("i")
j=list1.count("j")
k=list1.count("k")
l=list1.count("l")
m=list1.count("m")
n=list1.count("n")
o=list1.count("o")
p=list1.count("p")
q=list1.count("q")
r=list1.count("r")
s=list1.count("s")
t=list1.count("t")
u=list1.count("u")
v=list1.count("v")
w=list1.count("w")
x=list1.count("x")
y=list1.count("y")
z=list1.count("z")

sinolo=a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z
pososto_a=(float(a)/float(sinolo))*100
pososto_b=(float(b)/float(sinolo))*100
pososto_c=(float(c)/float(sinolo))*100
pososto_d=(float(d)/float(sinolo))*100
pososto_e=(float(e)/float(sinolo))*100
pososto_f=(float(f)/float(sinolo))*100
pososto_g=(float(g)/float(sinolo))*100
pososto_h=(float(h)/float(sinolo))*100
pososto_i=(float(i)/float(sinolo))*100
pososto_j=(float(j)/float(sinolo))*100
pososto_k=(float(k)/float(sinolo))*100
pososto_l=(float(l)/float(sinolo))*100
pososto_m=(float(m)/float(sinolo))*100
pososto_n=(float(n)/float(sinolo))*100
pososto_o=(float(o)/float(sinolo))*100
pososto_p=(float(p)/float(sinolo))*100
pososto_q=(float(q)/float(sinolo))*100
pososto_r=(float(r)/float(sinolo))*100
pososto_s=(float(s)/float(sinolo))*100
pososto_t=(float(t)/float(sinolo))*100
pososto_u=(float(u)/float(sinolo))*100
pososto_v=(float(v)/float(sinolo))*100
pososto_w=(float(w)/float(sinolo))*100
pososto_x=(float(x)/float(sinolo))*100
pososto_y=(float(y)/float(sinolo))*100
pososto_z=(float(z)/float(sinolo))*100



print "\nSTATISTICS PER LETTER:\n"

print "a:",pososto_a ,"%"
print "b:",pososto_b ,"%"
print "c:",pososto_c ,"%"
print "d:",pososto_d ,"%"
print "e:",pososto_e ,"%"
print "f:",pososto_f ,"%"
print "g:",pososto_g ,"%"
print "h:",pososto_h ,"%"
print "i:",pososto_i ,"%"
print "j:",pososto_j ,"%"
print "k:",pososto_k ,"%"
print "l:",pososto_l ,"%"
print "m:",pososto_m ,"%"
print "n:",pososto_n ,"%"
print "o:",pososto_o ,"%"
print "p:",pososto_p ,"%"
print "q:",pososto_q ,"%"
print "r:",pososto_r ,"%"
print "s:",pososto_s ,"%"
print "t:",pososto_t ,"%"
print "u:",pososto_u ,"%"
print "v:",pososto_v ,"%"
print "w:",pososto_w ,"%"
print "x:",pososto_x ,"%"
print "y:",pososto_y ,"%"
print "z:",pososto_z ,"%"

list2=[pososto_a,pososto_b,pososto_c,pososto_d,pososto_e,pososto_f,pososto_g,pososto_h,pososto_i,pososto_j,pososto_k,pososto_l,pososto_m,pososto_n,pososto_o,pososto_p,pososto_q,pososto_r,pososto_s,pososto_t,pososto_u,pososto_v,pososto_w,pososto_x,pososto_y,pososto_z]

list3=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print list2
list4=[]#create two new lists winthout 0%
list6=[]
for i in range(len(list2)): 
	
	if list2[i]!=0:
		list4.append(list2[i])
		list6.append(list3[i])

	
max_pososto=max(list4)
min_pososto=min(list4)
thesi_max=list4.index(max_pososto)
thesi_min=list4.index(min_pososto)
	
list7=[list6[thesi_max],max_pososto] #list with the letter and the biggest number
list8=[list6[thesi_min],min_pososto]  #list with the letter and the smallest number
print list7,list8 
#print list_peza
l=['h','h','l','f','i','e',list6[thesi_max],'f','f','e']
for i in range(len(list_peza)):
	#if list7[0] in l: #Checks if the max letter exists in the list , removes it and inserts there the min letter
	#	thesi_1=l.index(list7[0])
	#	del l[thesi_1]
	#	l.insert(thesi_1,list8[0])
	#for j in range(len(l)):
	#	if (list8[0] in l): #Checks if the min letter exists in the list , removes it and inserts there the max letter
	#		thesi_2=l.index(list8[0])
	#		del l[thesi_2]
		 
	#		l.insert(thesi_2,list7[0])
	if list_peza[i]==list7[0]:
		list_peza.remove(list_peza[i])
		
		list_peza.insert(i,list8[0])
	elif list_peza[i]==list8[0]:
		list_peza.remove(list_peza[i])
		
		list_peza.insert(i,list7[0])

		
list_kefalaia=[] #upper all the letters of the text
for x in list_peza:
	list_kefalaia.append(x.upper())

print "\n"," ".join(list_kefalaia) #join method to get the elements of the list out of it
#end of the program
