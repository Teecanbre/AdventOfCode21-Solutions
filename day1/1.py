f=open("1.txt","r")
input_list=  list(map(lambda line:int(line.strip("\n")),f.readlines()))
increaseNum = 0 
for i in range(1,len(input_list)) :
	if(input_list[i] > input_list[i-1]) :
		increaseNum +=1 
print(increaseNum) 
# first solution

oldSum = 0
currentSum = 0
increaseSum = 0
for i in range(len(input_list)-3) :
	oldSum = input_list[i] + input_list[i+1] + input_list[i+2]
	currentSum = input_list[i+1] + input_list[i+2] + input_list[i+3]
	if currentSum > oldSum  : 
		increaseSum +=1
print(increaseSum)
#second solution